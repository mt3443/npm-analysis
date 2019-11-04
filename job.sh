#!/bin/bash

#SBATCH -p intel
#SBATCH -N 130
#SBATCH -n 130
#SBATCH -c 1
#SBATCH -t 99:00:00
#SBATCH --mem-per-cpu=4096
#SBATCH -J npm-analysis
#SBATCH -o slurm-%j.out

for i in {0..129}; do
	srun -N1 -n1 --exclusive python3 test_model.py $i &
done
wait
