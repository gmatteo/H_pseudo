#!/bin/bash

#SBATCH --partition=small
#SBATCH --job-name=w0_t3
#SBATCH --ntasks=32
#SBATCH --mem-per-cpu=2048
#SBATCH --time=0-12:0:0
#SBATCH --account=project_465000061
#SBATCH --output=/pfs/lustrep2/scratch/project_465000061/magianto/H_pseudo/flow_pseudo/w0/t3/queue.qout
#SBATCH --error=/pfs/lustrep2/scratch/project_465000061/magianto/H_pseudo/flow_pseudo/w0/t3/queue.qerr
cd /pfs/lustrep2/scratch/project_465000061/magianto/H_pseudo/flow_pseudo/w0/t3
# OpenMp Environment
export OMP_NUM_THREADS=1
# Commands before execution
source $HOME/git_repos/abinit/_build_gnu/modules.sh

srun  -n 32 abinit --timelimit 0-12:0:0 < /pfs/lustrep2/scratch/project_465000061/magianto/H_pseudo/flow_pseudo/w0/t3/run.files > /pfs/lustrep2/scratch/project_465000061/magianto/H_pseudo/flow_pseudo/w0/t3/run.log 2> /pfs/lustrep2/scratch/project_465000061/magianto/H_pseudo/flow_pseudo/w0/t3/run.err
