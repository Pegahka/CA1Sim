#!/bin/bash
#cd $HOME/PycharmProjects/NEURON/
cd $HOME/CA1Sim
qsub -N job_060216_e3200_i500_subtr_0_shape1.0_inh0_0 -l d_rt=36000 -b y -cwd -V 'python simulate_place_cell_subtr_inh_shape_inh.py 0 3200 500 0 1.0 0'
qsub -N job_060216_e3200_i500_subtr_0_shape1.0_inh0_1 -l d_rt=36000 -b y -cwd -V 'python simulate_place_cell_subtr_inh_shape_inh.py 0 3200 500 0 1.0 1'
qsub -N job_060216_e3200_i500_subtr_0_shape1.0_inh0_2 -l d_rt=36000 -b y -cwd -V 'python simulate_place_cell_subtr_inh_shape_inh.py 0 3200 500 0 1.0 2'
qsub -N job_060216_e3200_i500_subtr_0_shape1.0_inh0_3 -l d_rt=36000 -b y -cwd -V 'python simulate_place_cell_subtr_inh_shape_inh.py 0 3200 500 0 1.0 3'
qsub -N job_060216_e3200_i500_subtr_0_shape1.0_inh0_4 -l d_rt=36000 -b y -cwd -V 'python simulate_place_cell_subtr_inh_shape_inh.py 0 3200 500 0 1.0 4'
qsub -N job_060216_e3200_i500_subtr_0_shape1.0_inh0_5 -l d_rt=36000 -b y -cwd -V 'python simulate_place_cell_subtr_inh_shape_inh.py 0 3200 500 0 1.0 5'
qsub -N job_060216_e3200_i500_subtr_0_shape1.0_inh0_6 -l d_rt=36000 -b y -cwd -V 'python simulate_place_cell_subtr_inh_shape_inh.py 0 3200 500 0 1.0 6'
qsub -N job_060216_e3200_i500_subtr_0_shape1.0_inh0_7 -l d_rt=36000 -b y -cwd -V 'python simulate_place_cell_subtr_inh_shape_inh.py 0 3200 500 0 1.0 7'
qsub -N job_060216_e3200_i500_subtr_0_shape1.0_inh0_8 -l d_rt=36000 -b y -cwd -V 'python simulate_place_cell_subtr_inh_shape_inh.py 0 3200 500 0 1.0 8'
qsub -N job_060216_e3200_i500_subtr_0_shape1.0_inh0_9 -l d_rt=36000 -b y -cwd -V 'python simulate_place_cell_subtr_inh_shape_inh.py 0 3200 500 0 1.0 9'
qsub -N job_060216_e3200_i500_subtr_0_shape1.0_inh3_20 -l d_rt=36000 -b y -cwd -V 'python simulate_place_cell_subtr_inh_shape_inh.py 0 3200 500 3 1.0 20'
qsub -N job_060216_e3200_i500_subtr_0_shape1.0_inh3_21 -l d_rt=36000 -b y -cwd -V 'python simulate_place_cell_subtr_inh_shape_inh.py 0 3200 500 3 1.0 21'
qsub -N job_060216_e3200_i500_subtr_0_shape1.0_inh3_22 -l d_rt=36000 -b y -cwd -V 'python simulate_place_cell_subtr_inh_shape_inh.py 0 3200 500 3 1.0 22'
qsub -N job_060216_e3200_i500_subtr_0_shape1.0_inh3_23 -l d_rt=36000 -b y -cwd -V 'python simulate_place_cell_subtr_inh_shape_inh.py 0 3200 500 3 1.0 23'
qsub -N job_060216_e3200_i500_subtr_0_shape1.0_inh3_24 -l d_rt=36000 -b y -cwd -V 'python simulate_place_cell_subtr_inh_shape_inh.py 0 3200 500 3 1.0 24'
qsub -N job_060216_e3200_i500_subtr_0_shape1.0_inh3_25 -l d_rt=36000 -b y -cwd -V 'python simulate_place_cell_subtr_inh_shape_inh.py 0 3200 500 3 1.0 25'
qsub -N job_060216_e3200_i500_subtr_0_shape1.0_inh3_26 -l d_rt=36000 -b y -cwd -V 'python simulate_place_cell_subtr_inh_shape_inh.py 0 3200 500 3 1.0 26'
qsub -N job_060216_e3200_i500_subtr_0_shape1.0_inh3_27 -l d_rt=36000 -b y -cwd -V 'python simulate_place_cell_subtr_inh_shape_inh.py 0 3200 500 3 1.0 27'
qsub -N job_060216_e3200_i500_subtr_0_shape1.0_inh3_28 -l d_rt=36000 -b y -cwd -V 'python simulate_place_cell_subtr_inh_shape_inh.py 0 3200 500 3 1.0 28'
qsub -N job_060216_e3200_i500_subtr_0_shape1.0_inh3_29 -m e -M milsteina@janelia.hhmi.org -l d_rt=36000 -b y -cwd -V 'python simulate_place_cell_subtr_inh_shape_inh.py 0 3200 500 3 1.0 29'
qsub -N job_060216_e3200_i500_subtr_inh_0_inh3_20 -l d_rt=36000 -b y -cwd -V 'python simulate_place_cell_subtr_inh.py 0 3200 500 3 2.5 20'
qsub -N job_060216_e3200_i500_subtr_inh_0_inh3_21 -l d_rt=36000 -b y -cwd -V 'python simulate_place_cell_subtr_inh.py 0 3200 500 3 2.5 21'
qsub -N job_060216_e3200_i500_subtr_inh_0_inh3_22 -l d_rt=36000 -b y -cwd -V 'python simulate_place_cell_subtr_inh.py 0 3200 500 3 2.5 22'
qsub -N job_060216_e3200_i500_subtr_inh_0_inh3_23 -l d_rt=36000 -b y -cwd -V 'python simulate_place_cell_subtr_inh.py 0 3200 500 3 2.5 23'
qsub -N job_060216_e3200_i500_subtr_inh_0_inh3_24 -l d_rt=36000 -b y -cwd -V 'python simulate_place_cell_subtr_inh.py 0 3200 500 3 2.5 24'
qsub -N job_060216_e3200_i500_subtr_inh_0_inh3_25 -l d_rt=36000 -b y -cwd -V 'python simulate_place_cell_subtr_inh.py 0 3200 500 3 2.5 25'
qsub -N job_060216_e3200_i500_subtr_inh_0_inh3_26 -l d_rt=36000 -b y -cwd -V 'python simulate_place_cell_subtr_inh.py 0 3200 500 3 2.5 26'
qsub -N job_060216_e3200_i500_subtr_inh_0_inh3_27 -l d_rt=36000 -b y -cwd -V 'python simulate_place_cell_subtr_inh.py 0 3200 500 3 2.5 27'
qsub -N job_060216_e3200_i500_subtr_inh_0_inh3_28 -l d_rt=36000 -b y -cwd -V 'python simulate_place_cell_subtr_inh.py 0 3200 500 3 2.5 28'
qsub -N job_060216_e3200_i500_subtr_inh_0_inh3_29 -l d_rt=36000 -b y -cwd -V 'python simulate_place_cell_subtr_inh.py 0 3200 500 3 2.5 29'
qsub -N job_060216_e3200_i500_subtr_50_shape0.5_inh3_1520 -l d_rt=36000 -b y -cwd -V 'python simulate_place_cell_subtr_inh_shape_inh.py 50 3200 500 3 0.5 1520'
qsub -N job_060216_e3200_i500_subtr_50_shape0.5_inh3_1521 -l d_rt=36000 -b y -cwd -V 'python simulate_place_cell_subtr_inh_shape_inh.py 50 3200 500 3 0.5 1521'
qsub -N job_060216_e3200_i500_subtr_50_shape0.5_inh3_1522 -l d_rt=36000 -b y -cwd -V 'python simulate_place_cell_subtr_inh_shape_inh.py 50 3200 500 3 0.5 1522'
qsub -N job_060216_e3200_i500_subtr_50_shape0.5_inh3_1523 -l d_rt=36000 -b y -cwd -V 'python simulate_place_cell_subtr_inh_shape_inh.py 50 3200 500 3 0.5 1523'
qsub -N job_060216_e3200_i500_subtr_50_shape0.5_inh3_1524 -l d_rt=36000 -b y -cwd -V 'python simulate_place_cell_subtr_inh_shape_inh.py 50 3200 500 3 0.5 1524'
qsub -N job_060216_e3200_i500_subtr_50_shape0.5_inh3_1525 -l d_rt=36000 -b y -cwd -V 'python simulate_place_cell_subtr_inh_shape_inh.py 50 3200 500 3 0.5 1525'
qsub -N job_060216_e3200_i500_subtr_50_shape0.5_inh3_1526 -l d_rt=36000 -b y -cwd -V 'python simulate_place_cell_subtr_inh_shape_inh.py 50 3200 500 3 0.5 1526'
qsub -N job_060216_e3200_i500_subtr_50_shape0.5_inh3_1527 -l d_rt=36000 -b y -cwd -V 'python simulate_place_cell_subtr_inh_shape_inh.py 50 3200 500 3 0.5 1527'
qsub -N job_060216_e3200_i500_subtr_50_shape0.5_inh3_1528 -l d_rt=36000 -b y -cwd -V 'python simulate_place_cell_subtr_inh_shape_inh.py 50 3200 500 3 0.5 1528'
qsub -N job_060216_e3200_i500_subtr_50_shape0.5_inh3_1529 -l d_rt=36000 -b y -cwd -V 'python simulate_place_cell_subtr_inh_shape_inh.py 50 3200 500 3 0.5 1529'
qsub -N job_060216_e3200_i500_subtr_40_shape2.0_inh3_1220 -l d_rt=36000 -b y -cwd -V 'python simulate_place_cell_subtr_inh_shape_inh.py 40 3200 500 3 2.0 1220'
qsub -N job_060216_e3200_i500_subtr_40_shape2.0_inh3_1221 -l d_rt=36000 -b y -cwd -V 'python simulate_place_cell_subtr_inh_shape_inh.py 40 3200 500 3 2.0 1221'
qsub -N job_060216_e3200_i500_subtr_40_shape2.0_inh3_1222 -l d_rt=36000 -b y -cwd -V 'python simulate_place_cell_subtr_inh_shape_inh.py 40 3200 500 3 2.0 1222'
qsub -N job_060216_e3200_i500_subtr_40_shape2.0_inh3_1223 -l d_rt=36000 -b y -cwd -V 'python simulate_place_cell_subtr_inh_shape_inh.py 40 3200 500 3 2.0 1223'
qsub -N job_060216_e3200_i500_subtr_40_shape2.0_inh3_1224 -l d_rt=36000 -b y -cwd -V 'python simulate_place_cell_subtr_inh_shape_inh.py 40 3200 500 3 2.0 1224'
qsub -N job_060216_e3200_i500_subtr_40_shape2.0_inh3_1225 -l d_rt=36000 -b y -cwd -V 'python simulate_place_cell_subtr_inh_shape_inh.py 40 3200 500 3 2.0 1225'
qsub -N job_060216_e3200_i500_subtr_40_shape2.0_inh3_1226 -l d_rt=36000 -b y -cwd -V 'python simulate_place_cell_subtr_inh_shape_inh.py 40 3200 500 3 2.0 1226'
qsub -N job_060216_e3200_i500_subtr_40_shape2.0_inh3_1227 -l d_rt=36000 -b y -cwd -V 'python simulate_place_cell_subtr_inh_shape_inh.py 40 3200 500 3 2.0 1227'
qsub -N job_060216_e3200_i500_subtr_40_shape2.0_inh3_1228 -l d_rt=36000 -b y -cwd -V 'python simulate_place_cell_subtr_inh_shape_inh.py 40 3200 500 3 2.0 1228'
qsub -N job_060216_e3200_i500_subtr_40_shape2.0_inh3_1229 -l d_rt=36000 -b y -cwd -V 'python simulate_place_cell_subtr_inh_shape_inh.py 40 3200 500 3 2.0 1229'
qsub -N job_060216_e800_i500_subtr_60_density_shape1.0_inh3_1820 -l d_rt=36000 -b y -cwd -V 'python simulate_place_cell_subtr_inh_density_shape_inh.py 60 800 500 3 1.0 1820'
qsub -N job_060216_e800_i500_subtr_60_density_shape1.0_inh3_1821 -l d_rt=36000 -b y -cwd -V 'python simulate_place_cell_subtr_inh_density_shape_inh.py 60 800 500 3 1.0 1821'
qsub -N job_060216_e800_i500_subtr_60_density_shape1.0_inh3_1822 -l d_rt=36000 -b y -cwd -V 'python simulate_place_cell_subtr_inh_density_shape_inh.py 60 800 500 3 1.0 1822'
qsub -N job_060216_e800_i500_subtr_60_density_shape1.0_inh3_1823 -l d_rt=36000 -b y -cwd -V 'python simulate_place_cell_subtr_inh_density_shape_inh.py 60 800 500 3 1.0 1823'
qsub -N job_060216_e800_i500_subtr_60_density_shape1.0_inh3_1824 -l d_rt=36000 -b y -cwd -V 'python simulate_place_cell_subtr_inh_density_shape_inh.py 60 800 500 3 1.0 1824'
qsub -N job_060216_e800_i500_subtr_60_density_shape1.0_inh3_1825 -l d_rt=36000 -b y -cwd -V 'python simulate_place_cell_subtr_inh_density_shape_inh.py 60 800 500 3 1.0 1825'
qsub -N job_060216_e800_i500_subtr_60_density_shape1.0_inh3_1826 -l d_rt=36000 -b y -cwd -V 'python simulate_place_cell_subtr_inh_density_shape_inh.py 60 800 500 3 1.0 1826'
qsub -N job_060216_e800_i500_subtr_60_density_shape1.0_inh3_1827 -l d_rt=36000 -b y -cwd -V 'python simulate_place_cell_subtr_inh_density_shape_inh.py 60 800 500 3 1.0 1827'
qsub -N job_060216_e800_i500_subtr_60_density_shape1.0_inh3_1828 -l d_rt=36000 -b y -cwd -V 'python simulate_place_cell_subtr_inh_density_shape_inh.py 60 800 500 3 1.0 1828'
qsub -N job_060216_e800_i500_subtr_60_density_shape1.0_inh3_1829 -l d_rt=36000 -b y -cwd -V 'python simulate_place_cell_subtr_inh_density_shape_inh.py 60 800 500 3 1.0 1829'
qsub -N job_060216_e800_i500_subtr_80_density_shape0.5_inh3_2420 -l d_rt=36000 -b y -cwd -V 'python simulate_place_cell_subtr_inh_density_shape_inh.py 80 800 500 3 0.5 2420'
qsub -N job_060216_e800_i500_subtr_80_density_shape0.5_inh3_2421 -l d_rt=36000 -b y -cwd -V 'python simulate_place_cell_subtr_inh_density_shape_inh.py 80 800 500 3 0.5 2421'
qsub -N job_060216_e800_i500_subtr_80_density_shape0.5_inh3_2422 -l d_rt=36000 -b y -cwd -V 'python simulate_place_cell_subtr_inh_density_shape_inh.py 80 800 500 3 0.5 2422'
qsub -N job_060216_e800_i500_subtr_80_density_shape0.5_inh3_2423 -l d_rt=36000 -b y -cwd -V 'python simulate_place_cell_subtr_inh_density_shape_inh.py 80 800 500 3 0.5 2423'
qsub -N job_060216_e800_i500_subtr_80_density_shape0.5_inh3_2424 -l d_rt=36000 -b y -cwd -V 'python simulate_place_cell_subtr_inh_density_shape_inh.py 80 800 500 3 0.5 2424'
qsub -N job_060216_e800_i500_subtr_80_density_shape0.5_inh3_2425 -l d_rt=36000 -b y -cwd -V 'python simulate_place_cell_subtr_inh_density_shape_inh.py 80 800 500 3 0.5 2425'
qsub -N job_060216_e800_i500_subtr_80_density_shape0.5_inh3_2426 -l d_rt=36000 -b y -cwd -V 'python simulate_place_cell_subtr_inh_density_shape_inh.py 80 800 500 3 0.5 2426'
qsub -N job_060216_e800_i500_subtr_80_density_shape0.5_inh3_2427 -l d_rt=36000 -b y -cwd -V 'python simulate_place_cell_subtr_inh_density_shape_inh.py 80 800 500 3 0.5 2427'
qsub -N job_060216_e800_i500_subtr_80_density_shape0.5_inh3_2428 -l d_rt=36000 -b y -cwd -V 'python simulate_place_cell_subtr_inh_density_shape_inh.py 80 800 500 3 0.5 2428'
qsub -N job_060216_e800_i500_subtr_80_density_shape0.5_inh3_2429 -l d_rt=36000 -b y -cwd -V 'python simulate_place_cell_subtr_inh_density_shape_inh.py 80 800 500 3 0.5 2429'
qsub -N job_060216_e800_i500_subtr_70_density_shape2.0_inh3_2120 -l d_rt=36000 -b y -cwd -V 'python simulate_place_cell_subtr_inh_density_shape_inh.py 70 800 500 3 2.0 2120'
qsub -N job_060216_e800_i500_subtr_70_density_shape2.0_inh3_2121 -l d_rt=36000 -b y -cwd -V 'python simulate_place_cell_subtr_inh_density_shape_inh.py 70 800 500 3 2.0 2121'
qsub -N job_060216_e800_i500_subtr_70_density_shape2.0_inh3_2122 -l d_rt=36000 -b y -cwd -V 'python simulate_place_cell_subtr_inh_density_shape_inh.py 70 800 500 3 2.0 2122'
qsub -N job_060216_e800_i500_subtr_70_density_shape2.0_inh3_2123 -l d_rt=36000 -b y -cwd -V 'python simulate_place_cell_subtr_inh_density_shape_inh.py 70 800 500 3 2.0 2123'
qsub -N job_060216_e800_i500_subtr_70_density_shape2.0_inh3_2124 -l d_rt=36000 -b y -cwd -V 'python simulate_place_cell_subtr_inh_density_shape_inh.py 70 800 500 3 2.0 2124'
qsub -N job_060216_e800_i500_subtr_70_density_shape2.0_inh3_2125 -l d_rt=36000 -b y -cwd -V 'python simulate_place_cell_subtr_inh_density_shape_inh.py 70 800 500 3 2.0 2125'
qsub -N job_060216_e800_i500_subtr_70_density_shape2.0_inh3_2126 -l d_rt=36000 -b y -cwd -V 'python simulate_place_cell_subtr_inh_density_shape_inh.py 70 800 500 3 2.0 2126'
qsub -N job_060216_e800_i500_subtr_70_density_shape2.0_inh3_2127 -l d_rt=36000 -b y -cwd -V 'python simulate_place_cell_subtr_inh_density_shape_inh.py 70 800 500 3 2.0 2127'
qsub -N job_060216_e800_i500_subtr_70_density_shape2.0_inh3_2128 -l d_rt=36000 -b y -cwd -V 'python simulate_place_cell_subtr_inh_density_shape_inh.py 70 800 500 3 2.0 2128'
qsub -N job_060216_e800_i500_subtr_70_density_shape2.0_inh3_2129 -l d_rt=36000 -b y -cwd -V 'python simulate_place_cell_subtr_inh_density_shape_inh.py 70 800 500 3 2.0 2129'