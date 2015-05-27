#!/bin/bash
#cd $HOME/PycharmProjects/NEURON/
cd $HOME/CA1Sim
ipcluster start -n 32 --profile-dir=$HOME/.ipython/profile_default &
sleep 60
python parallel_rinp_controller.py
ipcluster stop --profile-dir=$HOME/.ipython/profile_default