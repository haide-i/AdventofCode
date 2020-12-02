# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.6.0
#   kernelspec:
#     display_name: Python 3
#     name: python3
# ---

import numpy as np

# ## Part 1

# + tags=[]
f = open('./data/day2_data.txt')
count = 0
for i, line in enumerate(f):
    line = line.rstrip('\n')
    if line[1] != '-':
        start = int(line[:2])
        idx = 3
    else:
        start = int(line[0])
        idx = 2
    if line[idx+1].isspace():
        end = int(line[idx])
        idx = idx + 2
    else:
        end = int(line[idx:idx+2])
        idx = idx + 3
    letter = line[idx]
    password = line[idx+3:]
    testline = f'{start}-{end} {letter}: {password}'
    occ = password.count(letter)
    if start <= occ <= end:
        #print(i, testline)
        count += 1
print(count)
# -

# ## Part 2

# + tags=[]
f = open('./data/day2_data.txt')
count = 0
for i, line in enumerate(f):
    line = line.rstrip('\n')
    if line[1] != '-':
        start = int(line[:2])
        idx = 3
    else:
        start = int(line[0])
        idx = 2
    if line[idx+1].isspace():
        end = int(line[idx])
        idx = idx + 2
    else:
        end = int(line[idx:idx+2])
        idx = idx + 3
    letter = line[idx]
    password = line[idx+3:]
    testline = f'{start}-{end} {letter}: {password}'
    if len(password)>=end:
        if ((password[start-1] == letter) != (password[end-1] == letter)):
            print(letter, password[start-1], password[end-1])
            print(testline)
            count+=1
    else:
        if (password[start-1] == letter):
            print(letter, password[start-1])
            print(testline)
            count+=1
print(count)
