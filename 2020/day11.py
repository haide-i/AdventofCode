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
def seat_to_number(x):
    if x == '.':
        return -1 #no seat
    if x == 'L':
        return 1 #not occupied
    if x == '#':
        return 0 #occupied


# + tags=[]
def change_occ(seats):
    new_seats = np.copy(seats)
    for row in range(len(seats)):
        start_row, end_row = row-1, row+2
        if row == 0:
            start_row = 0
        if row == len(seats):
            end_row = len(seats)
        for col in range(len(seats[0])):
            curr = seats[row][col]
            start_col, end_col = col-1, col+2
            if col == 0:
                start_col = 0
            if col == len(seats[0]):
                end_col = len(seats[0])
            surround = seats[start_row:end_row,start_col:end_col]
            status, counts = np.unique(surround, return_counts=True)
            nbrs = dict(zip(status, counts))
            if (curr == 1) and 0 not in nbrs.keys():
                new_seats[row][col] = 0
            elif (curr == 0) and (nbrs[0] >= 5):
                new_seats[row][col] = 1
    return new_seats

f = open('data/dummy.csv')
seatmap = []
for line in f:
    line = line.rstrip('\n')
    seatmap.append(list(line))
seats = np.asarray([(list(map(seat_to_number, i))) for i in seatmap])
new = seats
for i in range(1000):
    changed_seats = change_occ(new)
    if (new == changed_seats).all():
        print(i, 'end')
        break
    else:
        new = np.copy(changed_seats)
occupied = np.size(changed_seats) - np.count_nonzero(changed_seats)
print(occupied)
# -

# ## Part 2

# + tags=[]
f = open('data/day11_data.csv')
seatmap = []
for line in f:
    line = line.rstrip('\n')
    seatmap.append(list(line))
seats_map = np.asarray([(list(map(seat_to_number, i))) for i in seatmap])

coord_list = [[-1, -1], [-1, 0], [1, 0], [0, 1], [0, -1], [1, 1], [-1, 1], [1, -1]]

def check_surroundings(seats, row, col, coord_list):
    x_range, y_range = np.arange(0, seats.shape[0], 1), np.arange(0, seats.shape[1], 1)
    curr = seats[row][col]
    if curr == -1:
        return curr
    count = 0
    for dx, dy in coord_list:
        n_x, n_y = row+dx, col+dy
        while (0<=n_x<(len(seats))) and (0<=n_y<(len(seats[0]))) and (seats[n_x][n_y]==-1):
            n_x, n_y = n_x+dx, n_y+dy
        if (n_x in x_range) and (n_y in y_range) and seats[n_x][n_y] == 0:
            count += 1
    if (curr == 1) and (count == 0):
        return 0
    elif (curr == 0) and (count >= 5):
        return 1
    else:
        return curr
def get_new_map(seats, coord_list):
    new_seats = np.copy(seats)
    for row in range(seats.shape[0]):
        for col in range(seats.shape[1]):
            new_seats[row][col] = check_surroundings(seats, row, col, coord_list)
    return new_seats

before = np.random.randn(seats_map.shape[0], seats_map.shape[1])

while not (before==seats_map).all():
    before = seats_map
    seats_map = get_new_map(before, coord_list)
occupied = np.size(seats_map) - np.count_nonzero(seats_map)
print(occupied)
