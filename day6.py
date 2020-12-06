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

# ## Part 1 & 2

# + tags=[]
f = open('data/day6_data.csv')
groups = []
part = 1
alphabet = list('abcdefghijklmnopqrstuvwxyz')
if part == 1:
    group = []
elif part == 2:
    group = alphabet
    first_line = True
for line in f:
    if line == '\n':
        groups.append(group)
        if part == 1:
            group = []
        elif part == 2:
            group = alphabet
    else:
        line = line.rstrip('\n')
        answers = set(list(line))
        if part == 1:
            group += list(answers - set(group))
        if part == 2:
            group = answers.intersection(group)
groups.append(group)
total_answers = 0
for i in groups:
    total_answers += len(i)
print(total_answers)
