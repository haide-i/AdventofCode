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

f = open('./data/day2.csv')
data = [n.rstrip('\n') for n in f.readlines()]

# # Part 1

# +
depth = 0
hor = 0

for cmd in data:
    if cmd[0]=='f':
        hor += int(cmd[-1])
    else:
        if cmd[0]=='d':
            depth += int(cmd[-1])
        else:
            depth -= int(cmd[-1])

print(depth, hor, depth*hor)
# -

# # Part 2

# +
depth = 0
hor = 0
aim = 0

for cmd in data:
    value = int(cmd[-1])
    if cmd[0]=='f':
        hor += value
        depth += aim * value
    else:
        if cmd[0]=='d':
            aim += value
        else:
            aim -= value
print(depth, hor, depth*hor)
