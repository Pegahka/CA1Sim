__author__ = 'milsteina'
from ipyparallel import Client
import sys
"""
Tests to see if engines are accessible across multiple nodes (16 cores per node) without an MPI backend on the
Stanford Sherlock cluster.
Assumes a controller is already running in another process with:
ipcluster start -n num_cores
"""

if len(sys.argv) > 1:
    cluster_id = sys.argv[1]
    c = Client(cluster_id=cluster_id)
else:
    c = Client()

print c.ids