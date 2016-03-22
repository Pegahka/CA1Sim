#!/bin/bash
#cd $HOME/PycharmProjects/NEURON/
cd $HOME/CA1Sim
qsub -N job_032216_e3000_i500_comp_phase_0_inh0_0 -b y -cwd -V 'python simulate_place_cell_compressed_phase.py 0 3000 500 0 2.5 0'
qsub -N job_032216_e3000_i500_comp_phase_0_inh0_1 -b y -cwd -V 'python simulate_place_cell_compressed_phase.py 0 3000 500 0 2.5 1'
qsub -N job_032216_e3000_i500_comp_phase_0_inh0_2 -b y -cwd -V 'python simulate_place_cell_compressed_phase.py 0 3000 500 0 2.5 2'
qsub -N job_032216_e3000_i500_comp_phase_0_inh0_3 -b y -cwd -V 'python simulate_place_cell_compressed_phase.py 0 3000 500 0 2.5 3'
qsub -N job_032216_e3000_i500_comp_phase_0_inh2_20 -b y -cwd -V 'python simulate_place_cell_compressed_phase.py 0 3000 500 2 2.5 20'
qsub -N job_032216_e3000_i500_comp_phase_0_inh2_21 -b y -cwd -V 'python simulate_place_cell_compressed_phase.py 0 3000 500 2 2.5 21'
qsub -N job_032216_e3000_i500_comp_phase_0_inh2_22 -b y -cwd -V 'python simulate_place_cell_compressed_phase.py 0 3000 500 2 2.5 22'
qsub -N job_032216_e3000_i500_comp_phase_0_inh2_23 -b y -cwd -V 'python simulate_place_cell_compressed_phase.py 0 3000 500 2 2.5 23'
qsub -N job_032216_e3200_i500_comp_phase_1_inh0_30 -b y -cwd -V 'python simulate_place_cell_compressed_phase.py 1 3200 500 0 2.5 30'
qsub -N job_032216_e3200_i500_comp_phase_1_inh0_31 -b y -cwd -V 'python simulate_place_cell_compressed_phase.py 1 3200 500 0 2.5 31'
qsub -N job_032216_e3200_i500_comp_phase_1_inh0_32 -b y -cwd -V 'python simulate_place_cell_compressed_phase.py 1 3200 500 0 2.5 32'
qsub -N job_032216_e3200_i500_comp_phase_1_inh0_33 -b y -cwd -V 'python simulate_place_cell_compressed_phase.py 1 3200 500 0 2.5 33'
qsub -N job_032216_e3200_i500_comp_phase_1_inh2_50 -b y -cwd -V 'python simulate_place_cell_compressed_phase.py 1 3200 500 2 2.5 50'
qsub -N job_032216_e3200_i500_comp_phase_1_inh2_51 -b y -cwd -V 'python simulate_place_cell_compressed_phase.py 1 3200 500 2 2.5 51'
qsub -N job_032216_e3200_i500_comp_phase_1_inh2_52 -b y -cwd -V 'python simulate_place_cell_compressed_phase.py 1 3200 500 2 2.5 52'
qsub -N job_032216_e3200_i500_comp_phase_1_inh2_53 -b y -cwd -V 'python simulate_place_cell_compressed_phase.py 1 3200 500 2 2.5 53'
qsub -N job_032216_e3400_i500_comp_phase_2_inh0_60 -b y -cwd -V 'python simulate_place_cell_compressed_phase.py 2 3400 500 0 2.5 60'
qsub -N job_032216_e3400_i500_comp_phase_2_inh0_61 -b y -cwd -V 'python simulate_place_cell_compressed_phase.py 2 3400 500 0 2.5 61'
qsub -N job_032216_e3400_i500_comp_phase_2_inh0_62 -b y -cwd -V 'python simulate_place_cell_compressed_phase.py 2 3400 500 0 2.5 62'
qsub -N job_032216_e3400_i500_comp_phase_2_inh0_63 -b y -cwd -V 'python simulate_place_cell_compressed_phase.py 2 3400 500 0 2.5 63'
qsub -N job_032216_e3400_i500_comp_phase_2_inh2_80 -b y -cwd -V 'python simulate_place_cell_compressed_phase.py 2 3400 500 2 2.5 80'
qsub -N job_032216_e3400_i500_comp_phase_2_inh2_81 -b y -cwd -V 'python simulate_place_cell_compressed_phase.py 2 3400 500 2 2.5 81'
qsub -N job_032216_e3400_i500_comp_phase_2_inh2_82 -b y -cwd -V 'python simulate_place_cell_compressed_phase.py 2 3400 500 2 2.5 82'
qsub -N job_032216_e3400_i500_comp_phase_2_inh2_83 -m e -M milsteina@janelia.hhmi.org -b y -cwd -V 'python simulate_place_cell_compressed_phase.py 2 3400 500 2 2.5 83'


