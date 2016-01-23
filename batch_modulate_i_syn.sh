#!/bin/bash
#cd $HOME/PycharmProjects/NEURON/
cd $HOME/CA1Sim
qsub -pe batch 2 -N job_011816_e1600_i600_i_syn_inh0_60 -l haswell=true -m e -M milsteina@janelia.hhmi.org -b y -cwd -V 'python test_poisson_inputs_record_i_syn.py 2 1600 600 0 60'
qsub -pe batch 2 -N job_011816_e1600_i600_i_syn_inh0_61 -l haswell=true -b y -cwd -V 'python test_poisson_inputs_record_i_syn.py 2 1600 600 0 61'
qsub -pe batch 2 -N job_011816_e1600_i600_i_syn_inh0_62 -l haswell=true -b y -cwd -V 'python test_poisson_inputs_record_i_syn.py 2 1600 600 0 62'
qsub -pe batch 2 -N job_011816_e1600_i600_i_syn_inh0_63 -l haswell=true -b y -cwd -V 'python test_poisson_inputs_record_i_syn.py 2 1600 600 0 63'
qsub -pe batch 2 -N job_011816_e1600_i600_i_syn_inh0_64 -l haswell=true -b y -cwd -V 'python test_poisson_inputs_record_i_syn.py 2 1600 600 0 64'
qsub -pe batch 2 -N job_011816_e1600_i600_i_syn_inh0_65 -l haswell=true -b y -cwd -V 'python test_poisson_inputs_record_i_syn.py 2 1600 600 0 65'
qsub -pe batch 2 -N job_011816_e1600_i600_i_syn_inh0_66 -l haswell=true -b y -cwd -V 'python test_poisson_inputs_record_i_syn.py 2 1600 600 0 66'
qsub -pe batch 2 -N job_011816_e1600_i600_i_syn_inh0_67 -l haswell=true -b y -cwd -V 'python test_poisson_inputs_record_i_syn.py 2 1600 600 0 67'
qsub -pe batch 2 -N job_011816_e1600_i600_i_syn_inh0_68 -l haswell=true -b y -cwd -V 'python test_poisson_inputs_record_i_syn.py 2 1600 600 0 68'
qsub -pe batch 2 -N job_011816_e1600_i600_i_syn_inh0_69 -l haswell=true -b y -cwd -V 'python test_poisson_inputs_record_i_syn.py 2 1600 600 0 69'