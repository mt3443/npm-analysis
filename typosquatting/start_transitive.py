import os
import sys

node = sys.argv[1]
os.system('rm -rf /dev/shm/npm')
os.system('mkdir -p /dev/shm/npm/transitive')
os.system('mkdir /dev/shm/npm/data')
os.system('cp run_transitive.js /dev/shm/npm/transitive')
os.system('cp ../data/typosquatting_candidates.txt /dev/shm/npm/data')
os.system('node run_transitive.js {}'.format(node))
os.system('mv /dev/shm/npm/transitive/positive /users/m139t745/npm-analysis/typosquatting/transitive_output/positive/{}'.format(node))
os.system('mv /dev/shm/npm/transitive/negative /users/m139t745/npm-analysis/typosquatting/transitive_output/negative/{}'.format(node))
os.system('rm -rf /dev/shm/npm')
