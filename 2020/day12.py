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

def get_position(inst, pos, facing):
    cmd = inst[0]
    lngth = int(inst[1:])
    steps = 0
    if (cmd == 'F'):
        cmd = facing
    if cmd == 'N':
        pos[1] += lngth
    elif cmd == 'S':
        pos[1] += -lngth
    elif cmd == 'E':
        pos[0] += lngth
    elif cmd == 'W':
        pos[0] += - lngth
    if cmd == 'R':
        steps = int(lngth/90.)
    elif cmd == 'L':
        steps = 4-int(lngth/90.)
    return pos, steps
    


f = open('data/day12_data.csv')
instructions = []
for line in f:
    instructions.append(line.rstrip('\n'))


facings = ['N', 'E', 'S', 'W']
current_pos = [0, 0]
facing_idx = 1
for i in instructions:
    current_pos, steps = get_position(i, current_pos, facings[facing_idx])
    facing_idx = (facing_idx + steps)%4
manhattan_dist = abs(current_pos[0]) + abs(current_pos[1])
print(manhattan_dist)

# ## Part 2

# +
import math
import numpy as np

def rotmat(alpha):
    alpha = alpha * math.pi / 180.
    mat = [[math.cos(alpha), -math.sin(alpha)], [math.sin(alpha), math.cos(alpha)]]
    return mat

def get_waypoint(inst, pos, waypoint):
    cmd = inst[0]
    lngth = int(inst[1:])
    if cmd == 'F':
        pos[0] += lngth*waypoint[0]
        pos[1] += lngth*waypoint[1]
    if cmd == 'N':
        waypoint[1] += lngth
    elif cmd == 'S':
        waypoint[1] += -lngth
    elif cmd == 'E':
        waypoint[0] += lngth
    elif cmd == 'W':
        waypoint[0] += - lngth
    if cmd == 'R':
        waypoint = np.dot(rotmat(-lngth), waypoint)
    elif cmd == 'L':
        waypoint = np.dot(rotmat(lngth), waypoint)
    return pos, waypoint


facings = ['N', 'E', 'S', 'W']
current_pos = [0, 0]
waypoint_pos = [10, 1]
facing_idx = 1
for i in instructions:
    current_pos, waypoint_pos = get_waypoint(i, current_pos, waypoint_pos)
manhattan_dist = abs(current_pos[0]) + abs(current_pos[1])
print(manhattan_dist)
