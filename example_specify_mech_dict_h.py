__author__ = 'milsteina'
from specify_cells import *
from plot_results import *

#morph_filename = 'EB1-early-bifurcation.swc'
morph_filename = 'EB2-late-bifurcation.swc'
mech_filename = '042015 pas_ka_scale kdr - EB2.pkl'

cell = CA1_Pyr(morph_filename, mech_filename, full_spines=True)

cell.modify_mech_param('soma', 'h', 'ghbar', 0.00005)
cell.modify_mech_param('soma', 'h', 'vhalfl', -73.)
cell.modify_mech_param('soma', 'h', 'eh', -30.)

cell.modify_mech_param('basal', 'h', 'ghbar', origin='soma')
cell.modify_mech_param('basal', 'h', 'vhalfl', origin='soma')

for sec_type in ['basal', 'trunk', 'apical', 'tuft']:
    cell.modify_mech_param(sec_type, 'h', 'eh', origin='soma')

cell.modify_mech_param('trunk', 'h', 'ghbar', origin='soma', slope=1.e-6)
cell.modify_mech_param('trunk', 'h', 'vhalfl', origin='soma', max_loc=75.)
cell.modify_mech_param('trunk', 'h', 'vhalfl', origin='soma', slope=-0.16, min_loc=75., max_loc=125., replace=False)
cell.modify_mech_param('trunk', 'h', 'vhalfl', -81., origin='soma', min_loc=125., replace=False)

for sec_type in ['apical', 'tuft']:
    cell.modify_mech_param(sec_type, 'h', 'ghbar', origin='trunk')
    cell.modify_mech_param(sec_type, 'h', 'vhalfl', origin='trunk')

plot_mech_param_distribution(cell, 'h', 'ghbar')
plot_mech_param_distribution(cell, 'h', 'vhalfl')