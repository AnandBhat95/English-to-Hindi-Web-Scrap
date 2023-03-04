import os
import json
x = (os.listdir())
z = [i for i in x if i.startswith('zzz')]

for i in z:
    with open('textfile.txt','a') as f:
        f.write('./'+i+'\n')
