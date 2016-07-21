#!/bin/bash
#cd $HOME/PycharmProjects/NEURON/
cd $HOME/CA1Sim
qsub -N job_072116_e3200_i600_silent6_inh0_0 -l d_rt=36000 -b y -cwd -V 'python simulate_place_cell_subtr_inh_silent.py 6 3200 600 0 0'
qsub -N job_072116_e3200_i600_silent6_inh0_1 -l d_rt=36000 -b y -cwd -V 'python simulate_place_cell_subtr_inh_silent.py 6 3200 600 0 1'
qsub -N job_072116_e3200_i600_silent6_inh0_2 -l d_rt=36000 -b y -cwd -V 'python simulate_place_cell_subtr_inh_silent.py 6 3200 600 0 2'
qsub -N job_072116_e3200_i600_silent6_inh0_3 -l d_rt=36000 -b y -cwd -V 'python simulate_place_cell_subtr_inh_silent.py 6 3200 600 0 3'
qsub -N job_072116_e3200_i600_silent6_inh0_4 -l d_rt=36000 -b y -cwd -V 'python simulate_place_cell_subtr_inh_silent.py 6 3200 600 0 4'
qsub -N job_072116_e3200_i600_silent6_inh0_5 -l d_rt=36000 -b y -cwd -V 'python simulate_place_cell_subtr_inh_silent.py 6 3200 600 0 5'
qsub -N job_072116_e3200_i600_silent6_inh0_6 -l d_rt=36000 -b y -cwd -V 'python simulate_place_cell_subtr_inh_silent.py 6 3200 600 0 6'
qsub -N job_072116_e3200_i600_silent6_inh0_7 -l d_rt=36000 -b y -cwd -V 'python simulate_place_cell_subtr_inh_silent.py 6 3200 600 0 7'
qsub -N job_072116_e3200_i600_silent6_inh0_8 -l d_rt=36000 -b y -cwd -V 'python simulate_place_cell_subtr_inh_silent.py 6 3200 600 0 8'
qsub -N job_072116_e3200_i600_silent6_inh0_9 -l d_rt=36000 -b y -cwd -V 'python simulate_place_cell_subtr_inh_silent.py 6 3200 600 0 9'
qsub -N job_072116_e3200_i600_silent6_inh0_10 -l d_rt=36000 -b y -cwd -V 'python simulate_place_cell_subtr_inh_silent.py 6 3200 600 0 10'
qsub -N job_072116_e3200_i600_silent6_inh0_11 -l d_rt=36000 -b y -cwd -V 'python simulate_place_cell_subtr_inh_silent.py 6 3200 600 0 11'
qsub -N job_072116_e3200_i600_silent6_inh0_12 -l d_rt=36000 -b y -cwd -V 'python simulate_place_cell_subtr_inh_silent.py 6 3200 600 0 12'
qsub -N job_072116_e3200_i600_silent6_inh0_13 -l d_rt=36000 -b y -cwd -V 'python simulate_place_cell_subtr_inh_silent.py 6 3200 600 0 13'
qsub -N job_072116_e3200_i600_silent6_inh0_14 -l d_rt=36000 -b y -cwd -V 'python simulate_place_cell_subtr_inh_silent.py 6 3200 600 0 14'
qsub -N job_072116_e3200_i600_silent6_inh0_15 -l d_rt=36000 -b y -cwd -V 'python simulate_place_cell_subtr_inh_silent.py 6 3200 600 0 15'
qsub -N job_072116_e3200_i600_silent6_inh0_16 -l d_rt=36000 -b y -cwd -V 'python simulate_place_cell_subtr_inh_silent.py 6 3200 600 0 16'
qsub -N job_072116_e3200_i600_silent6_inh0_17 -l d_rt=36000 -b y -cwd -V 'python simulate_place_cell_subtr_inh_silent.py 6 3200 600 0 17'
qsub -N job_072116_e3200_i600_silent6_inh0_18 -l d_rt=36000 -b y -cwd -V 'python simulate_place_cell_subtr_inh_silent.py 6 3200 600 0 18'
qsub -N job_072116_e3200_i600_silent6_inh0_19 -m e -M milsteina@janelia.hhmi.org -l d_rt=36000 -b y -cwd -V 'python simulate_place_cell_subtr_inh_silent.py 6 3200 600 0 19'
