#!/bin/bash
#cd $HOME/PycharmProjects/NEURON/
cd $HOME/CA1Sim
cluster_id="$1"
ipcluster start -n 31 --profile-dir=$HOME/.ipython/profile_default --cluster-id=$cluster_id &
#ipcluster start -n 8 --profile-dir=$HOME/.ipython/profile_default &
#ipcluster start -n 16 --profile-dir=$HOME/.ipython/profile_default &
sleep 120
#python parallel_clustered_branch_cooperativity_nmda_controller.py
python parallel_optimize_branch_cooperativity_nmda_kin3_controller.py $cluster_id
ipcluster stop --profile-dir=$HOME/.ipython/profile_default --cluster-id=$cluster_id