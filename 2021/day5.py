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

# +
f = open('./data/day5.csv')
start = []
end = []
for line in f.readlines():
    coords = line.rstrip('\n').split('->')
    start.append(coords[0].replace(' ','').split(','))
    end.append(coords[1].replace(' ','').split(','))
start = np.array(start).astype(int)
end = np.array(end).astype(int)

max_x = np.max(start.T[0]) if np.max(start.T[0]) > np.max(end.T[0]) else np.max(end.T[0])
max_y = np.max(start.T[1]) if np.max(start.T[1]) > np.max(end.T[1]) else np.max(end.T[1])

# -

# # Part 1

grid = np.zeros((max_x+1, max_y+1))
diff = end - start
idxs = np.where(np.all((diff!=0), axis=1))
start_st = np.delete(start, obj=idxs, axis=0)
end_st = np.delete(end, obj=idxs, axis=0)
st_diff = end_st - start_st
nr_of_steps = np.linalg.norm(st_diff, axis=1).astype(int)
st_diff[st_diff>0] = 1
st_diff[st_diff<0] = -1
pos = []
for i in range(len(start_st)):
    for j in range(nr_of_steps[i]+1):
        pos.append(list(start_st[i]+j*st_diff[i]))
for step in pos:
    grid[step[0]][step[1]] += 1
result = len(grid[np.where(grid>1)])
print(result)

# # Part 2

grid = np.zeros((max_x+1, max_y+1))
diff = end - start
nr_of_steps = np.linalg.norm(diff, axis=1).astype(int)
diff[diff>0] = 1
diff[diff<0] = -1
pos = []
for i in range(len(start)):
    for j in range(nr_of_steps[i]+1):
        if np.any((start[i]+j*diff[i])!=end[i]):
            pos.append(list(start[i]+j*diff[i]))
        else:
            pos.append(list(end[i]))
            break
for step in pos:
    grid[step[0]][step[1]] += 1
result = len(grid[np.where(grid>1)])
print(result)
