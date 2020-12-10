# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:light
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.6.0
#   kernelspec:
#     display_name: Python 3
#     name: python3
# ---

# ## Part 1

import numpy as np
from itertools import combinations
def find_summands(data, idx, steps=25):
    possible = data[idx-steps:idx]
    for i in combinations(possible, 2):
        i = list(i)
        if (i[0]+i[1]) == data[idx]:
            return find_summands(data, idx+1, steps=steps)
    return data[idx]


numbers = np.genfromtxt('data/day9_data.csv', delimiter='\n')
break_number = find_summands(numbers, 25, steps=25)
break_number

# ## Part 2

for i in range(len(numbers)):
    added_numbers = np.cumsum(numbers[i:])
    if break_number in added_numbers:
        idx = np.where(added_numbers == break_number)
        print(i, idx[0][0])
        print(numbers[i:i+idx[0][0]])
        break

line = numbers[i:i+idx[0][0]+1]
np.amin(line) + np.amax(line)
