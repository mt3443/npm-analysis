import os
import sys

node = sys.argv[1]
n_threads = int(sys.argv[2])

os.system('rm -rf /dev/shm/npm')
os.system('mkdir -p /dev/shm/npm/transitive')
os.system('mkdir -p /dev/shm/npm/data')
os.system('mv /users/m139t745/npm-analysis/typosquatting/typosquatting_transitive.js /dev/shm/npm/transitive')
os.system('mv /users/m139t745/npm-analysis/data/downloads.csv /dev/shm/npm/data')
os.system('node /dev/shm/npm/transitive/typosquatting_transitive.js')
os.system('mv /dev/shm/npm/transitive/positive /volatile/m139t745/transitive_output/positive/{}'.format(node))
os.system('rm -rf /dev/shm/npm')
