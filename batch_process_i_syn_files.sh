#!/bin/bash
#cd $HOME/PycharmProjects/NEURON/
cd $HOME/CA1Sim
qsub -N job_061316_i_AMPA_0_0 -m e -M milsteina@janelia.hhmi.org -l d_rt=3600 -b y -cwd -V 'python process_i_syn_files.py i_AMPA 0 0'
qsub -N job_061316_i_AMPA_0_3 -l d_rt=3600 -b y -cwd -V 'python process_i_syn_files.py i_AMPA 0 3'
qsub -N job_061316_i_AMPA_1_0 -l d_rt=3600 -b y -cwd -V 'python process_i_syn_files.py i_AMPA 1 0'
qsub -N job_061316_i_AMPA_1_3 -l d_rt=3600 -b y -cwd -V 'python process_i_syn_files.py i_AMPA 1 3'
qsub -N job_061316_i_AMPA_2_0 -l d_rt=3600 -b y -cwd -V 'python process_i_syn_files.py i_AMPA 2 0'
qsub -N job_061316_i_AMPA_2_3 -l d_rt=3600 -b y -cwd -V 'python process_i_syn_files.py i_AMPA 2 3'
qsub -N job_061316_i_AMPA_3_0 -l d_rt=3600 -b y -cwd -V 'python process_i_syn_files.py i_AMPA 3 0'
qsub -N job_061316_i_AMPA_3_3 -l d_rt=3600 -b y -cwd -V 'python process_i_syn_files.py i_AMPA 3 3'
qsub -N job_061316_i_AMPA_4_0 -l d_rt=3600 -b y -cwd -V 'python process_i_syn_files.py i_AMPA 4 0'
qsub -N job_061316_i_AMPA_4_3 -l d_rt=3600 -b y -cwd -V 'python process_i_syn_files.py i_AMPA 4 3'
qsub -N job_061316_i_NMDA_0_0 -l d_rt=3600 -b y -cwd -V 'python process_i_syn_files.py i_NMDA 0 0'
qsub -N job_061316_i_NMDA_0_3 -l d_rt=3600 -b y -cwd -V 'python process_i_syn_files.py i_NMDA 0 3'
qsub -N job_061316_i_NMDA_1_0 -l d_rt=3600 -b y -cwd -V 'python process_i_syn_files.py i_NMDA 1 0'
qsub -N job_061316_i_NMDA_1_3 -l d_rt=3600 -b y -cwd -V 'python process_i_syn_files.py i_NMDA 1 3'
qsub -N job_061316_i_NMDA_2_0 -l d_rt=3600 -b y -cwd -V 'python process_i_syn_files.py i_NMDA 2 0'
qsub -N job_061316_i_NMDA_2_3 -l d_rt=3600 -b y -cwd -V 'python process_i_syn_files.py i_NMDA 2 3'
qsub -N job_061316_i_NMDA_3_0 -l d_rt=3600 -b y -cwd -V 'python process_i_syn_files.py i_NMDA 3 0'
qsub -N job_061316_i_NMDA_3_3 -l d_rt=3600 -b y -cwd -V 'python process_i_syn_files.py i_NMDA 3 3'
qsub -N job_061316_i_NMDA_4_0 -l d_rt=3600 -b y -cwd -V 'python process_i_syn_files.py i_NMDA 4 0'
qsub -N job_061316_i_NMDA_4_3 -l d_rt=3600 -b y -cwd -V 'python process_i_syn_files.py i_NMDA 4 3'
qsub -N job_061316_i_GABA_0_0 -l d_rt=3600 -b y -cwd -V 'python process_i_syn_files.py i_GABA 0 0'
qsub -N job_061316_i_GABA_0_3 -l d_rt=3600 -b y -cwd -V 'python process_i_syn_files.py i_GABA 0 3'
qsub -N job_061316_i_GABA_1_0 -l d_rt=3600 -b y -cwd -V 'python process_i_syn_files.py i_GABA 1 0'
qsub -N job_061316_i_GABA_1_3 -l d_rt=3600 -b y -cwd -V 'python process_i_syn_files.py i_GABA 1 3'
qsub -N job_061316_i_GABA_2_0 -l d_rt=3600 -b y -cwd -V 'python process_i_syn_files.py i_GABA 2 0'
qsub -N job_061316_i_GABA_2_3 -l d_rt=3600 -b y -cwd -V 'python process_i_syn_files.py i_GABA 2 3'
qsub -N job_061316_i_GABA_3_0 -l d_rt=3600 -b y -cwd -V 'python process_i_syn_files.py i_GABA 3 0'
qsub -N job_061316_i_GABA_3_3 -l d_rt=3600 -b y -cwd -V 'python process_i_syn_files.py i_GABA 3 3'
qsub -N job_061316_i_GABA_4_0 -l d_rt=3600 -b y -cwd -V 'python process_i_syn_files.py i_GABA 4 0'
qsub -N job_061316_i_GABA_4_3 -l d_rt=3600 -b y -cwd -V 'python process_i_syn_files.py i_GABA 4 3'
