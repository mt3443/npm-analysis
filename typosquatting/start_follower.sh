#!/bin/bash

#SBATCH -p intel
#SBATCH -N 1
#SBATCH -n 1
#SBATCH -c 1
#SBATCH -t 99-00:00:00
#SBATCH -J npm-follower
#SBATCH -o slurm-%j.out

srun -N 1 -n 1 -w g016 node follower.js follower &
wait
