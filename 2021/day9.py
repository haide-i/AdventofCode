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

f = open('./data/day9.csv')
data = []
for line in f.readlines():
    line = line.rstrip('\n')
    line = [int(l) for l in line]
    data.append(line)
data = np.array(data)


# # Part 1

# +
def check_surroundings(vents, row, col):
    coord_list = [[-1, 0], [1, 0], [0, 1], [0, -1]]
    curr = vents[row][col]
    low = True
    for dx, dy in coord_list:
        n_x, n_y = row+dx, col+dy
        
        if (0<=n_x<(len(vents))) and (0<=n_y<(len(vents[0]))):
            if (vents[n_x][n_y]>curr):
                low = True
            else:
                low = False
                break
    if low:
        return curr+1
    else:
        return 0

low_points = np.copy(data)
for row in range(len(data)):
    for col in range(len(data[0])):
        low_points[row][col] = check_surroundings(data, row, col)

print(np.sum(low_points))


# -

# # Part 2

# +
def check_basins(vents, row, col, idx=[], basin=[]):

    coord_list = [[-1, 0], [1, 0], [0, 1], [0, -1]]

    for dx, dy in coord_list:
        n_x, n_y = row+dx, col+dy
        if (0<=n_x<(len(vents))) and (0<=n_y<(len(vents[0]))):
            if (vents[n_x][n_y]<9):
                if [n_x, n_y] not in idx:
                    basin += [vents[n_x][n_y]]
                    idx.append([n_x, n_y])
                    basin + check_basins(vents, n_x, n_y, idx=idx, basin=basin)
    return basin

row, col = np.where(low_points!=0)

all_basins = []
for i in range(len(row)):
    all_basins.append(check_basins(data, row[i], col[i], basin=[]))

length = [len(x) for x in all_basins]
result = np.prod(np.array(sorted(length)[-3:]))
print(result)
