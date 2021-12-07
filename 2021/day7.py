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

f = open('./data/day7.csv')
data = np.array(f.read().rstrip('\n').split(',')).astype(int)
positions = np.arange(np.min(data), np.max(data))

# # Part 1

differences = []
for i in positions:
    diff = np.sum(np.abs(data - i))
    differences.append(diff)
differences = np.array(differences)
print(np.argmin(differences), np.min(differences))

# # Part 2

differences = []
for i in positions:
    diff = np.abs(data - i)
    diff = np.sum((diff**2 + diff)/2.)
    differences.append(diff)
differences = np.array(differences)
print(np.argmin(differences), np.min(differences))
