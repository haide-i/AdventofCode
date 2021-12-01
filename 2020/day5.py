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
#     name: python3
# ---

# ## Part 1

# + tags=[]
import numpy as np

def get_row(ticket, rows):
    if ticket[0] == 'F' or ticket[0] == 'L':
        rows, _ = np.split(rows, 2)
    else:
        _, rows = np.split(rows, 2)
    if len(rows) > 1:
        return get_row(ticket[1:], rows)
    elif len(rows) == 1:
        return rows[0]

all_rows = np.arange(0, 128, 1)
all_columns = np.arange(0, 8, 1)
highest_id = 0
f = open('data/day5_data.csv')
seats = []
seat_ids = []
for line in f:
    line = line.rstrip('\n')
    row = get_row(line[:7], all_rows)
    column = get_row(line[7:], all_columns)
    seat_id = row*8 + column
    if seat_id > highest_id:
        highest_id = seat_id
    seat_ids.append(seat_id)
    seats.append([row, column, seat_id])
print(highest_id)

# -

# ## Part 2

seat_ids = np.array(seat_ids)
all_seats = np.arange(0, highest_id, 1)
possible = np.setdiff1d(all_seats, seat_ids)
for s in possible:
    if ((s+1) in seat_ids) & ((s-1) in seat_ids):
        print(s)
