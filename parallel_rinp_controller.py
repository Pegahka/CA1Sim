__author__ = 'milsteina'
from IPython.parallel import Client
from IPython.display import clear_output
from plot_results import *
import parallel_rinp_engine
import sys
"""
Parallel version: Iterates through every section, injecting hyperpolarizing current and measuring input resistance.

Assumes a controller is already running in another process with:
ipcluster start -n num_cores
"""
filename_suffix = ' - Rinp'
new_rec_filename = parallel_rinp_engine.mech_filename+filename_suffix

c = Client()
num_secs = len(parallel_rinp_engine.nodes)

dv = c[:]
dv.clear()
dv.block = True
start_time = time.time()
dv.execute('from parallel_rinp_engine import *')
v = c.load_balanced_view()
result = v.map_async(parallel_rinp_engine.test_single_section, range(num_secs))
while not result.ready():
    clear_output()
    for stdout in [stdout for stdout in result.stdout if stdout][-len(c):]:
        lines = stdout.split('\n')
        if lines[-2]:
            print lines[-2]
    sys.stdout.flush()
    time.sleep(60)
for stdout in result.stdout:
    if stdout:
        lines = stdout.split('\n')
        if lines[-2]:
            print lines[-2]
print 'Parallel execution took: ', time.time()-start_time, ' s'
rec_file_list = dv['rec_filename']
combine_output_files(rec_file_list, new_rec_filename)
plot_Rinp(new_rec_filename)
