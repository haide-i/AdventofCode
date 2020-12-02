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

# ## Part 1

data = np.loadtxt('./data/day1_data.csv')
fuel = np.floor(data/3.) -2.
total = fuel.sum()
print(total)


# ## Part 2

# +
def calc_fuel(x, y):
    y = np.floor(y/3.)
    if y > 2:
        y = y - 2
        x = x + y
        return calc_fuel(x, y)
    else:
        return x

total = 0
for i in data:
    total += calc_fuel(0, i)
print(total)

