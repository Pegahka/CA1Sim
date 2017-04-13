__author__ = 'Grace Ng'
import parallel_optimize_spike_stability_engine
import sys
import os
from ipyparallel import Client
from IPython.display import clear_output
from plot_results import *
import scipy.optimize as optimize
import mkl

"""
Aims for spike initiation at initial segment by increasing nax density and decreasing activation V1/2 relative to soma,
axon_hill, and axon compartments. Extend linear kap gradient into basals and obliques, aim for 60% spike attenuation
at bifurcation of trunk and tuft.

Optimizes gbar_nax/nas/sh/sha, gkabar_kap/d, gkdrbar for target na spike threshold, AHP amp, and vm stability

Parallel version dynamically submits jobs to available cores.

Assumes a controller is already running in another process with:
ipcluster start -n num_cores
"""

mkl.set_num_threads(1)


def na_ka_stability_error(x, plot=0):
    """

    :param x: array [soma.gkabar, soma.gkdrbar, axon.gkabar_kap factor, axon.gbar_nax factor, soma.sh_nas/x,
                    axon.gkdrbar factor, dend.gkabar factor]
    :param plot: int
    :return: float
    """
    if not check_bounds.within_bounds(x, 'na_ka_stability'):
        print 'Process %i: Aborting - Parameters outside optimization bounds.' % (os.getpid())
        hist.x_values.append(x)
        Err = 1e9
        hist.error_values.append(Err)
        return Err
    start_time = time.time()
    dv['x'] = x
    hist.x_values.append(x)
    formatted_x = '[' + ', '.join(['%.3E' % xi for xi in x]) + ']'
    print 'Process %i using current x: %s: %s' % (os.getpid(), str(xlabels['na_ka_stability']), formatted_x)
    result = c[0].apply(parallel_optimize_spike_stability_engine.compute_spike_shape_features)
    last = ''
    while not result.ready():
        time.sleep(1.)
        clear_output()
        stdout = result.stdout
        if stdout:
            line = stdout.splitlines()[-1]
            if line != last:
                print line
                last = line
        sys.stdout.flush()
    result = result.get()
    if result is None:
        print 'Cell is spontaneously firing, or parameters are out of bounds.'
        Err = 1e9
        hist.error_values.append(Err)
        return Err
    final_result = result
    result = v.map_async(parallel_optimize_spike_stability_engine.compute_spike_stability_features,
                         [final_result['amp'] + amp for amp in [0.25, 0.5, 0.75]])
    last = []
    while not result.ready():
        time.sleep(1.)
        clear_output()
        for i, stdout in enumerate([stdout for stdout in result.stdout if stdout][-3:]):
            line = stdout.splitlines()[-1]
            if line not in last:
                print line
                last.append(line)
        if len(last) > len(x):
            last = last[-len(x):]
        sys.stdout.flush()
    result = result.get()
    for this_dict in result:
        if 'stability' not in final_result:
            final_result['stability'] = this_dict['stability']
        else:
            final_result['stability'] += this_dict['stability']
        if 'slow_depo' not in final_result:
            final_result['slow_depo'] = this_dict['v_min_late'] - final_result['v_th']
        else:
            final_result['slow_depo'] += this_dict['v_min_late'] - final_result['v_th']

    Err = 0.
    for target in final_result:
        if target not in hist.features:
            hist.features[target] = []
        hist.features[target].append(final_result[target])
    for target in ['v_th', 'ADP', 'AHP', 'stability', 'slow_depo', 'dend_amp']:
        # don't penalize AHP or slow_depo less than target
        if not ((target == 'AHP' and final_result[target] < target_val['na_ka'][target]) or
                (target == 'slow_depo' and final_result[target] < target_val['na_ka'][target])):
            Err += ((target_val['na_ka'][target] - final_result[target])/target_range['na_ka'][target])**2.
            if target not in hist.features:
                hist.features[target] = []
            hist.features[target].append(final_result[target])

    print 'Simulation took %i s' % (time.time()-start_time)
    print 'Process %i: [soma.gkabar, soma.gkdrbar, axon.gkabar_kap factor, axon.gbar_nax factor, soma.sh_nax/s, ' \
          'axon.gkdrbar factor, dend.gkabar factor]: ' \
          '[%.4f, %.4f, %.3f, %.3f, %.3f, %.3f, %.3f], amp: %.3f, v_rest: %.1f, threshold: %.1f, ADP: %.1f, ' \
          'AHP: %.1f, stability: %.2f, slow_depo: %.2f, dend_amp: %.2f' % (os.getpid(), x[0], x[1], x[2], x[3], x[4],
                                                                           x[5], x[6], final_result['amp'],
                                                                           final_result['v_rest'],
                                                                           final_result['v_th'], final_result['ADP'],
                                                                           final_result['AHP'],
                                                                           final_result['stability'],
                                                                           final_result['slow_depo'],
                                                                           final_result['dend_amp'])
    print 'Process %i: Error: %.4E' % (os.getpid(), Err)
    hist.error_values.append(Err)
    sys.stdout.flush()
    return Err


def plot_best(x=None, discard=True):
    """
    Run simulations on the engines with the last best set of parameters, have the engines export their results to .hdf5,
    and then read in and plot the results.
    :param x: array
    """
    if x is None:
        if hist.x_values:
            na_ka_stability_error(hist.report_best())
        else:
            raise Exception('Please specify input parameters (history might be empty).')
    else:
        na_ka_stability_error(x)
    dv.execute('export_sim_results()')
    rec_file_list = [filename for filename in dv['rec_filename'] if os.path.isfile(data_dir + filename + '.hdf5')]
    for i, rec_filename in enumerate(rec_file_list):
        with h5py.File(data_dir+rec_filename+'.hdf5', 'r') as f:
            plt.figure(i)
            for trial in f.itervalues():
                amplitude = trial.attrs['amp']
                fig, axes = plt.subplots(1)
                for rec in trial['rec'].itervalues():
                    axes.plot(trial['time'], rec, label=rec.attrs['description'])
                axes.legend(loc='best', frameon=False, framealpha=0.5)
                axes.set_xlabel('Time (ms)')
                axes.set_ylabel('Vm (mV)')
                axes.set_title('Optimize Vm: I_inj amplitude %.2f' % amplitude)
                fig.tight_layout()
                clean_axes(axes)
    plt.show()
    plt.close()
    if discard:
        for rec_filename in rec_file_list:
            os.remove(data_dir + rec_filename + '.hdf5')


v_init = -77.
soma_ek = -77.

# the target values and acceptable ranges
target_val = {}
target_range = {}
target_val['v_rest'] = {'soma': v_init, 'tuft_offset': 0.}
target_range['v_rest'] = {'soma': 0.25, 'tuft_offset': 0.1}
target_val['na_ka'] = {'v_rest': v_init, 'v_th': -48., 'soma_peak': 40., 'ADP': 0., 'AHP': 4.,
                       'stability': 0., 'ais_delay': 0., 'slow_depo': 20., 'dend_amp': 0.3}
target_range['na_ka'] = {'v_rest': 0.25, 'v_th': .2, 'soma_peak': 2., 'ADP': 0.01, 'AHP': .2,
                         'stability': 1., 'ais_delay': 0.001, 'slow_depo': 0.5, 'dend_amp': 0.005}

x0 = {}
xlabels = {}
xmin = {}
xmax = {}

if len(sys.argv) > 1:
    spines = bool(int(sys.argv[1]))
else:
    spines = False
if len(sys.argv) > 2:
    mech_filename = str(sys.argv[2])
else:
    mech_filename = '030217 GC optimizing excitability'
if len(sys.argv) > 3:
    cluster_id = sys.argv[3]
    c = Client(cluster_id=cluster_id)
else:
    c = Client()

check_bounds = CheckBounds(xmin, xmax)
xlabels['na_ka_stability'] = ['soma.gkabar', 'soma.gkdrbar', 'axon.gkabar_kap factor', 'axon.gbar_nax factor',
                              'soma.sh_nas/x', 'axon.gkdrbar factor', 'dend.gkabar factor']
hist = optimize_history()
hist.xlabels = xlabels['na_ka_stability']


# [soma.gkabar, soma.gkdrbar, axon.gkabar_kap factor, axon.gbar_nax factor, soma.sh_nas/x, axon.gkdrbar factor,
#  dend.gkabar factor]
# x0['na_ka_stability'] = [0.0483, 0.0100, 4.56, 4.90, 4.63]  # Error: 2.7284E+03
# x0['na_ka_stability'] = [0.02948262,  0.01003593,  4.66184288,  4.48235059,  4.91410208]  # Error: 2.644E+03
# x0['na_ka_stability'] = [0.0365, 0.0118, 4.91, 4.72, 4.90, 1., 1.]  # Error: 2.2990E+03
x0['na_ka_stability'] = [0.0308, 0.0220, 4.667, 4.808, 4.032, 1.297, 1.023]  # Error: 1.5170E+03
xmin['na_ka_stability'] = [0.01, 0.01, 1., 2., 0.1, 1., 1.]
xmax['na_ka_stability'] = [0.075, 0.05, 5., 5., 6., 2., 5.]

max_niter = 2100  # max number of iterations to run
niter_success = 400  # max number of interations without significant progress before aborting optimization

take_step = Normalized_Step(x0['na_ka_stability'], xmin['na_ka_stability'], xmax['na_ka_stability'])
minimizer_kwargs = dict(method=null_minimizer)

dv = c[:]
dv.block = True
global_start_time = time.time()


dv.execute('run parallel_optimize_spike_stability_engine %i \"%s\"' % (int(spines), mech_filename))
# time.sleep(60)
v = c.load_balanced_view()

"""
result = optimize.basinhopping(na_ka_stability_error, x0['na_ka_stability'], niter=max_niter,
                               niter_success=niter_success, disp=True, interval=40,
                               minimizer_kwargs=minimizer_kwargs, take_step=take_step)
print result

best_x = hist.report_best()
hist.export_to_pkl(history_filename)
dv['x'] = best_x
# dv['x'] = x0['na_ka_stability']
c[0].apply(parallel_optimize_spike_stability_engine.update_mech_dict)
"""
plot_best(x0['na_ka_stability'])