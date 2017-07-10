#!/bin/bash                                                                                                                                             
#PBS -l nodes=3:ppn=16:xe                                                                                                                               
#PBS -q debug                                                                                                                                           
#PBS -l walltime=00:30:00                                                                                                                               
#PBS -A bafv             
#PBS -N test_ipyparallel_bw                                                                                                                             
#PBS -e test_ipyparallel_bw.$PBS_JOBID.err                                                                                   
#PBS -o test_ipyparallel_bw.$PBS_JOBID.out
### set email notification                                                                                                                            
#PBS -m bea                                                                                                                                             
#PBS -M aaronmil@stanford.edu                                                                                                                           
### Set umask so users in my group can read job stdout and stderr files
#PBS -W umask=0027                                                                                                

module swap PrgEnv-cray PrgEnv-gnu
module load cray-hdf5-parallel
module load bwpy
module load bwpy-mpi                                                                                                                      

export PI_HOME=/projects/sciteam/baef
export LD_LIBRARY_PATH=/sw/bw/bwpy/0.3.0/python-mpi/usr/lib:/sw/bw/bwpy/0.3.0/python-single/usr/lib:$LD_LIBRARY_PATH
export PYTHONPATH=$PI_HOME/bin/nrn/lib/python:$PI_HOME/site-packages:$PYTHONPATH
export PATH=$PI_HOME/bin/nrn/x86_64/bin:$PATH
cd $PBS_O_WORKDIR

set -x
cluster_id="$1"
aprun -n 1 ipcontroller --ip='*' --cluster-id=$cluster_id &
sleep 60
aprun -n 46 ipengine --cluster-id=$cluster_id &
sleep 60
aprun -n 1 python test_ipyparallel.py --cluster-id=$cluster_id
