#!/bin/bash
#cd $HOME/PycharmProjects/NEURON/
cd $HOME/CA1Sim
qsub -N job_081415_i200_4 -m e -M milsteina@janelia.hhmi.org -b y -cwd -V 'python test_poisson_inputs.py 1 1400 200 4'
qsub -N job_081415_i200_5 -b y -cwd -V 'python test_poisson_inputs.py 1 1400 200 5'
qsub -N job_081415_i200_6 -b y -cwd -V 'python test_poisson_inputs.py 1 1400 200 6'
qsub -N job_081415_i200_7 -b y -cwd -V 'python test_poisson_inputs.py 1 1400 200 7'
qsub -N job_081415_i200_8 -b y -cwd -V 'python test_poisson_inputs.py 1 1400 200 8'
qsub -N job_081415_i200_9 -b y -cwd -V 'python test_poisson_inputs.py 1 1400 200 9'
qsub -N job_081415_i400_4 -b y -cwd -V 'python test_poisson_inputs.py 1 1400 400 4'
qsub -N job_081415_i400_5 -m e -M milsteina@janelia.hhmi.org -b y -cwd -V 'python test_poisson_inputs.py 1 1400 400 5'
qsub -N job_081415_i400_6 -b y -cwd -V 'python test_poisson_inputs.py 1 1400 400 6'
qsub -N job_081415_i400_7 -b y -cwd -V 'python test_poisson_inputs.py 1 1400 400 7'
qsub -N job_081415_i400_8 -b y -cwd -V 'python test_poisson_inputs.py 1 1400 400 8'
qsub -N job_081415_i400_9 -b y -cwd -V 'python test_poisson_inputs.py 1 1400 400 9'
qsub -N job_081415_i600_4 -b y -cwd -V 'python test_poisson_inputs.py 1 1400 600 4'
qsub -N job_081415_i600_5 -m e -M milsteina@janelia.hhmi.org -b y -cwd -V 'python test_poisson_inputs.py 1 1400 400 5'
qsub -N job_081415_i600_6 -b y -cwd -V 'python test_poisson_inputs.py 1 1400 600 6'
qsub -N job_081415_i600_7 -b y -cwd -V 'python test_poisson_inputs.py 1 1400 600 7'
qsub -N job_081415_i600_8 -b y -cwd -V 'python test_poisson_inputs.py 1 1400 600 8'
qsub -N job_081415_i600_9 -b y -cwd -V 'python test_poisson_inputs.py 1 1400 600 9'