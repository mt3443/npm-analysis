#!/bin/bash

#SBATCH -p intel
#SBATCH -N 1
#SBATCH -n 1
#SBATCH -c 1
#SBATCH -t 99:00:00
#SBATCH --mem-per-cpu=4096
#SBATCH -J npm-download
#SBATCH -o slurm-%j.out

srun -N 1 -n 1 --mem=4096 python3 download_packages.py &
wait
