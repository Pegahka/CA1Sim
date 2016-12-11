#!/bin/bash
cd $HOME/CA1Sim_dev
qsub -N long_cell_121016_cell02 -l d_rt=36000 -b y -cwd -V 'python optimize_long_time_scale_plasticity_rule_121016.py 2'
qsub -N long_cell_121016_cell04 -l d_rt=36000 -b y -cwd -V 'python optimize_long_time_scale_plasticity_rule_121016.py 4'
qsub -N long_cell_121016_cell05 -l d_rt=36000 -b y -cwd -V 'python optimize_long_time_scale_plasticity_rule_121016.py 5'
qsub -N long_cell_121016_cell06 -l d_rt=36000 -b y -cwd -V 'python optimize_long_time_scale_plasticity_rule_121016.py 6'
qsub -N long_cell_121016_cell07 -l d_rt=36000 -b y -cwd -V 'python optimize_long_time_scale_plasticity_rule_121016.py 7'
qsub -N long_cell_121016_cell08 -l d_rt=36000 -b y -cwd -V 'python optimize_long_time_scale_plasticity_rule_121016.py 8'
qsub -N long_cell_121016_cell09 -l d_rt=36000 -b y -cwd -V 'python optimize_long_time_scale_plasticity_rule_121016.py 9'
qsub -N long_cell_121016_cell10 -l d_rt=36000 -b y -cwd -V 'python optimize_long_time_scale_plasticity_rule_121016.py 10'
qsub -N long_cell_121016_cell11 -l d_rt=36000 -b y -cwd -V 'python optimize_long_time_scale_plasticity_rule_121016.py 11'
qsub -N long_cell_121016_cell12 -l d_rt=36000 -b y -cwd -V 'python optimize_long_time_scale_plasticity_rule_121016.py 12'
qsub -N long_cell_121016_cell13 -l d_rt=36000 -b y -cwd -V 'python optimize_long_time_scale_plasticity_rule_121016.py 13'
qsub -N long_cell_121016_cell14 -l d_rt=36000 -b y -cwd -V 'python optimize_long_time_scale_plasticity_rule_121016.py 14'
qsub -N long_cell_121016_cell15 -l d_rt=36000 -b y -cwd -V 'python optimize_long_time_scale_plasticity_rule_121016.py 15'
qsub -N long_cell_121016_cell17 -l d_rt=36000 -b y -cwd -V 'python optimize_long_time_scale_plasticity_rule_121016.py 17'
qsub -N long_cell_121016_cell18 -l d_rt=36000 -m e -M milsteina@janelia.hhmi.org -b y -cwd -V 'python optimize_long_time_scale_plasticity_rule_121016.py 18'

qsub -N short_cell_121016_cell01 -l d_rt=36000 -b y -cwd -V 'python optimize_short_time_scale_plasticity_rule_121016.py 1'
qsub -N short_cell_121016_cell02 -l d_rt=36000 -b y -cwd -V 'python optimize_short_time_scale_plasticity_rule_121016.py 2'
qsub -N short_cell_121016_cell04 -l d_rt=36000 -b y -cwd -V 'python optimize_short_time_scale_plasticity_rule_121016.py 4'
qsub -N short_cell_121016_cell05 -l d_rt=36000 -b y -cwd -V 'python optimize_short_time_scale_plasticity_rule_121016.py 5'
qsub -N short_cell_121016_cell06 -l d_rt=36000 -b y -cwd -V 'python optimize_short_time_scale_plasticity_rule_121016.py 6'
qsub -N short_cell_121016_cell07 -l d_rt=36000 -b y -cwd -V 'python optimize_short_time_scale_plasticity_rule_121016.py 7'
qsub -N short_cell_121016_cell08 -l d_rt=36000 -b y -cwd -V 'python optimize_short_time_scale_plasticity_rule_121016.py 8'
qsub -N short_cell_121016_cell09 -l d_rt=36000 -b y -cwd -V 'python optimize_short_time_scale_plasticity_rule_121016.py 9'
qsub -N short_cell_121016_cell10 -l d_rt=36000 -b y -cwd -V 'python optimize_short_time_scale_plasticity_rule_121016.py 10'
qsub -N short_cell_121016_cell11 -l d_rt=36000 -b y -cwd -V 'python optimize_short_time_scale_plasticity_rule_121016.py 11'
qsub -N short_cell_121016_cell12 -l d_rt=36000 -b y -cwd -V 'python optimize_short_time_scale_plasticity_rule_121016.py 12'
qsub -N short_cell_121016_cell13 -l d_rt=36000 -b y -cwd -V 'python optimize_short_time_scale_plasticity_rule_121016.py 13'
qsub -N short_cell_121016_cell14 -l d_rt=36000 -b y -cwd -V 'python optimize_short_time_scale_plasticity_rule_121016.py 14'
qsub -N short_cell_121016_cell15 -l d_rt=36000 -b y -cwd -V 'python optimize_short_time_scale_plasticity_rule_121016.py 15'
qsub -N short_cell_121016_cell17 -l d_rt=36000 -b y -cwd -V 'python optimize_short_time_scale_plasticity_rule_121016.py 17'
qsub -N short_cell_121016_cell18 -l d_rt=36000 -m e -M milsteina@janelia.hhmi.org -b y -cwd -V 'python optimize_short_time_scale_plasticity_rule_121016.py 18'