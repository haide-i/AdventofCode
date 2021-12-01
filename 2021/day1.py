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
#     display_name: 'Python 3.8.5 64-bit (''toy'': conda)'
#     language: python
#     name: python3
# ---

import numpy as np

f = open('./data/day1.csv')
data = np.array([float(n) for n in f.readlines()])

# # Part 1

increases = np.count_nonzero(np.diff(data)>0)
print(increases)

# # Part 2

help_var = np.sum(data[0:3])
increases = 0
for i in range(1, len(data[:-2])):
    curr = np.sum(data[i:i+3])
    if (curr - help_var)>0:
        increases += 1
    help_var = curr
print(increases)
