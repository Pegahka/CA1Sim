__author__ = 'milsteina'
from nested import *
from plot_parallel_optimize_results import *
from scipy.stats import skewnorm

"""
These methods aim to optimize a single parameterization of a model of bidirectional, state-dependent behavioral time 
scale synaptic plasticity to account for the width and amplitude of all place fields in an experimental data set from 
the Magee lab that includes: 
1) Silent cells converted into place cells by spontaneous plateaus
2) Silent cells converted into place cells by experimentally induced plateaus
3) Existing place cells that shift their place field locations after an experimentally induced plateau

Features/assumptions of the phenomenological model:
1) Synaptic weights in a silent cell are all = 1 prior to field induction 1. w(t0) = 1
2) Activity at each synapse generates a long duration 'local signal', or an 'eligibility trace' for plasticity.
3) Dendritic plateaus generate a long duration 'global signal', or an 'availability trace' for plasticity.
4) Synaptic weights w1 at time t1 after a plateau are a function of the initial weights w0 at time t0, and the two
plasticity signals.

Features/assumptions of the mechanistic model:
1) Synaptic strength is equivalent to the number of AMPA-Rs at a synapse (quantal size). 
2) Dendritic plateaus generate a global signal that increases the size of a pool of mobile AMPA-Rs, available for stable
incorporation into synapses.
3) Activity at each synapse generates a local signal that increases the number of eligible slots to capture mobile 
AMPA-Rs.
4) Both signals interact at already potentiated synapses to destabilize captured AMPA-Rs, returning them to the mobile 
pool, and reducing the number of eligible slots. 
5) AMPAR-s can be in 2 states (Markov-style kinetic scheme):
 
        rMC0 * global_signal * local_signal
M (mobile) <----------------------> C (captured by a synapse)
       rCM0 * global_signal * f(local_signal)

6) At rest 100% of non-synaptic receptors are in state M, mobile and available for synaptic capture.
7) Global signal gates the transition rate from state M (mobile AMPA-Rs) to state C (captured AMPA-Rs), proportional
to the amount of local signal.
8) Global signal also gates return of receptors from state C to state M, depending on a non-monotonic function of local
signal and current weight (occupancy of state C).
"""

script_filename = 'parallel_optimize_bidirectional_BTSP_CA1.py'

context = Context()


def config_interactive(config_file_path='data/parallel_optimize_BTSP_CA1_simple_config.yaml',
                       output_dir='data', temp_output_path=None, export_file_path=None, verbose=True, disp=True):
    """
    :param config_file_path: str (.yaml file path)
    :param output_dir: str (dir path)
    :param temp_output_path: str (.hdf5 file path)
    :param export_file_path: str (.hdf5 file path)
    :param verbose: bool
    :param disp: bool
    """
    config_dict = read_from_yaml(config_file_path)
    if 'param_gen' in config_dict and config_dict['param_gen'] is not None:
        param_gen_name = config_dict['param_gen']
    else:
        param_gen_name = 'BGen'
    param_names = config_dict['param_names']
    if 'default_params' not in config_dict or config_dict['default_params'] is None:
        default_params = {}
    else:
        default_params = config_dict['default_params']
    for param in default_params:
        config_dict['bounds'][param] = (default_params[param], default_params[param])
    bounds = [config_dict['bounds'][key] for key in param_names]
    if 'rel_bounds' not in config_dict or config_dict['rel_bounds'] is None:
        rel_bounds = None
    else:
        rel_bounds = config_dict['rel_bounds']
    if 'x0' not in config_dict or config_dict['x0'] is None:
        x0 = None
    else:
        x0 = config_dict['x0']
    feature_names = config_dict['feature_names']
    objective_names = config_dict['objective_names']
    target_val = config_dict['target_val']
    target_range = config_dict['target_range']
    optimization_title = config_dict['optimization_title']
    kwargs = config_dict['kwargs']  # Extra arguments to be passed to imported submodules

    if 'update_params' not in config_dict or config_dict['update_params'] is None:
        update_params = []
    else:
        update_params = config_dict['update_params']
    update_params_funcs = []
    for update_params_func_name in update_params:
        func = globals().get(update_params_func_name)
        if not callable(func):
            raise Exception('parallel_optimize: update_params: %s is not a callable function.'
                            % update_params_func_name)
        update_params_funcs.append(func)

    if temp_output_path is None:
        temp_output_path = '%s/parallel_optimize_temp_output_%s_pid%i.hdf5' % \
                        (output_dir, datetime.datetime.today().strftime('%m%d%Y%H%M'), os.getpid())
    if export_file_path is None:
        export_file_path = '%s/%s_%s_%s_optimization_exported_output.hdf5' % \
                           (output_dir, datetime.datetime.today().strftime('%m%d%Y%H%M'), optimization_title,
                            param_gen_name)
    x0_array = param_dict_to_array(x0, param_names)
    context.update(locals())
    context.update(kwargs)
    config_engine(update_params_funcs, param_names, default_params, temp_output_path, export_file_path, output_dir,
                  disp, **kwargs)
    update_submodule_params(x0_array)


def config_controller(export_file_path, output_dir, **kwargs):
    """

    :param export_file_path: str
    :param output_dir: str
    """
    processed_export_file_path = export_file_path.replace('.hdf5', '_processed.hdf5')
    context.update(locals())
    context.update(kwargs)
    init_context()


def config_engine(update_params_funcs, param_names, default_params, temp_output_file_path, export_file_path, output_dir,
                  disp, data_file_name, **kwargs):
    """
    :param update_params_funcs: list of function references
    :param param_names: list of str
    :param default_params: dict
    :param temp_output_file_path: str
    :param export_file_path: str
    :param output_dir: str (path)
    :param disp: bool
    :param data_file_name: str (path)
    """
    param_indexes = {param_name: i for i, param_name in enumerate(param_names)}
    processed_export_file_path = export_file_path.replace('.hdf5', '_processed.hdf5')
    context.update(locals())
    context.update(kwargs)
    init_context()


def init_context():
    """

    """
    context.data_file_path = context.output_dir + '/' + context.data_file_name
    with h5py.File(context.data_file_path, 'r') as f:
        dt = f['defaults'].attrs['dt']  # ms
        input_field_width = f['defaults'].attrs['input_field_width']  # cm
        input_field_peak_rate = f['defaults'].attrs['input_field_peak_rate']  # Hz
        num_inputs = f['defaults'].attrs['num_inputs']
        track_length = f['defaults'].attrs['track_length']  # cm
        binned_dx = f['defaults'].attrs['binned_dx']  # cm
        generic_dx = f['defaults'].attrs['generic_dx']  # cm
        default_run_vel = f['defaults'].attrs['default_run_vel']  # cm/s
        generic_position_dt = f['defaults'].attrs['generic_position_dt']  # ms
        default_interp_dx = f['defaults'].attrs['default_interp_dx']  # cm
        ramp_scaling_factor = f['defaults'].attrs['ramp_scaling_factor']
        binned_x = f['defaults']['binned_x'][:]
        generic_x = f['defaults']['generic_x'][:]
        generic_t = f['defaults']['generic_t'][:]
        default_interp_t = f['defaults']['default_interp_t'][:]
        default_interp_x = f['defaults']['default_interp_x'][:]
        extended_x = f['defaults']['extended_x'][:]
        input_rate_maps = f['defaults']['input_rate_maps'][:]
        peak_locs = f['defaults']['peak_locs'][:]
        if 'data_keys' not in context() or context.data_keys is None:
            data_keys = [(int(cell_id), int(induction)) for cell_id in f['data'] for induction in f['data'][cell_id]]
        spont_cell_id_list = [int(cell_id) for cell_id in f['data'] if f['data'][cell_id].attrs['spont']]
    down_dt = 10.  # ms, to speed up optimization
    context.update(locals())
    context.input_matrix = compute_EPSP_matrix(input_rate_maps, generic_x)
    context.sm = StateMachine(dt=down_dt)
    context.cell_id = None
    context.induction = None
        

def import_data(cell_id, induction):
    """
    
    :param cell_id: int 
    :param induction: int
    """
    if cell_id == context.cell_id and induction == context.induction:
        return
    cell_key = str(cell_id)
    induction_key = str(induction)
    with h5py.File(context.data_file_path, 'r') as f:
        if cell_key not in f['data'] or induction_key not in f['data'][cell_key]:
            raise KeyError('parallel_optimize_bidirectional_BTSP_CA1: no data found for cell_id: %s, induction: %s' %
                           (cell_key, induction_key))
        else:
            context.cell_id = cell_id
            context.induction = induction
        this_group = f['data'][cell_key][induction_key]
        context.induction_locs = this_group.attrs['induction_locs']
        context.induction_durs = this_group.attrs['induction_durs']
        context.exp_ramp_raw = {'after': this_group['raw']['exp_ramp']['after'][:]}
        if 'before' in this_group['raw']['exp_ramp']:
            context.exp_ramp_raw['before'] = this_group['raw']['exp_ramp']['before'][:]
        context.position = {}
        context.t = {}
        context.current = []
        for category in this_group['processed']['position']:
            context.position[category] = []
            context.t[category] = []
            for i in xrange(len(this_group['processed']['position'][category])):
                lap_key = str(i)
                context.position[category].append(this_group['processed']['position'][category][lap_key][:])
                context.t[category].append(this_group['processed']['t'][category][lap_key][:])
        for i in xrange(len(this_group['processed']['current'])):
            lap_key = str(i)
            context.current.append(this_group['processed']['current'][lap_key][:])
        context.mean_position = this_group['processed']['mean_position'][:]
        context.mean_t = this_group['processed']['mean_t'][:]
        context.exp_ramp = {'after': this_group['processed']['exp_ramp']['after'][:]}
        context.exp_ramp_vs_t = {'after': this_group['processed']['exp_ramp_vs_t']['after'][:]}
        if 'before' in this_group['processed']['exp_ramp']:
            context.exp_ramp['before'] = this_group['processed']['exp_ramp']['before'][:]
            context.exp_ramp_vs_t['before'] = this_group['processed']['exp_ramp_vs_t']['before'][:]
        context.SVD_ramp = {}
        context.SVD_ramp['after'] = this_group['processed']['SVD_ramp']['after'][:]
        if 'before' in this_group['processed']['SVD_ramp']:
            context.SVD_ramp['before'] = this_group['processed']['SVD_ramp']['before'][:]
        context.SVD_weights = {}
        context.SVD_weights['before'] = this_group['processed']['SVD_weights']['before'][:]
        context.SVD_weights['after'] = this_group['processed']['SVD_weights']['after'][:]
        context.complete_run_vel = this_group['complete']['run_vel'][:]
        context.complete_run_vel_gate = this_group['complete']['run_vel_gate'][:]
        context.complete_position = this_group['complete']['position'][:]
        context.complete_t = this_group['complete']['t'][:]
        context.induction_gate = this_group['complete']['induction_gate'][:]
    context.mean_induction_loc = np.mean(context.induction_locs)
    context.complete_rate_maps = get_complete_rate_maps()
    context.down_t = np.arange(context.complete_t[0], context.complete_t[-1] + context.down_dt / 2., context.down_dt)
    context.down_induction_gate = np.interp(context.down_t, context.complete_t, context.induction_gate)
    if context.disp:
        print 'parallel_optimize_bidirectional_BTSP_CA1: process: %i loaded data for cell: %i, induction: %i' % \
              (os.getpid(), cell_id, induction)


def update_model_params(x, local_context):
    """

    :param x: array
    :param local_context: :class:'Context'
    """
    if local_context is None:
        local_context = context
    local_context.update(param_array_to_dict(x, local_context.param_names))


def update_submodule_params(x, local_context=None):
    """

    :param x: array
    :param local_context: :class:'Context'
    """
    if local_context is None:
        local_context = context
    for update_func in local_context.update_params_funcs:
        update_func(x, local_context)


def plot_data():
    """
     
    """
    fig, axes = plt.subplots(1)
    for group in context.position:
        for i, this_position in enumerate(context.position[group]):
            this_t = context.t[group][i]
            axes.plot(this_t / 1000., this_position, label=group+str(i))
    axes.set_xlabel('Time (s)')
    axes.set_ylabel('Position (cm)')
    axes.set_title('Interpolated position')
    axes.legend(loc='best', frameon=False, framealpha=0.5)
    fig.tight_layout()
    clean_axes(axes)

    fig, axes = plt.subplots(1)
    axes2 = axes.twinx()
    axes.plot(context.complete_t / 1000., context.complete_run_vel)
    axes2.plot(context.complete_t / 1000., context.complete_run_vel_gate, c='k')
    axes.set_xlabel('Time (s)')
    axes.set_ylabel('Running speed (cm/s)')
    clean_axes(axes)
    axes2.tick_params(direction='out')
    axes2.spines['top'].set_visible(False)
    axes2.spines['left'].set_visible(False)
    axes2.get_xaxis().tick_bottom()
    axes2.get_yaxis().tick_right()
    fig.tight_layout()

    fig, axes = plt.subplots(2, 2)
    axes[1][0].plot(context.binned_x, context.exp_ramp['after'])
    if 'before' in context.exp_ramp:
        axes[1][0].plot(context.binned_x, context.exp_ramp['before'])
        axes[1][0].plot(context.binned_x, context.exp_ramp_raw['before'])
    axes[1][0].plot(context.binned_x, context.exp_ramp_raw['after'])
    axes[1][0].set_xlabel('Position (cm)')
    axes[0][0].set_xlabel('Position (cm)')
    axes[1][0].set_ylabel('Ramp amplitude (mV)')
    axes[1][1].set_ylabel('Ramp amplitude (mV)')
    axes[1][1].set_xlabel('Time (s)')
    axes[0][1].set_xlabel('Time (s)')
    axes[0][0].set_ylabel('Induction current (nA)')
    axes[0][1].set_ylabel('Induction gate (a.u.)')
    for i, this_position in enumerate(context.position['induction']):
        this_t = context.t['induction'][i]
        this_current = context.current[i]
        this_induction_gate = np.zeros_like(this_current)
        indexes = np.where(this_current >= 0.5 * np.max(this_current))[0]
        this_induction_gate[indexes] = 1.
        start_index = indexes[0]
        this_induction_loc = context.induction_locs[i]
        this_induction_dur = context.induction_durs[i]
        axes[0][0].plot(this_position, this_current, label='Lap %i: Loc: %i cm, Dur: %i ms' %
                                                           (i, this_induction_loc, this_induction_dur))
        axes[0][1].plot(np.subtract(this_t, this_t[start_index]) / 1000., this_induction_gate)
    mean_induction_index = np.where(context.mean_position >= context.mean_induction_loc)[0][0]
    mean_induction_onset = context.mean_t[mean_induction_index]
    peak_val, ramp_width, peak_shift, ratio, start_loc, peak_loc, end_loc = \
        calculate_ramp_features(context.exp_ramp['after'], context.mean_induction_loc)
    start_index, peak_index, end_index = get_indexes_from_ramp_bounds_with_wrap(context.binned_x, start_loc, peak_loc,
                                                                                end_loc)
    axes[1][0].scatter(context.binned_x[[start_index, peak_index, end_index]],
                       context.exp_ramp['after'][[start_index, peak_index, end_index]])
    start_index, peak_index, end_index = get_indexes_from_ramp_bounds_with_wrap(context.mean_position, start_loc,
                                                                                peak_loc, end_loc)
    this_shifted_t = np.subtract(context.mean_t, mean_induction_onset) / 1000.
    axes[1][1].plot(this_shifted_t, context.exp_ramp_vs_t['after'])
    axes[1][1].scatter(this_shifted_t[[start_index, peak_index, end_index]],
                       context.exp_ramp_vs_t['after'][[start_index, peak_index, end_index]])
    if 'before' in context.exp_ramp_vs_t:
        axes[1][1].plot(this_shifted_t, context.exp_ramp_vs_t['before'])
    axes[0][0].legend(loc='best', frameon=False, framealpha=0.5)
    clean_axes(axes)
    fig.tight_layout()

    fig, axes = plt.subplots(1, 2)
    axes[0].plot(context.binned_x, context.SVD_ramp['after'])
    axes[1].plot(context.peak_locs, context.SVD_weights['after'])
    if 'before' in context.SVD_ramp:
        axes[0].plot(context.binned_x, context.SVD_ramp['before'])
        axes[1].plot(context.peak_locs, context.SVD_weights['before'])
    axes[0].plot(context.binned_x, context.exp_ramp['after'])
    axes[0].plot(context.binned_x, context.exp_ramp_raw['after'])
    if 'before' in context.exp_ramp:
        axes[0].plot(context.binned_x, context.exp_ramp['before'])
        axes[0].plot(context.binned_x, context.exp_ramp_raw['before'])

    axes[0].set_xlabel('Position (cm)')
    axes[1].set_xlabel('Position (cm)')
    axes[0].set_ylabel('Ramp amplitude (mV)')
    axes[1].set_ylabel('Candidate synaptic weights (a.u.)')
    clean_axes(axes)
    fig.tight_layout()

    plt.show()
    plt.close()


def get_indexes_from_ramp_bounds_with_wrap(x, start, peak, end, min):
    """

    :param x: array
    :param start: float
    :param peak: float
    :param end: float
    :param min: float
    :return: tuple of float: (start_index, peak_index, end_index, min_index)
    """
    peak_index = np.where(x >= peak)[0]
    if np.any(peak_index):
        peak_index = peak_index[0]
    else:
        peak_index = len(x) - 1
    min_index = np.where(x <= min)[0]
    if np.any(min_index):
        min_index = min_index[0]
    else:
        min_index = len(x) - 1
    if start < peak:
        start_index = np.where(x[:peak_index] <= start)[0][-1]
    else:
        start_index = peak_index + np.where(x[peak_index:] <= start)[0]
        if np.any(start_index):
            start_index = start_index[-1]
        else:
            start_index = len(x) - 1
    if end < peak:
        end_index = np.where(x > end)[0][0]
    else:
        end_index = peak_index + np.where(x[peak_index:] > end)[0]
        if np.any(end_index):
            end_index = end_index[0]
        else:
            end_index = len(x) - 1
    return start_index, peak_index, end_index, min_index


def calculate_ramp_features(ramp, induction_loc, offset=False, smooth=False):
    """

    :param ramp: array
    :param induction_loc: float
    :param offset: bool
    :param smooth: bool
    :return tuple of float
    """
    binned_x = context.binned_x
    track_length = context.track_length
    default_interp_x = context.default_interp_x
    extended_binned_x = np.concatenate([binned_x - track_length, binned_x, binned_x + track_length])
    if smooth:
        local_ramp = signal.savgol_filter(ramp, 21, 3, mode='wrap')
    else:
        local_ramp = np.array(ramp)
    extended_binned_ramp = np.concatenate([local_ramp] * 3)
    extended_interp_x = np.concatenate([default_interp_x - track_length, default_interp_x,
                                        default_interp_x + track_length])
    extended_ramp = np.interp(extended_interp_x, extended_binned_x, extended_binned_ramp)
    interp_ramp = extended_ramp[len(default_interp_x):2*len(default_interp_x)]
    baseline_indexes = np.where(interp_ramp <= np.percentile(interp_ramp, 10.))[0]
    baseline = np.mean(interp_ramp[baseline_indexes])
    if offset:
        interp_ramp -= baseline
        extended_ramp -= baseline
    peak_index = np.where(interp_ramp == np.max(interp_ramp))[0][0] + len(interp_ramp)
    peak_val = extended_ramp[peak_index]
    peak_x = extended_interp_x[peak_index]
    start_index = np.where(extended_ramp[:peak_index] <=
                           0.15*(peak_val - baseline) + baseline)[0][-1]
    end_index = peak_index + np.where(extended_ramp[peak_index:] <= 0.15*
                                                (peak_val - baseline) + baseline)[0][0]
    start_loc = float(start_index % len(default_interp_x)) / float(len(default_interp_x)) * track_length
    end_loc = float(end_index % len(default_interp_x)) / float(len(default_interp_x)) * track_length
    peak_loc = float(peak_index % len(default_interp_x)) / float(len(default_interp_x)) * track_length
    min_index = np.where(interp_ramp == np.min(interp_ramp))[0][0] + len(interp_ramp)
    min_val = extended_ramp[min_index]
    min_loc = float(min_index % len(default_interp_x)) / float(len(default_interp_x)) * track_length
    peak_shift = peak_x - induction_loc
    if peak_shift > track_length / 2.:
        peak_shift = -(track_length - peak_shift)
    elif peak_shift < -track_length / 2.:
        peak_shift += track_length
    ramp_width = extended_interp_x[end_index] - extended_interp_x[start_index]
    before_width = induction_loc - start_loc
    if induction_loc < start_loc:
        before_width += track_length
    after_width = end_loc - induction_loc
    if induction_loc > end_loc:
        after_width += track_length
    ratio = before_width / after_width
    return peak_val, ramp_width, peak_shift, ratio, start_loc, peak_loc, end_loc, min_val, min_loc 


def wrap_around_and_compress(waveform, interp_x):
    """

    :param waveform: array of len(3 * interp_x)
    :param interp_x: array
    :return: array of len(interp_x)
    """
    before = np.array(waveform[:len(interp_x)])
    after = np.array(waveform[2 * len(interp_x):])
    within = np.array(waveform[len(interp_x):2 * len(interp_x)])
    waveform = within[:len(interp_x)] + before[:len(interp_x)] + after[:len(interp_x)]
    return waveform


def compute_EPSP_matrix(rate_maps, local_x):
    """

    :param rate_maps: list of array
    :param local_x: array
    :return: array
    """
    filter_t = np.arange(0., 200., context.dt)
    epsp_filter = np.exp(-filter_t / 20.) - np.exp(-filter_t / .5)
    epsp_filter /= np.sum(epsp_filter)
    EPSP_maps = []

    for rate_map in rate_maps:
        this_EPSP_map = np.interp(context.default_interp_x, local_x, rate_map) * context.ramp_scaling_factor
        this_EPSP_map = np.concatenate([this_EPSP_map] * 3)
        this_EPSP_map = np.convolve(this_EPSP_map, epsp_filter)[:3 * len(context.default_interp_x)]
        EPSP_maps.append(this_EPSP_map[len(context.default_interp_x):2 * len(context.default_interp_x)])
    return np.array(EPSP_maps)


def subtract_baseline(waveform, baseline=None):
    """

    :param waveform: array
    :param baseline: float
    :return: array
    """
    new_waveform = np.array(waveform)
    if baseline is None:
        baseline = np.mean(new_waveform[np.where(new_waveform <= np.percentile(new_waveform, 10.))[0]])
    new_waveform -= baseline
    return new_waveform, baseline


def get_complete_rate_maps():
    """

    :return: list of array
    """
    complete_rate_maps = []
    for j in xrange(len(context.input_rate_maps)):
        this_complete_rate_map = np.array([])
        for group in ['pre', 'induction', 'post']:
            for i, this_position in enumerate(context.position[group]):
                this_rate_map = np.interp(this_position, context.generic_x, context.input_rate_maps[j])
                this_complete_rate_map = np.append(this_complete_rate_map, this_rate_map)
        this_complete_rate_map = np.multiply(this_complete_rate_map, context.complete_run_vel_gate)
        if len(this_complete_rate_map) != len(context.complete_run_vel_gate):
            print 'get_complete_rate_maps: mismatched array length'
        complete_rate_maps.append(this_complete_rate_map)
    return complete_rate_maps


def get_signal_filters(local_signal_rise, local_signal_decay, global_signal_rise, global_signal_decay, dt=None, 
                       plot=False):
    """
    :param local_signal_rise: float
    :param local_signal_decay: float
    :param global_signal_rise: float
    :param global_signal_decay: float
    :param dt: float
    :param plot: bool
    :return: array, array
    """
    max_time_scale = max(local_signal_rise + local_signal_decay, global_signal_rise + global_signal_decay)
    if dt is None:
        dt = context.dt
    filter_t = np.arange(0., 6.*max_time_scale, dt)
    local_filter = np.exp(-filter_t/local_signal_decay) - np.exp(-filter_t/local_signal_rise)
    peak_index = np.where(local_filter == np.max(local_filter))[0][0]
    decay_indexes = np.where(local_filter[peak_index:] < 0.005*np.max(local_filter))[0]
    if np.any(decay_indexes):
        local_filter = local_filter[:peak_index+decay_indexes[0]]
    local_filter /= np.sum(local_filter)
    local_filter_t = filter_t[:len(local_filter)]
    global_filter = np.exp(-filter_t / global_signal_decay) - np.exp(-filter_t / global_signal_rise)
    peak_index = np.where(global_filter == np.max(global_filter))[0][0]
    decay_indexes = np.where(global_filter[peak_index:] < 0.005 * np.max(global_filter))[0]
    if np.any(decay_indexes):
        global_filter = global_filter[:peak_index + decay_indexes[0]]
    global_filter /= np.sum(global_filter)
    global_filter_t = filter_t[:len(global_filter)]
    if plot:
        fig, axes = plt.subplots(1)
        axes.plot(local_filter_t/1000., local_filter / np.max(local_filter), color='k', 
                  label='Local signal filter')
        axes.plot(global_filter_t / 1000., global_filter / np.max(global_filter), color='r', 
                  label='Global signal filter')
        axes.set_xlabel('Time (s)')
        axes.set_ylabel('Normalized filter amplitude')
        axes.set_title('Plasticity signal filters')
        axes.legend(loc='best', frameon=False, framealpha=0.5)
        axes.set_xlim(-0.5, max(5000., local_filter_t[-1], global_filter_t[-1]) / 1000.)
        clean_axes(axes)
        fig.tight_layout()
        plt.show()
        plt.close()
    return local_filter_t, local_filter, global_filter_t, global_filter


def get_local_signal(rate_map, local_filter, dt):
    """

    :param rate_map: array
    :param local_filter: array
    :param dt: float
    :return: array
    """
    return np.convolve(0.001 * dt * rate_map, local_filter)[:len(rate_map)]


def get_global_signal(induction_gate, global_filter):
    """
    
    :param induction_gate: array 
    :param global_filter: array
    :return: array
    """
    return np.convolve(induction_gate, global_filter)[:len(induction_gate)]


def get_model_ramp_features(indiv, c=None, client_range=None, export=False):
    """
    Distribute simulations across available engines for computing model ramp features.
    :param indiv: dict {'pop_id': pop_id, 'x': x arr, 'features': features dict}
    :param c: :class:'ipyparallel.Client'
    :param client_range: list of int
    :param export: bool
    :return: dict
    """
    if c is not None:
        if client_range is None:
            client_range = range(len(c))
        dv = c[client_range]
        map_func = dv.map_async
    else:
        map_func = map
    x = indiv['x']
    cell_id_list = [data_key[0] for data_key in context.data_keys]
    induction_list = [data_key[1] for data_key in context.data_keys]
    result = map_func(compute_model_ramp_features, [x] * len(context.data_keys), cell_id_list, induction_list,
                      [export] * len(context.data_keys))
    return {'pop_id': indiv['pop_id'], 'client_range': client_range, 'async_result': result,
            'filter_features': filter_model_ramp_features}


def compute_model_ramp_features(x, cell_id=None, induction=None, export=False, plot=False, full_output=False):
    """

    :param x: array
    :param cell_id: int
    :param induction: int
    :param export: bool
    :param plot: bool
    :param full_output: bool
    :return: dict
    """
    import_data(cell_id, induction)
    update_submodule_params(x, context)
    print 'Process: %i: computing model_ramp_features for cell_id: %i, induction: %i with x: %s' % \
          (os.getpid(), context.cell_id, context.induction, ', '.join('%.3E' % i for i in x))
    start_time = time.time()
    down_dt = context.down_dt
    local_filter_t, local_filter, global_filter_t, global_filter = \
        get_signal_filters(context.local_signal_rise, context.local_signal_decay, context.global_signal_rise,
                           context.global_signal_decay, down_dt, plot)
    global_signal = get_global_signal(context.down_induction_gate, global_filter)
    weights = []
    # peak_local_signal_amp = []
    peak_weight = context.peak_delta_weight + 1.
    initial_weights = np.minimum(context.SVD_weights['before'] + 1., peak_weight) / peak_weight
    for i in xrange(len(context.peak_locs)):
        # normalize total number of receptors
        initial_weight = initial_weights[i]
        available = 1. - initial_weight
        context.sm.update_states({'M': available, 'C': initial_weight})
        rate_map = np.interp(context.down_t, context.complete_t, context.complete_rate_maps[i])
        local_signal = get_local_signal(rate_map, local_filter, down_dt)
        context.sm.update_rates(
            {'M': {'C': context.rMC0 * global_signal * local_signal},
             'C': {'M': context.rCM0 * global_signal * local_signal}})
        context.sm.reset()
        context.sm.run()
        if plot and i == 100:
            fig, axes = plt.subplots(1)
            axes.plot(context.down_t / 1000., local_signal, c='k', label='Local signal')
            axes.plot(context.down_t / 1000., global_signal, c='r', label='Global signal')
            axes.set_xlabel('Time (s)')
            axes.set_ylabel('Plasticity signal amplitude (a.u.)')
            axes.legend(loc='best', frameon=False, framealpha=0.5)
            clean_axes(axes)
            fig.tight_layout()
            context.sm.plot()
        # peak_local_signal_amp.append(np.max(local_signal))
        weights.append(context.sm.states['C'] * peak_weight)
    initial_weights = np.multiply(initial_weights, peak_weight)
    weights = np.array(weights)
    delta_weights = np.subtract(weights, initial_weights)
    ramp_amp, ramp_width, peak_shift, ratio, start_loc, peak_loc, end_loc, min_val, min_loc = {}, {}, {}, {}, {}, {}, \
                                                                                              {}, {}, {}
    target_ramp = context.exp_ramp['after']
    ramp_amp['target'], ramp_width['target'], peak_shift['target'], ratio['target'], start_loc['target'], \
        peak_loc['target'], end_loc['target'], min_val['target'], min_loc['target'] = \
        calculate_ramp_features(target_ramp, context.mean_induction_loc)
    model_ramp = get_model_ramp(weights - 1.)
    ramp_amp['model'], ramp_width['model'], peak_shift['model'], ratio['model'], start_loc['model'], \
        peak_loc['model'], end_loc['model'], min_val['model'], min_loc['model'] = \
        calculate_ramp_features(model_ramp, context.mean_induction_loc)

    result = {'delta_amp': ramp_amp['model'] - ramp_amp['target'],
              'delta_width': ramp_width['model'] - ramp_width['target'],
              'delta_peak_shift': peak_shift['model'] - peak_shift['target'],
              'delta_asymmetry': ratio['model'] - ratio['target'],
              'delta_min_val': min_val['model'] - min_val['target']}
    abs_delta_min_loc = abs(min_loc['model'] - min_loc['target'])
    if min_loc['model'] <= min_loc['target']:
        if abs_delta_min_loc > context.track_length / 2.:
            delta_min_loc = context.track_length - abs_delta_min_loc
        else:
            delta_min_loc = -abs_delta_min_loc
    else:
        if abs_delta_min_loc > context.track_length / 2.:
            delta_min_loc = -(context.track_length - abs_delta_min_loc)
        else:
            delta_min_loc = abs_delta_min_loc
    result['delta_min_loc'] = delta_min_loc
    if plot:
        fig, axes = plt.subplots(1, 2)
        axes[1].plot(context.peak_locs, delta_weights)
        axes[0].plot(context.binned_x, target_ramp, label='Experiment')
        axes[0].plot(context.binned_x, model_ramp, label='Model')
        axes[1].set_ylabel('Change in synaptic weight (a.u.)')
        axes[1].set_xlabel('Location (cm)')
        axes[0].set_ylabel('Ramp amplitude (mV)')
        axes[0].set_xlabel('Location (cm)')
        axes[0].legend(loc='best', frameon=False, framealpha=0.5)
        axes[0].set_ylim([min(-1., np.min(model_ramp) - 1., np.min(target_ramp) - 1.),
                          max(10., np.max(model_ramp) + 1., np.max(target_ramp) + 1.)])
        axes[1].set_ylim([-peak_weight, peak_weight])
        clean_axes(axes)
        fig.suptitle('Cell_id: %i, Induction: %i' % (context.cell_id, context.induction))
        fig.tight_layout()
        plt.show()
        plt.close()
    if full_output:
        result['weights'] = weights
        result['initial_weights'] = initial_weights
        result['model_ramp'] = np.array(model_ramp)
    if export:
        with h5py.File(context.processed_export_file_path, 'a') as f:
            description = 'model_ramp_context'
            if description not in f:
                f.create_group(description)
                group = f[description]
                group.create_dataset('peak_locs', compression='gzip', compression_opts=9, data=context.peak_locs)
                group.create_dataset('binned_x', compression='gzip', compression_opts=9, data=context.binned_x)
                group.attrs['peak_weight'] = peak_weight
            description = 'model_ramp_features'
            if description not in f:
                f.create_group(description)
            cell_key = str(cell_id)
            induction_key = str(induction)
            if cell_key not in f[description]:
                f[description].create_group(cell_key)
            if induction_key not in f[description][cell_key]:
                f[description][cell_key].create_group(induction_key)
            group = f[description][cell_key][induction_key]
            group.create_dataset('target_ramp', compression='gzip', compression_opts=9, data=target_ramp)
            group.create_dataset('model_ramp', compression='gzip', compression_opts=9, data=model_ramp)
            group.create_dataset('weights', compression='gzip', compression_opts=9, data=weights)
            group.create_dataset('initial_weights', compression='gzip', compression_opts=9, data=initial_weights)
    model_ramp /= ramp_amp['model']
    model_ramp *= ramp_amp['target']
    residuals = np.sum(np.abs(np.subtract(target_ramp, model_ramp)))
    result['residuals'] = residuals
    print 'Process: %i: computing model_ramp_features for cell_id: %i, induction: %i took %.1f s' % \
          (os.getpid(), context.cell_id, context.induction, time.time() - start_time)
    return {cell_id: {induction: result}}


def filter_model_ramp_features(computed_result_list, current_features, target_val, target_range, export=False):
    """

    :param computed_result_list: list of dict (each dict contains results from a single simulation)
    :param current_features: dict
    :param target_val: dict of float
    :param target_range: dict of float
    :param export: bool
    :return: dict
    """
    residuals, delta_amp, delta_width, delta_peak_shift, delta_asymmetry, delta_min_loc, delta_min_val, \
        features = {}, {}, {}, {}, {}, {}, {}, {}
    groups = ['spont', 'exp1', 'exp2']
    features_names = ['residuals', 'delta_amp', 'delta_width', 'delta_peak_shift', 'delta_asymmetry',
                      'delta_min_loc', 'delta_min_val']
    for feature in residuals, delta_amp, delta_width, delta_peak_shift, delta_asymmetry, delta_min_loc,\
            delta_min_val:
        for group in groups:
            feature[group] = []
    for this_result_dict in computed_result_list:
        for cell_id in this_result_dict:
            for induction in this_result_dict[cell_id]:
                if cell_id in context.spont_cell_id_list:
                    group = 'spont'
                else:
                    group = 'exp'+str(induction)
                for feature, feature_name in \
                        zip([residuals, delta_amp, delta_width, delta_peak_shift, delta_asymmetry, delta_min_loc,
                             delta_min_val], features_names):
                    feature[group].append(this_result_dict[cell_id][induction][feature_name])
    for feature, feature_name in \
            zip([residuals, delta_amp, delta_width, delta_peak_shift, delta_asymmetry, delta_min_loc,
                 delta_min_val], features_names):
        for group in groups:
            if len(feature[group]) > 0:
                features[group + '_' + feature_name] = np.mean(feature[group])
            else:
                features[group + '_' + feature_name] = 0.
    return features


def get_objectives(features, target_val, target_range):
    """

    :param features: dict
    :param target_val: dict of float
    :param target_range: dict of float
    :return: tuple of dict
    """
    objectives = {}
    for objective_name in target_val:
        objectives[objective_name] = ((target_val[objective_name] - features[objective_name]) /
                                      target_range[objective_name]) ** 2.
    return features, objectives


def get_model_ramp(delta_weights, plot=False):
    """

    :param delta_weights: array
    :param plot: bool
    :return: array
    """
    model_ramp = delta_weights.dot(context.input_matrix)
    model_ramp = np.interp(context.binned_x, context.default_interp_x, model_ramp)
    if plot:
        fig, axes = plt.subplots(1)
        axes.plot(context.binned_x, context.exp_ramp['after'], label='Experiment')
        axes.plot(context.binned_x, model_ramp, label='Model')
        axes.set_xlabel('Location (cm)')
        axes.set_ylabel('Ramp amplitude (mV)')
        axes.set_title('Cell_id: %i, Induction: %i' % (context.cell_id, context.induction))
        clean_axes(axes)
        fig.tight_layout()
        plt.show()
        plt.close()
    return model_ramp


def get_model_ramp_error(x):
    """

    :param x:
    :param plot: bool
    :param full_output: bool
    :return: float
    """
    indiv = {'pop_id': 0, 'x': x}
    computed_result = get_model_ramp_features(indiv)['async_result']
    features = filter_model_ramp_features(computed_result, {}, context.target_val, context.target_range)
    features, objectives = get_objectives(features, context.target_val, context.target_range)
    Err = np.sum(objectives.values())
    return Err


if __name__ == '__main__':
    config_interactive()
    # x = context.x0_array
    # x = [17.26330989, 58.89765021, 57.32413683, 765.69679806, 10.14063316, 500.60616055, 3.23101249, -5.14206064,
    #     2.634794]
    #x = [17.26330989, 100., 57.32413683, 765.69679806, 10.14063316, 500.60616055, 1.,
    #          2.634794]
    x = [37.09395918, 105.52255606, 62.95478383, 524.0054589,
     97.33240168, 158.68052365, 2.47129701]

    results = []
    for cell_id, induction in context.data_keys:
        results.append(compute_model_ramp_features(x, cell_id, induction, plot=True, full_output=True))
    """
    for result in results:
        print result.items()
    
    Err = get_model_ramp_error(x)
    
    result = optimize.minimize(get_model_ramp_error, x, method='L-BFGS-B', bounds=context.bounds, 
                               options={'disp': True, 'maxfun': 200})
    x = result.x
    """
    context.update(locals())