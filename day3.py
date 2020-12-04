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

import numpy as np


def nr_trees(data, right_step, down_step):
    lines = data
    nr_lines = len(lines)
    line_length = len(list(lines[0].rstrip('\n')))
    idx = 0
    trees = 0
    no_tree = 0
    rows = np.arange(0, nr_lines, down_step)
    for i in rows[1:]:
        idx += right_step
        if idx >= line_length:
            idx = idx - line_length
        if list(lines[i])[idx] == '#':
            trees += 1
        else:
            no_tree += 1
    print(trees)
    return trees, no_tree


f = open('./data/day3_data.csv')
data = f.readlines()
print(nr_trees(data, 3, 1))

# ## Part 2

one = (1, 1)
two = (3, 1)
three = (5, 1)
four = (7, 1)
five = (1, 2)
print(nr_trees(data, *one)[0]*nr_trees(data, *two)[0]*nr_trees(data, *three)[0]*nr_trees(data, *four)[0]*nr_trees(data, *five)[0])


