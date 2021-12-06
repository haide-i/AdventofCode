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
f = open('./data/day4.csv')
draw = True
boards = {}
enum_one = -1
enum_two = 0
nr_of_boards = 0
for line in f.readlines():
    if line == '\n':
        nr_of_boards += 1

boards = np.zeros((nr_of_boards, 5, 5))
f = open('./data/day4.csv')

for line in f.readlines():
    if draw:
        bingo_input = np.fromstring(line, dtype=int, sep=',')
        draw = False
    else:
        if line=='\n':
            enum_two = 0
            enum_one += 1
        else:
            line = line.rstrip('\n').lstrip(' ')
            boards[enum_one, enum_two, :] = np.fromstring(line, dtype=int, sep=' ')
            enum_two += 1
# -

# # Part 1

# +
bingo_boards = np.copy(boards).astype(float)

for number in bingo_input:
    bingo_boards[bingo_boards==number] = 0
    rows = np.count_nonzero(bingo_boards, axis=1)
    columns = np.count_nonzero(bingo_boards, axis=2)
    if (np.any(rows==0)):
        final_number = number
        idx = np.where(rows==0)[0]
        break
    elif (np.any(columns==0)):
        final_number = number
        idx = np.where(columns==0)[0]
        break
result = final_number * np.sum(bingo_boards[idx][:][:])
print(result)
# -

# # Part 2

# +
standing_boards = np.copy(boards).astype(float)

for number in bingo_input:
    rm = False
    standing_boards[standing_boards==number] = 0
    rows = np.count_nonzero(standing_boards, axis=1)
    columns = np.count_nonzero(standing_boards, axis=2)
    if (np.any(rows==0)):
        idx = np.where(rows==0)[0]
        rm = True
    elif (np.any(columns==0)):
        final_number = number
        idx = np.where(columns==0)[0]
        rm = True
    if rm:
        if np.shape(standing_boards)[0]==1:
            final_number = number
            break
        else:
            standing_boards = np.delete(standing_boards, obj=idx, axis=0)
    
print(final_number, standing_boards)
result = final_number * np.sum(standing_boards)
print(result)
