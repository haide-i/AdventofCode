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

f = open('./data/day6.csv')
data = np.array(f.read().rstrip('\n').split(',')).astype(int)


def count_down(days, count_dict):
    if days==8:
        count_dict[days-1] = count_dict[days]
        return count_dict
    else:
        count_dict[days-1] = count_dict[days]
        return count_down(days+1, count_dict)


# # Part 1 & 2

# +
unique, counts = np.unique(data, return_counts=True)
counts = dict(zip(unique, counts))

for i in range(9):
    if i not in counts:
        counts[i] = 0

for i in range(256):
    respawns = counts[0]
    counts = count_down(1, counts)
    counts[8] = respawns
    counts[6] += respawns
fish = counts.values()
all_fish = sum(fish)
print(all_fish)
