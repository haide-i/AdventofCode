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
import pandas as pd

# ## Part 1

# + tags=[]
df = pd.read_csv('./data/day2_data.csv', header=None, names=['start', 'end', 'letter', 'password'], sep=' |: |-')
count = 0
df['letter'] = df.letter.apply(lambda x: set(list(x)))
df['new_pwd'] = df.password.apply(lambda x: set(list(x)))
df['occ'] = df.new_pwd - df.letter

# + tags=[]
f = open('./data/day2_data.csv')
count = 0
for line in f:
    line = line.rstrip('\n')
    line = line.replace('-', ' ')
    line = line.replace(': ', ' ')
    lst = line.split()
    if int(lst[0]) <= lst[-1].count(lst[2]) <= int(lst[1]):
        print(lst)
        count += 1
print(count)
# -

# ## Part 2

# + tags=["outputPrepend"]
f = open('./data/day2_data.csv')
count = 0
for i, line in enumerate(f):
    line = line.rstrip('\n')
    line = line.rstrip('\n')
    line = line.replace('-', ' ')
    line = line.replace(': ', ' ')
    lst = line.split()
    if len(lst[-1])>=int(lst[1]):
        if ((lst[-1][int(lst[0])-1] == lst[2]) != (lst[-1][int(lst[1])-1] == lst[2])):
            print(lst[2], lst[-1][int(lst[0])-1], lst[-1][int(lst[1])-1])
            print(lst)
            count+=1
    else:
        if (lst[-1][int(lst[0])-1] == lst[2]):
            print(lst[2], lst[-1][int(lst[0])-1])
            print(lst)
            count+=1
print(count)
