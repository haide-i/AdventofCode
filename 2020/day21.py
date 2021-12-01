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

from collections import Counter

# + tags=[]
f = open('data/day21_data.csv')
allergens = {}
all_ingredients = []
for line in f:
    ingr, aller = line.rstrip('\n').split('(')
    ingredients = ingr.rstrip(' ').split(' ')
    all_ingredients += ingredients
    aller = aller.replace('contains ', '').replace(' ', '').replace(')', '').split(',')
    for key in aller:
        if key in allergens.keys():
            allergens[key] = allergens[key].intersection(set(ingredients))
        else:
            allergens[key] = set(ingredients)
still_long = True
while still_long:
    still_long = False
    for key, item in allergens.items():
        if len(list(item))==1:
            for scd, scd_item in allergens.items():
                if scd!=key:
                    allergens[scd] = scd_item - item
        else:
            still_long = True

count = dict(Counter(all_ingredients))
for item in allergens.values():
    count.pop(list(item)[0])
total = 0
for item in count.values():
    total += item
print(total)
# -

# ## Part 2

cdil = ''
for entry in sorted(list(allergens.keys())):
    cdil += str(list(allergens[entry])[0]) + ','
cdil = cdil.rstrip(',')
print(cdil)
