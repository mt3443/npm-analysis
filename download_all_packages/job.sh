#!/bin/bash

#SBATCH -N 40
#SBATCH -n 40
#SBATCH -c 2
#SBATCH -t 48:00:00
#SBATCH --mem-per-cpu=2G
#SBATCH -J npm-download
#SBATCH -o slurm-%j.out

srun -N1 -n1 -c2 -w l000 python3 package_downloader.py l000 2 &
srun -N1 -n1 -c2 -w l001 python3 package_downloader.py l001 2 &
srun -N1 -n1 -c2 -w l002 python3 package_downloader.py l002 2 &
srun -N1 -n1 -c2 -w l003 python3 package_downloader.py l003 2 &
srun -N1 -n1 -c2 -w l004 python3 package_downloader.py l004 2 &
srun -N1 -n1 -c2 -w l005 python3 package_downloader.py l005 2 &
srun -N1 -n1 -c2 -w l006 python3 package_downloader.py l006 2 &
srun -N1 -n1 -c2 -w l007 python3 package_downloader.py l007 2 &
srun -N1 -n1 -c2 -w l008 python3 package_downloader.py l008 2 &
srun -N1 -n1 -c2 -w l009 python3 package_downloader.py l009 2 &
srun -N1 -n1 -c2 -w l010 python3 package_downloader.py l010 2 &
srun -N1 -n1 -c2 -w l011 python3 package_downloader.py l011 2 &
srun -N1 -n1 -c2 -w l012 python3 package_downloader.py l012 2 &
srun -N1 -n1 -c2 -w l013 python3 package_downloader.py l013 2 &
srun -N1 -n1 -c2 -w l014 python3 package_downloader.py l014 2 &
srun -N1 -n1 -c2 -w l015 python3 package_downloader.py l015 2 &
srun -N1 -n1 -c2 -w l016 python3 package_downloader.py l016 2 &
srun -N1 -n1 -c2 -w l017 python3 package_downloader.py l017 2 &
srun -N1 -n1 -c2 -w l018 python3 package_downloader.py l018 2 &
srun -N1 -n1 -c2 -w l019 python3 package_downloader.py l019 2 &
srun -N1 -n1 -c2 -w l020 python3 package_downloader.py l020 2 &
srun -N1 -n1 -c2 -w l021 python3 package_downloader.py l021 2 &
srun -N1 -n1 -c2 -w l022 python3 package_downloader.py l022 2 &
srun -N1 -n1 -c2 -w l023 python3 package_downloader.py l023 2 &
srun -N1 -n1 -c2 -w l024 python3 package_downloader.py l024 2 &
srun -N1 -n1 -c2 -w l025 python3 package_downloader.py l025 2 &
srun -N1 -n1 -c2 -w l026 python3 package_downloader.py l026 2 &
srun -N1 -n1 -c2 -w l027 python3 package_downloader.py l027 2 &
srun -N1 -n1 -c2 -w l028 python3 package_downloader.py l028 2 &
srun -N1 -n1 -c2 -w l029 python3 package_downloader.py l029 2 &
srun -N1 -n1 -c2 -w l030 python3 package_downloader.py l030 2 &
srun -N1 -n1 -c2 -w l031 python3 package_downloader.py l031 2 &
srun -N1 -n1 -c2 -w l032 python3 package_downloader.py l032 2 &
srun -N1 -n1 -c2 -w l033 python3 package_downloader.py l033 2 &
srun -N1 -n1 -c2 -w l034 python3 package_downloader.py l034 2 &
srun -N1 -n1 -c2 -w l035 python3 package_downloader.py l035 2 &
srun -N1 -n1 -c2 -w l036 python3 package_downloader.py l036 2 &
srun -N1 -n1 -c2 -w l037 python3 package_downloader.py l037 2 &
srun -N1 -n1 -c2 -w l038 python3 package_downloader.py l038 2 &
srun -N1 -n1 -c2 -w l039 python3 package_downloader.py l039 2 &
wait
