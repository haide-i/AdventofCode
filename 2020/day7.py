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

def find_outer(inner, bags, tested):
    for i in inner:
        if i not in tested:
            if i in bags.keys():
                inner += find_outer(bags[i], bags, inner)
    return set(inner)



# + tags=[]
import re
f = open('data/day7_data.csv')
bags = {}
for line in f:
    line = line.rstrip('.\n')
    line = line.replace('contain', '')
    line = line.replace(',', '')
    line = line.replace('bags', 'bag')
    line = line.replace(' ', '')
    line = re.sub(r'[0-9]', '', line)
    words = line.split('bag')
    for i in words[1:-1]:
        if i not in bags.keys():
            bags[i] = [words[0]]
        else:
            bags[i].append(words[0])
all_bags = dict.fromkeys(bags.keys(), {})
for key, values in bags.items():
    for i in values:
        if i in bags.keys():
            all_bags[key][i] = bags[i]
our_bag = 'shinygold'
outer_bags = find_outer([our_bag], bags, ['']) - set([our_bag])
print(len(outer_bags))


# -

# ## Part 2

def find_inner(outer, bags):
    total = 0
    for i in outer:
        if i[0].isdigit():
            multiplier = int(i[0])
            i = i[1:]
        else:
            multiplier = 1
        if i in bags.keys():
            values = bags[i]
            for j in values:
                if j != 'noother':
                    total += multiplier*(int(j[0]) + find_inner([j], bags))
    return total


f = open('data/day7_data.csv')
bags = {}
for line in f:
    line = line.rstrip('.\n')
    line = line.replace('contain', '')
    line = line.replace(',', '')
    line = line.replace('bags', 'bag')
    line = line.replace(' ', '')
    words = line.split('bag')
    bags[words[0]] = words[1:-1]
find_inner([our_bag], bags)
