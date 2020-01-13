import pandas as pd

all_typosquatting = pd.read_csv('C:\\Users\\Matthew\\Desktop\\a.csv')
known_typosquatting = pd.read_csv('../data/typosquatting_examples.csv')

malicious = list(known_typosquatting.malicious_package_name.values)
a = list(all_typosquatting.package_name.values)

caught = 0
for m in malicious:
    if m in a:
        print('yes')
        caught += 1
    else:
        print('no')

print(caught)