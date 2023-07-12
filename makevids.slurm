#!/bin/bash

#SBATCH --job-name=vids
#SBATCH --time='120:00:00'
#SBATCH --ntasks=1

dir='/local/home/iskander/ophiolites/pics'
savedir='/local/home/iskander/ophiolites/vids'
N=$(find $dir -mindepth 1 -maxdepth 1 -type d | wc -l)
echo Number of Folders : $N
echo and they are : $(find $dir -mindepth 1 -maxdepth 1 -type d)
# run LaMEM:
mpiexec -n $N python3 /local/home/iskander/scripts/makevidsmpi/makevids.py $dir $savedir
