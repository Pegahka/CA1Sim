#!/bin/bash
#cd $HOME/PycharmProjects/NEURON/
cd $HOME/CA1Sim
qsub -N job_081415_i400_mod_amp_0 -m e -M milsteina@janelia.hhmi.org -b y -cwd -V 'python test_poisson_inputs_modulate_amplitude.py 1 1400 400 0'
qsub -N job_081415_i400_mod_amp_1 -b y -cwd -V 'python test_poisson_inputs_modulate_amplitude.py 1 1400 400 1'
qsub -N job_081415_i400_mod_amp_2 -b y -cwd -V 'python test_poisson_inputs_modulate_amplitude.py 1 1400 400 2'
qsub -N job_081415_i400_mod_amp_3 -b y -cwd -V 'python test_poisson_inputs_modulate_amplitude.py 1 1400 400 3'
qsub -N job_081415_i400_mod_amp_4 -b y -cwd -V 'python test_poisson_inputs_modulate_amplitude.py 1 1400 400 4'
qsub -N job_081415_i400_mod_amp_5 -b y -cwd -V 'python test_poisson_inputs_modulate_amplitude.py 1 1400 400 5'
qsub -N job_081415_i400_mod_amp_6 -b y -cwd -V 'python test_poisson_inputs_modulate_amplitude.py 1 1400 400 6'
qsub -N job_081415_i400_mod_amp_7 -b y -cwd -V 'python test_poisson_inputs_modulate_amplitude.py 1 1400 400 7'
qsub -N job_081415_i400_mod_amp_8 -b y -cwd -V 'python test_poisson_inputs_modulate_amplitude.py 1 1400 400 8'
qsub -N job_081415_i400_mod_amp_9 -b y -cwd -V 'python test_poisson_inputs_modulate_amplitude.py 1 1400 400 9'
qsub -N job_081415_i200_mod_amp_0 -m e -M milsteina@janelia.hhmi.org -b y -cwd -V 'python test_poisson_inputs_modulate_amplitude.py 1 1400 200 0'
qsub -N job_081415_i200_mod_amp_1 -b y -cwd -V 'python test_poisson_inputs_modulate_amplitude.py 1 1400 200 1'
qsub -N job_081415_i200_mod_amp_2 -b y -cwd -V 'python test_poisson_inputs_modulate_amplitude.py 1 1400 200 2'
qsub -N job_081415_i200_mod_amp_3 -b y -cwd -V 'python test_poisson_inputs_modulate_amplitude.py 1 1400 200 3'
qsub -N job_081415_i200_mod_amp_4 -b y -cwd -V 'python test_poisson_inputs_modulate_amplitude.py 1 1400 200 4'
qsub -N job_081415_i200_mod_amp_5 -b y -cwd -V 'python test_poisson_inputs_modulate_amplitude.py 1 1400 200 5'
qsub -N job_081415_i200_mod_amp_6 -b y -cwd -V 'python test_poisson_inputs_modulate_amplitude.py 1 1400 200 6'
qsub -N job_081415_i200_mod_amp_7 -b y -cwd -V 'python test_poisson_inputs_modulate_amplitude.py 1 1400 200 7'
qsub -N job_081415_i200_mod_amp_8 -b y -cwd -V 'python test_poisson_inputs_modulate_amplitude.py 1 1400 200 8'
qsub -N job_081415_i200_mod_amp_9 -b y -cwd -V 'python test_poisson_inputs_modulate_amplitude.py 1 1400 200 9'