#!/bin/bash

#SBATCH --job-name=mkvids
#SBATCH --time='00:60:00'
#SBATCH --ntasks=1

dir='/local/home/iskander/ophiolites/pics'
savedir='/local/home/iskander/ophiolites/vids'
N=$(find $dir -type f -name '*.png*' | sed -r 's|/[^/]+$||' |sort |uniq |wc -l)
echo Number of Folders : $N
echo and they are : $(find $dir -type f -name '*.png*' | sed -r 's|/[^/]+$||' |sort |uniq)
# run LaMEM:
mpiexec -n $N python3 /local/home/iskander/scripts/makevidsmpi/makevids.py $dir $savedir
