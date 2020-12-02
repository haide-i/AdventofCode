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
from itertools import combinations
import time

# ## Part 1

# +
data = np.loadtxt('./data/day2_data.csv', delimiter=',', dtype='int')

def opcode(data, noun, verb):
    cp_data = np.copy(data)
    cp_data[1] = noun
    cp_data[2] = verb
    op = np.arange(0, len(cp_data), 4)
    for i in op[:-1]:
        if cp_data[i] == 99:
            return cp_data
        elif cp_data[i] == 1:
            cp_data[cp_data[i+3]] = cp_data[cp_data[i+1]] + cp_data[cp_data[i+2]]
        elif cp_data[i] == 2:
            cp_data[cp_data[i+3]] = cp_data[cp_data[i+1]] * cp_data[cp_data[i+2]]
    return cp_data

print(opcode(data, 12, 2)[0])
# -

# ## Part 2

# + tags=[]
noun = np.arange(0, 100, 1)
verb = np.arange(0, 100, 1)
noun = np.append(noun, verb)
start = time.time()
for (a, b) in combinations(noun, 2):
    if opcode(data, a, b)[0] == 19690720.:
        print(a, b)
end = time.time()
print(start-end)
start = time.time()
for i in noun:
    for j in verb:
        if opcode(data, i, j)[0] == 19690720:
            print(i, j)
            print(100*i+j)
end = time.time()
print(start-end)

