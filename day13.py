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

# +
import math

f = open('data/day13_data.csv')
f = f.readlines()
f[1] = f[1].replace('x,', '')
timestamp = int(f[0])
busnumbers = list(map(int, f[1].split(',')))

wait_time = 10000
chosen_bus = busnumbers[0]
for bus in busnumbers:
    multiplicator = math.ceil(timestamp/bus)
    new_time = bus*multiplicator - timestamp
    if new_time < wait_time:
        wait_time = new_time
        chosen_bus = bus
print(wait_time * chosen_bus)
# -

# ## Part 2

# + tags=[]
import numpy as np
f = open('data/day13_data.csv')
f = f.readlines()
f[1] = f[1].replace('x', '0')
busnumbers = np.asarray(list(map(int, f[1].split(','))), dtype=np.float64)
busses = busnumbers[busnumbers != 0]
minutes = np.nonzero(busnumbers)[0]


# + tags=[]
steps_1 = np.lcm.reduce([23, 431, 13, 19, 41], dtype=np.int64)
steps_2 = np.lcm.reduce([17, 409], dtype=np.int64)

found = False
i = 0
while not found:
    tst = np.count_nonzero((i-23+minutes)%busses)
    if tst == 0:
        timestamp = i - 23
        found = True
    else:
        i = i + steps_1
        while (i+31)%steps_2 != 0:
            i = i+steps_1
print("Timestamp: ", timestamp)
