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
import matplotlib.pyplot as plt


# ## Part 1

# +
def get_coord(wire):
    start = [0, 0]
    coord = [[0, 0]]
    for cmd in wire:
        d = cmd[0]
        diff = int(cmd[1:])
        for j in range(1, diff+1):
            if d == 'R':
                start[0] += 1
            elif d == 'L':
                start[0] -= 1
            elif d == "U":
                start[1] += 1
            elif d == 'D':
                start[1] -= 1
            coord.append(start.copy())
    return coord

def get_intersect(a, b):
    for (point1, point2) in combinations((a, b), 2):
        print(point1, point2)
    pass


# + tags=[]
f = open('./data/day3_data.csv')
lines = f.readlines()
wire_a = lines[0].split(',')
wire_b = lines[1].split(',')
coord_a = get_coord(wire_a)
coord_b = get_coord(wire_b)
coord_a
tuple_a = set(map(tuple, coord_a))
tuple_b = set(map(tuple, coord_b))
# -

x_a = [i[0] for i in coord_a]
y_a = [i[1] for i in coord_a]
x_b = [i[0] for i in coord_b]
y_b = [i[1] for i in coord_b]
plt.plot(x_a, y_a, '-r', label="Wire A")
plt.plot(x_b, y_b, '-b', label="Wire B")
plt.legend()
plt.show()

sect = tuple_a.intersection(tuple_b)
dist = 100000
for (a, b) in sect:
    if (abs(a) + abs(b)) < dist:
        dist = abs(a)+abs(b)
        print(a, b, dist)


# ## Part 2

steps_a = 0
steps_b = 0
total = 10000000000000
for (a, b) in sect:
    steps_a = 0
    steps_b = 0
    for idx, j in enumerate(coord_a):
        if idx != 0:
            if (j[0] != a) or (j[1] != b):
                steps_a += abs(j[0] - coord_a[idx-1][0]) + abs(j[1] - coord_a[idx-1][1])
                # print(j[0], j[1], steps_a)
            else:
                break
    for idx, j in enumerate(coord_b):
        if idx != 0:
            if (j[0] != a) or (j[1] != b):
                steps_b += abs(j[0] - coord_b[idx-1][0]) + abs(j[1] - coord_b[idx-1][1])
                # print(j[0], j[1], steps_b)
            else:
                break
    # print(a, b, steps_a+steps_b+2)
    if (steps_a+steps_b+2) < total:
        total = (steps_a+steps_b+2)
        print(a, b, total, steps_a, steps_b)

