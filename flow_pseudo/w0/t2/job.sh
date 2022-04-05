#!/bin/bash
cd /Users/gmatteo/git_repos/H_pseudo/flow_pseudo/w0/t2
# OpenMp Environment
export OMP_NUM_THREADS=1
# Commands before execution
ulimit -n 2048
source ~/env.sh

mpirun  -n 1 abinit < /Users/gmatteo/git_repos/H_pseudo/flow_pseudo/w0/t2/run.files > /Users/gmatteo/git_repos/H_pseudo/flow_pseudo/w0/t2/run.log 2> /Users/gmatteo/git_repos/H_pseudo/flow_pseudo/w0/t2/run.err
