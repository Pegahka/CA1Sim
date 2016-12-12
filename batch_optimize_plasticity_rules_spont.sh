#!/bin/bash
cd $HOME/CA1Sim_dev
qsub -N long_spont_121216_cell01 -l d_rt=36000 -b y -cwd -V 'python optimize_long_time_scale_plasticity_rule_spont_121016.py 1'
qsub -N long_spont_121216_cell02 -l d_rt=36000 -b y -cwd -V 'python optimize_long_time_scale_plasticity_rule_spont_121016.py 2'
qsub -N long_spont_121216_cell03 -l d_rt=36000 -b y -cwd -V 'python optimize_long_time_scale_plasticity_rule_spont_121016.py 3'
qsub -N long_spont_121216_cell04 -l d_rt=36000 -b y -cwd -V 'python optimize_long_time_scale_plasticity_rule_spont_121016.py 4'
qsub -N long_spont_121216_cell05 -l d_rt=36000 -b y -cwd -V 'python optimize_long_time_scale_plasticity_rule_spont_121016.py 5'
qsub -N long_spont_121216_cell06 -l d_rt=36000 -b y -cwd -V 'python optimize_long_time_scale_plasticity_rule_spont_121016.py 6'
qsub -N long_spont_121216_cell07 -l d_rt=36000 -m e -M milsteina@janelia.hhmi.org -b y -cwd -V 'python optimize_long_time_scale_plasticity_rule_spont_121016.py 7'

qsub -N short_spont_121216_cell01 -l d_rt=36000 -b y -cwd -V 'python optimize_short_time_scale_plasticity_rule_spont_121016.py 1'
qsub -N short_spont_121216_cell02 -l d_rt=36000 -b y -cwd -V 'python optimize_short_time_scale_plasticity_rule_spont_121016.py 2'
qsub -N short_spont_121216_cell03 -l d_rt=36000 -b y -cwd -V 'python optimize_short_time_scale_plasticity_rule_spont_121016.py 3'
qsub -N short_spont_121216_cell04 -l d_rt=36000 -b y -cwd -V 'python optimize_short_time_scale_plasticity_rule_spont_121016.py 4'
qsub -N short_spont_121216_cell05 -l d_rt=36000 -b y -cwd -V 'python optimize_short_time_scale_plasticity_rule_spont_121016.py 5'
qsub -N short_spont_121216_cell06 -l d_rt=36000 -b y -cwd -V 'python optimize_short_time_scale_plasticity_rule_spont_121016.py 6'
qsub -N short_spont_121216_cell07 -l d_rt=36000 -m e -M milsteina@janelia.hhmi.org -b y -cwd -V 'python optimize_short_time_scale_plasticity_rule_spont_121016.py 7'
