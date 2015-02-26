__author__ = 'Aaron D. Milstein'
import time
from specify_cells import *
from plot_results import *

#morph_filename = 'EB022715-stitched-proofread.swc'
morph_filename = 'Erik_Bloss_CA1_0215_Stitched_Proofread.swc'
mech_filename = '022315 kap_scale kd ih_scale no_na.pkl'
rec_filename = '030215 kap_scale kd ih_scale no_na - EB1Morph- ar'


equilibrate = 200.  # time to steady-state
duration = 250.
amp = 0.06

cell = CA1_Pyr(morph_filename, mech_filename, full_spines=False)
for node in cell.basal+cell.trunk+cell.apical+cell.tuft:
    syn = Synapse(cell, node, ['EPSC'], stochastic=0)
    syn.netcon('EPSC').weight[0] = amp
    cell.insert_spine(node, 0.5)
    syn = Synapse(cell, node.spines[0], ['EPSC'], stochastic=0)
    syn.netcon('EPSC').weight[0] = amp
cell._reinit_mech(cell.spine)

sim = QuickSim(duration)
sim.parameters['amp'] = amp
sim.parameters['equilibrate'] = equilibrate
sim.parameters['duration'] = duration
sim.append_rec(cell, cell.tree.root, 0.5)
sim.append_rec(cell, cell.tree.root, 0.5)

spike_times = h.Vector([equilibrate])

f = h5py.File(data_dir+rec_filename+'.hdf5', 'w')
simiter = 0
for node in cell.basal+cell.trunk+cell.apical+cell.tuft:
    start_time = time.time()
    sim.parameters['stim_loc'] = 'spine'
    sim.modify_rec(0, node, description='branch')
    sim.modify_rec(1, node.spines[0], description='spine')
    syn = node.spines[0].synapses[0]
    syn.source.play(spike_times)
    print 'Run: ', simiter, ', stim spine'
    sim.run()
    print 'Took: ', time.time() - start_time, ' sec'
    sim.export_to_file(f, simiter)
    syn.source = None
    simiter += 1
    start_time = time.time()
    sim.parameters['stim_loc'] = 'branch'
    syn = node.synapses[0]
    syn.source.play(spike_times)
    print 'Run: ', simiter, ', stim branch'
    sim.run()
    print 'Took: ', time.time() - start_time, ' sec'
    sim.export_to_file(f, simiter)
    syn.source = None
    simiter += 1
f.close()

plot_AR(rec_filename)