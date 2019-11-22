import random
import os

malicious = list(range(39))
benign = list(range(7201))

test_size = 0.2

malicious_test = random.sample(malicious, int(len(malicious) * test_size))
benign_test = random.sample(benign, int(len(benign) * test_size))

malicious_train = list(set(malicious) - set(malicious_test))
benign_train = list(set(benign) - set(benign_test))

os.mkdir('train')
os.mkdir('test')

os.mkdir('train/benign')
os.mkdir('train/malicious')

os.mkdir('test/benign')
os.mkdir('test/malicious')

for i in malicious_train:
    os.system('cp malicious/{} train/malicious'.format(i))

for i in malicious_test:
    os.system('cp malicious/{} test/malicious'.format(i))

for i in benign_train:
    os.system('cp benign/{} train/benign'.format(i))

for i in benign_test:
    os.system('cp benign/{} test/benign'.format(i))