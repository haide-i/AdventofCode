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
#     language: python
#     name: python3
# ---

# ## Part 1

import numpy as np
from itertools import product


# +
def pad_array(data, part):
    if part==1:
        zero_array = np.zeros((np.shape(data)[0]+2, np.shape(data)[1]+2, np.shape(data)[2]+2))
        zero_array[1:-1, 1:-1, 1:-1] = data
    if part==2:
        zero_array = np.zeros((np.shape(data)[0]+2, np.shape(data)[1]+2, np.shape(data)[2]+2, np.shape(data)[3]+2))
        zero_array[1:-1, 1:-1, 1:-1, 1:-1] = data
    return zero_array


def change_occ_3d(data):
    cubes = pad_array(data, part=1)
    new_cubes = cubes.copy()
    positions = product(np.arange(1, np.shape(cubes)[0]-1),
                        np.arange(1, np.shape(cubes)[1]-1),
                        np.arange(1, np.shape(cubes)[2]-1))
    for i, j, k in positions:
        curr = cubes[i][j][k]
        surround = cubes[i-1:i+2,j-1:j+2,k-1:k+2]
        counts = np.count_nonzero(surround) - np.count_nonzero(curr)
        if (curr==0) and (counts==3):
            new_cubes[i][j][k] = 1
        elif (curr == 1) and ((counts<2) | (counts>3)):
            new_cubes[i][j][k] = 0
    return new_cubes

def change_occ_4d(data):
    cubes = pad_array(data, part=2)
    new_cubes = cubes.copy()
    positions = product(np.arange(1, np.shape(cubes)[0]-1),
                        np.arange(1, np.shape(cubes)[1]-1),
                        np.arange(1, np.shape(cubes)[2]-1),
                        np.arange(1, np.shape(cubes)[3]-1))
    for i, j, k, l in positions:
        curr = cubes[i][j][k][l]
        surround = cubes[i-1:i+2,j-1:j+2,k-1:k+2,l-1:l+2]
        counts = np.count_nonzero(surround) - np.count_nonzero(curr)
        if (curr == 0) and (counts==3):
            new_cubes[i][j][k][l] = 1
        elif (curr == 1) and ((counts<2) | (counts>3)):
            new_cubes[i][j][k][l] = 0
    return new_cubes


# + tags=[]

with open('./data/day17_data.csv') as file:
    data = [list(map(int, line.replace('#', '1').replace('.', '0')))
            for line in file.read().split('\n')]
data = np.asarray(data)
data = np.expand_dims(data, axis=0)
part = 2
if part == 1:
    data = pad_array(data, part)
    for i in range(6):
        changed_seats = change_occ_3d(data)
        data = np.copy(changed_seats)

elif part == 2:
    data = np.expand_dims(data, axis=0)
    data = pad_array(data, part)
    for i in range(6):
        changed_seats = change_occ_4d(data)
        data = np.copy(changed_seats)


active = np.count_nonzero(data)
print(active)
