__author__ = 'milsteina'
from specify_cells import *
from plot_results import *
import random
import sys
"""

"""
morph_filename = 'EB2-late-bifurcation.swc'
mech_filename = '020516 altered km2 rinp - ampa nmda_kin5'


if len(sys.argv) > 1:
    synapses_seed = int(sys.argv[1])
else:
    synapses_seed = 1
if len(sys.argv) > 2:
    num_exc_syns = int(sys.argv[2])
else:
    num_exc_syns = 3000
if len(sys.argv) > 3:
    num_inh_syns = int(sys.argv[3])
else:
    num_inh_syns = 500
# whether to modulate the peak rate of all inhibitory inputs (0 = no, 1 = out of field at track start, 2 = in field)
# input_field_width)
if len(sys.argv) > 4:
    mod_inh = int(sys.argv[4])
else:
    mod_inh = 0
# the number of in-field excitatory inputs will be multiplied by this factor, with their density following a gaussian distribution
if len(sys.argv) > 5:
    mod_density = float(sys.argv[5])
else:
    mod_density = 1.25
# allows parallel computation of multiple trials for the same spines with the same peak_locs, but with different
# input spike trains and stochastic synapses for each trial
if len(sys.argv) > 6:
    trial_seed = int(sys.argv[6])
else:
    trial_seed = 0

rec_filename = 'output'+datetime.datetime.today().strftime('%m%d%Y%H%M')+'-pid'+str(os.getpid())+'-seed'+\
               str(synapses_seed)+'-e'+str(num_exc_syns)+'-i'+str(num_inh_syns)+'-mod_inh'+str(mod_inh)+\
               '-density_'+str(mod_density)+'_'+str(trial_seed)


def run_trial(simiter):
    """

    :param simiter: int
    """
    local_random.seed(simiter)
    global_phase_offset = local_random.uniform(-np.pi, np.pi)
    with h5py.File(data_dir+rec_filename+'-working.hdf5', 'a') as f:
        f.create_group(str(simiter))
        f[str(simiter)].create_group('train')
        f[str(simiter)].create_group('inh_train')
        f[str(simiter)].attrs['phase_offset'] = global_phase_offset / 2. / np.pi * global_theta_cycle_duration
    if mod_inh > 0:
        if mod_inh == 1:
            mod_inh_start = int(track_equilibrate / dt)
        elif mod_inh == 2:
            mod_inh_start = int((track_equilibrate + modulated_field_center - 0.3 * input_field_duration) / dt)
        sim.parameters['mod_inh_start'] = stim_t[mod_inh_start]
        mod_inh_stop = mod_inh_start + int(inhibitory_manipulation_duration * input_field_duration / dt)
        sim.parameters['mod_inh_stop'] = stim_t[mod_inh_stop]
    index = 0
    for group in stim_exc_syns:
        excitatory_theta_amp = excitatory_theta_modulation_depth[group] / 2.
        excitatory_theta_offset = 1. - excitatory_theta_amp
        for i, syn in enumerate(stim_exc_syns[group]):
            # the stochastic sequence used for each synapse is unique for each trial,
            # up to 1000 input spikes per spine
            if excitatory_stochastic:
                syn.randObj.seq(rand_exc_seq_locs[group][i]+int(simiter*1e3))
            gauss_force = excitatory_peak_rate * np.exp(-((stim_t - peak_locs[group][i]) / gauss_sigma)**2.)
            if group == 'ECIII':
                theta_force = excitatory_theta_offset + excitatory_theta_amp * np.cos(2. * np.pi /
                                        global_theta_cycle_duration * stim_t - global_phase_offset -
                                        excitatory_theta_phase_offset['ECIII'])
            else:
                unit_phase_offset = peak_locs[group][i] * theta_compression_factor
                theta_force = excitatory_theta_offset + excitatory_theta_amp * np.cos(2. * np.pi /
                                        unit_theta_cycle_duration * (stim_t - unit_phase_offset) -
                                        global_phase_offset - excitatory_theta_phase_offset['CA3'])
            stim_force = np.multiply(gauss_force, theta_force)
            train = get_inhom_poisson_spike_times(stim_force, stim_t, dt=stim_dt, generator=local_random)
            syn.source.play(h.Vector(np.add(train, equilibrate + track_equilibrate)))
            with h5py.File(data_dir+rec_filename+'-working.hdf5', 'a') as f:
                f[str(simiter)]['train'].create_dataset(str(index), compression='gzip', compression_opts=9, data=train)
                f[str(simiter)]['train'][str(index)].attrs['group'] = group
                f[str(simiter)]['train'][str(index)].attrs['index'] = syn.node.index
                f[str(simiter)]['train'][str(index)].attrs['type'] = syn.node.parent.parent.type
                f[str(simiter)]['train'][str(index)].attrs['peak_loc'] = peak_locs[group][i]
            index += 1
    index = 0
    for group in stim_inh_syns:
        inhibitory_theta_amp = inhibitory_peak_rate[group] * inhibitory_theta_modulation_depth[group] / 2.
        inhibitory_theta_offset = inhibitory_peak_rate[group] - inhibitory_theta_amp
        inhibitory_phase_offset = inhibitory_theta_phase_offset[group]
        for syn in stim_inh_syns[group]:
            inhibitory_theta_force = inhibitory_theta_offset + inhibitory_theta_amp * np.cos(2. * np.pi /
                                                global_theta_cycle_duration * stim_t - global_phase_offset -
                                                inhibitory_phase_offset)
            if mod_inh > 0 and group in inhibitory_manipulation_fraction and syn in manipulated_inh_syns[group]:
                inhibitory_theta_force[mod_inh_start:mod_inh_stop] = 0.
            train = get_inhom_poisson_spike_times(inhibitory_theta_force, stim_t, dt=stim_dt,
                                                  generator=local_random)
            syn.source.play(h.Vector(np.add(train, equilibrate + track_equilibrate)))
            with h5py.File(data_dir+rec_filename+'-working.hdf5', 'a') as f:
                f[str(simiter)]['inh_train'].create_dataset(str(index), compression='gzip', compression_opts=9,
                                                            data=train)
                f[str(simiter)]['inh_train'][str(index)].attrs['group'] = group
                f[str(simiter)]['inh_train'][str(index)].attrs['index'] = syn.node.index
                f[str(simiter)]['inh_train'][str(index)].attrs['loc'] = syn.loc
                f[str(simiter)]['inh_train'][str(index)].attrs['type'] = syn.node.type
            index += 1
    sim.run(v_init)
    with h5py.File(data_dir+rec_filename+'-working.hdf5', 'a') as f:
        sim.export_to_file(f, simiter)
        if excitatory_stochastic:
            f[str(simiter)].create_group('successes')
            index = 0
            for group in stim_exc_syns:
                for syn in stim_exc_syns[group]:
                    f[str(simiter)]['successes'].create_dataset(str(index), compression='gzip', compression_opts=9,
                                data=np.subtract(syn.netcon('AMPA_KIN').get_recordvec().to_python(),
                                                 equilibrate + track_equilibrate))
                    index += 1
        # save the spike output of the cell, removing the equilibration offset
        f[str(simiter)].create_dataset('output', compression='gzip', compression_opts=9,
                                    data=np.subtract(cell.spike_detector.get_recordvec().to_python(),
                                                     equilibrate + track_equilibrate))


NMDA_type = 'NMDA_KIN5'

equilibrate = 250.  # time to steady-state
global_theta_cycle_duration = 150.  # (ms)
input_field_width = 20  # (theta cycles per 6 standard deviations)
excitatory_phase_extent = 450.  # (degrees)
# Geissler...Buzsaki, PNAS 2010
unit_theta_cycle_duration = global_theta_cycle_duration * input_field_width / (input_field_width +
                                                                               (excitatory_phase_extent / 360.))
input_field_duration = input_field_width * global_theta_cycle_duration
track_length = 2.5  # field widths
track_duration = track_length * input_field_duration
track_equilibrate = 2. * global_theta_cycle_duration
duration = equilibrate + track_equilibrate + track_duration  # input_field_duration
excitatory_peak_rate = 40.
excitatory_theta_modulation_depth = {'CA3': 0.75, 'ECIII': 0.7}
theta_compression_factor = 1. - unit_theta_cycle_duration / global_theta_cycle_duration
excitatory_theta_phase_offset = {}
excitatory_theta_phase_offset['CA3'] = 165. / 360. * 2. * np.pi  # radians
excitatory_theta_phase_offset['ECIII'] = 0. / 360. * 2. * np.pi  # radians
excitatory_stochastic = 1
inhibitory_manipulation_fraction = {'perisomatic': 0.35, 'axo-axonic': 0.35, 'apical dendritic': 0.35,
                                    'tuft feedback': 0.35}
inhibitory_manipulation_duration = 0.6  # Ratio of input_field_duration
inhibitory_peak_rate = {'perisomatic': 40., 'axo-axonic': 40., 'apical dendritic': 40., 'distal apical dendritic': 40.,
                        'tuft feedforward': 40., 'tuft feedback': 40.}
inhibitory_theta_modulation_depth = {'perisomatic': 0.5, 'axo-axonic': 0.5, 'apical dendritic': 0.5,
                                     'distal apical dendritic': 0.5, 'tuft feedforward': 0.5, 'tuft feedback': 0.5}
inhibitory_theta_phase_offset = {}
inhibitory_theta_phase_offset['perisomatic'] = 145. / 360. * 2. * np.pi  # Like PV+ Basket
inhibitory_theta_phase_offset['axo-axonic'] = 70. / 360. * 2. * np.pi  # Vargas et al., ELife, 2014
inhibitory_theta_phase_offset['apical dendritic'] = 210. / 360. * 2. * np.pi  # Like PYR-layer Bistratified
inhibitory_theta_phase_offset['distal apical dendritic'] = 180. / 360. * 2. * np.pi  # Like SR/SLM Border Cells
inhibitory_theta_phase_offset['tuft feedforward'] = 340. / 360. * 2. * np.pi  # Like Neurogliaform
inhibitory_theta_phase_offset['tuft feedback'] = 210. / 360. * 2. * np.pi  # Like SST+ O-LM

stim_dt = 0.02
dt = 0.02
v_init = -67.

syn_types = ['AMPA_KIN', NMDA_type]

local_random = random.Random()

# choose a subset of synapses to stimulate with inhomogeneous poisson rates
local_random.seed(synapses_seed)

cell = CA1_Pyr(morph_filename, mech_filename, full_spines=True)
cell.set_terminal_branch_nas_gradient()
cell.insert_inhibitory_synapses_in_subset()

trunk_bifurcation = [trunk for trunk in cell.trunk if cell.is_bifurcation(trunk, 'trunk')]
if trunk_bifurcation:
    trunk_branches = [branch for branch in trunk_bifurcation[0].children if branch.type == 'trunk']
    # get where the thickest trunk branch gives rise to the tuft
    trunk = max(trunk_branches, key=lambda node: node.sec(0.).diam)
    trunk = (node for node in cell.trunk if cell.node_in_subtree(trunk, node) and 'tuft' in (child.type
                                                                                    for child in node.children)).next()
else:
    trunk_bifurcation = [node for node in cell.trunk if 'tuft' in (child.type for child in node.children)]
    trunk = trunk_bifurcation[0]

all_exc_syns = {sec_type: [] for sec_type in ['basal', 'trunk', 'apical', 'tuft']}
all_inh_syns = {sec_type: [] for sec_type in ['soma', 'ais', 'basal', 'trunk', 'apical', 'tuft']}
stim_exc_syns = {'CA3': [], 'ECIII': []}
stim_inh_syns = {'perisomatic': [], 'axo-axonic': [], 'apical dendritic': [], 'distal apical dendritic': [],
                 'tuft feedforward': [], 'tuft feedback': []}
stim_successes = []
peak_locs = {'CA3': [], 'ECIII': []}

# place synapses in trunk for inheritance of mechanisms (for testing)
if 'trunk' not in all_exc_syns:
    for node in cell.trunk:
        for spine in node.spines:
            syn = Synapse(cell, spine, syn_types, stochastic=excitatory_stochastic)

# place synapses in every spine
for sec_type in all_exc_syns:
    for node in cell.get_nodes_of_subtype(sec_type):
        for spine in node.spines:
            syn = Synapse(cell, spine, syn_types, stochastic=excitatory_stochastic)
            all_exc_syns[sec_type].append(syn)
cell.init_synaptic_mechanisms()

# collate inhibitory synapses
for sec_type in all_inh_syns:
    for node in cell.get_nodes_of_subtype(sec_type):
        for syn in node.synapses:
            if 'GABA_A_KIN' in syn._syn:
                all_inh_syns[sec_type].append(syn)

sim = QuickSim(duration, cvode=0, dt=0.01)
sim.parameters['equilibrate'] = equilibrate
sim.parameters['track_equilibrate'] = track_equilibrate
sim.parameters['global_theta_cycle_duration'] = global_theta_cycle_duration
sim.parameters['input_field_duration'] = input_field_duration
sim.parameters['track_length'] = track_length
sim.parameters['duration'] = duration
sim.parameters['stim_dt'] = stim_dt
sim.append_rec(cell, cell.tree.root, description='soma', loc=0.5)
sim.append_rec(cell, trunk, description='distal_trunk', loc=0.)
sim.append_rec(cell, trunk_bifurcation[0], description='proximal_trunk', loc=1.)
spike_output_vec = h.Vector()
cell.spike_detector.record(spike_output_vec)

# get the fraction of total spines contained in each sec_type
total_exc_syns = {sec_type: len(all_exc_syns[sec_type]) for sec_type in ['basal', 'trunk', 'apical', 'tuft']}
fraction_exc_syns = {sec_type: float(total_exc_syns[sec_type]) / float(np.sum(total_exc_syns.values())) for sec_type in
                 ['basal', 'trunk', 'apical', 'tuft']}

for sec_type in all_exc_syns:
    for i in local_random.sample(range(len(all_exc_syns[sec_type])), int(num_exc_syns*fraction_exc_syns[sec_type])):
        syn = all_exc_syns[sec_type][i]
        if sec_type == 'tuft':
            stim_exc_syns['ECIII'].append(syn)
        else:
            stim_exc_syns['CA3'].append(syn)

# get the fraction of inhibitory synapses contained in each sec_type
total_inh_syns = {sec_type: len(all_inh_syns[sec_type]) for sec_type in ['soma', 'ais', 'basal', 'trunk', 'apical',
                                                                         'tuft']}
fraction_inh_syns = {sec_type: float(total_inh_syns[sec_type]) / float(np.sum(total_inh_syns.values())) for sec_type in
                 ['soma', 'ais', 'basal', 'trunk', 'apical', 'tuft']}
num_inh_syns = min(num_inh_syns, int(np.sum(total_inh_syns.values())))

for sec_type in all_inh_syns:
    for i in local_random.sample(range(len(all_inh_syns[sec_type])), int(num_inh_syns*fraction_inh_syns[sec_type])):
        syn = all_inh_syns[sec_type][i]
        if syn.node.type == 'tuft':
            if cell.is_terminal(syn.node):
                # GABAergic synapses on terminal tuft branches are about 25% feedforward
                group = local_random.choice(['tuft feedforward', 'tuft feedback', 'tuft feedback', 'tuft feedback'])
            else:
                # GABAergic synapses on intermediate tuft branches are about 50% feedforward
                group = local_random.choice(['tuft feedforward', 'tuft feedback'])
        elif syn.node.type == 'trunk':
            distance = cell.get_distance_to_node(cell.tree.root, syn.node, syn.loc)
            if distance <= 50.:
                group = 'perisomatic'
            elif distance <= 150.:
                group = 'apical dendritic'
            else:
                group = local_random.choice(['apical dendritic', 'distal apical dendritic', 'distal apical dendritic'])
        elif syn.node.type == 'basal':
            distance = cell.get_distance_to_node(cell.tree.root, syn.node, syn.loc)
            group = 'perisomatic' if distance <= 50. and not cell.is_terminal(syn.node) else 'apical dendritic'
        elif syn.node.type == 'soma':
            group = 'perisomatic'
        elif syn.node.type == 'apical':
            distance = cell.get_distance_to_node(cell.tree.root, cell.get_dendrite_origin(syn.node), loc=1.)
            if distance <= 150.:
                group = 'apical dendritic'
            else:
                group = local_random.choice(['apical dendritic', 'distal apical dendritic', 'distal apical dendritic'])
        elif syn.node.type == 'ais':
            group = 'axo-axonic'
        stim_inh_syns[group].append(syn)

stim_t = np.arange(-track_equilibrate, track_duration, dt)

gauss_sigma = global_theta_cycle_duration * input_field_width / 3. / np.sqrt(2.)  # contains 99.7% gaussian area

rand_exc_seq_locs = {}
for group in stim_exc_syns:
    rand_exc_seq_locs[group] = []
    if stim_exc_syns[group]:
        peak_locs[group] = np.arange(-0.75 * input_field_duration, (0.75 + track_length) * input_field_duration,
                          (1.5 + track_length) * input_field_duration / int(len(stim_exc_syns[group])))
        peak_locs[group] = peak_locs[group][:len(stim_exc_syns[group])]
    local_random.shuffle(peak_locs[group])
    peak_locs[group] = list(peak_locs[group])

for group in stim_exc_syns:
    for syn in stim_exc_syns[group]:
        if excitatory_stochastic:
            success_vec = h.Vector()
            stim_successes.append(success_vec)
            syn.netcon('AMPA_KIN').record(success_vec)
            rand_exc_seq_locs[group].append(syn.randObj.seq())
        # if syn.node.parent.parent not in [rec['node'] for rec in sim.rec_list]:
        #    sim.append_rec(cell, syn.node.parent.parent)
        # sim.append_rec(cell, syn.node, object=syn.target('AMPA_KIN'), param='_ref_i', description='i_AMPA')
        # sim.append_rec(cell, syn.node, object=syn.target(NMDA_type), param='_ref_i', description='i_NMDA')
        # remove this synapse from the pool, so that additional "modulated" inputs
        # can be selected from those that remain
        all_exc_syns[syn.node.parent.parent.type].remove(syn)

# rand_inh_seq_locs = [] will need this when inhibitory synapses become stochastic
# stim_inh_successes = [] will need this when inhibitory synapses become stochastic

# modulate the number and density of inputs with peak_locs along this stretch of the track
modulated_field_center = track_duration * 0.6

peak_loc_choices = {}
peak_loc_probabilities = {}
pre_modulation_num_exc_syns = {}
total_modulated_num_exc_syns = 0
gauss_mod_probability = np.exp(-((stim_t - modulated_field_center) / (gauss_sigma * 1.4)) ** 2.)
indexes = np.where(gauss_mod_probability > 0.01)[0]
start = stim_t[indexes[0]]
end = stim_t[indexes[-1]]
for group in stim_exc_syns:
    pre_modulation_num_exc_syns[group] = len(stim_exc_syns[group])
    peak_loc_t = np.arange(-0.75 * input_field_duration, (0.75 + track_length) * input_field_duration,
                          (1.5 + track_length) * input_field_duration / int(len(stim_exc_syns[group])))
    in_field_indexes = np.where((peak_loc_t >= start) & (peak_loc_t <= end))[0]
    in_field_peak_locs = peak_loc_t[in_field_indexes]
    peak_loc_probabilities = np.exp(-((in_field_peak_locs - modulated_field_center) /
                                      (gauss_sigma * 1.4)) ** 2.)
    peak_loc_probabilities /= np.sum(peak_loc_probabilities)  # sum of probabilities must equal 1
    baseline_num_exc_syns = len(np.where((peak_locs[group] >= start) & (peak_locs[group] <= end))[0])
    this_modulated_num_exc_syns = int(baseline_num_exc_syns * (mod_density - 1.))
    peak_loc_probabilities *= this_modulated_num_exc_syns  # now sum of probabilities equals number of new inputs
    peak_loc_choices[group] = []
    j = 0
    running_sum = 0.
    for i, this_peak_loc in enumerate(in_field_peak_locs):
        running_sum += peak_loc_probabilities[i]
        if running_sum >= 1.:
            bin_center = (this_peak_loc + in_field_peak_locs[j]) / 2.
            neighbor_index = np.where(in_field_peak_locs[j:] >= bin_center)[0][0]
            new_peak_loc_choice = in_field_peak_locs[j+neighbor_index]
            peak_loc_choices[group].append(new_peak_loc_choice)
            j = i
            running_sum = 0.
    local_random.shuffle(peak_loc_choices[group])
    total_modulated_num_exc_syns += len(peak_loc_choices[group])

modulated_num_exc_syns = {group: 0 for group in stim_exc_syns}
for sec_type in all_exc_syns:
    for i in local_random.sample(range(len(all_exc_syns[sec_type])),
                                 min(int(total_modulated_num_exc_syns*fraction_exc_syns[sec_type]),
                                     len(all_exc_syns[sec_type]))):
        syn = all_exc_syns[sec_type][i]
        if sec_type == 'tuft':
            group = 'ECIII'
        else:
            group = 'CA3'
        if modulated_num_exc_syns[group] < len(peak_loc_choices[group]):
            stim_exc_syns[group].append(syn)
            modulated_num_exc_syns[group] += 1

for group in stim_exc_syns:
    peak_locs[group].extend(peak_loc_choices[group][:modulated_num_exc_syns[group]])
    for syn in stim_exc_syns[group][pre_modulation_num_exc_syns[group]:]:
        if excitatory_stochastic:
            success_vec = h.Vector()
            stim_successes.append(success_vec)
            syn.netcon('AMPA_KIN').record(success_vec)
            rand_exc_seq_locs[group].append(syn.randObj.seq())
        # if syn.node.parent.parent not in [rec['node'] for rec in sim.rec_list]:
        #    sim.append_rec(cell, syn.node.parent.parent)
        # sim.append_rec(cell, syn.node, object=syn.target('AMPA_KIN'), param='_ref_i', description='i_AMPA')
        # sim.append_rec(cell, syn.node, object=syn.target(NMDA_type), param='_ref_i', description='i_NMDA')
        # remove this synapse from the pool, so that additional "modulated" inputs
        # can be selected from those that remain
        all_exc_syns[syn.node.parent.parent.type].remove(syn)

manipulated_inh_syns = {}
for group in inhibitory_manipulation_fraction:
    num_syns = int(len(stim_inh_syns[group]) * inhibitory_manipulation_fraction[group])
    manipulated_inh_syns[group] = local_random.sample(stim_inh_syns[group], num_syns)

run_trial(trial_seed)
if os.path.isfile(data_dir+rec_filename+'-working.hdf5'):
    os.rename(data_dir+rec_filename+'-working.hdf5', data_dir+rec_filename+'.hdf5')