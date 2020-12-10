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

# +
import numpy as np

adapter = np.genfromtxt('data/day10_data.csv', delimiter='\n')
adapter = np.append(adapter, 0)
adapter = np.sort(adapter)
adapter = np.append(adapter, adapter[-1]+3)
# -

differences = np.diff(adapter)
jolts, idxs, counts = np.unique(differences, return_counts=True, return_inverse=True)
occ = dict(zip(jolts, counts))
occ[1.0] * occ[3.0]

# ## Part 2

threes = np.where(differences == 3.)
ones = []
first = -1
for pos in threes[0]:
    ones.append(pos-first-2)
    first = pos
ones

combs = 1
for i in ones:
    if i == 1:
        combs = combs*2
    if i == 2:
        combs = combs*(2**2)
    if i == 3:
        combs = combs*(2**3-1)
print(combs)
