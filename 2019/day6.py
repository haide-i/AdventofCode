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

import numpy as np


def suborbits(planet, orbdir):
    if planet in orbdir:
        for subplanets in orbdir[planet]:
            return 1 + suborbits(subplanets, orbdir)
    else:
        return 0


# ## Part 1

# + tags=[]
f = open('./data/dummy.csv')
lines = f.readlines()
orbit_dir = {}
for i in lines:
    i = i.rstrip('\n')
    planets = i.split(')')
    if planets[1] in orbit_dir:
        orbit_dir[planets[1]].append(planets[0])
    else:
        orbit_dir[planets[1]] = [planets[0]]
nr_orbits = 0
for key, orbits in orbit_dir.items():
    nr_orbits += suborbits(key, orbit_dir)
nr_orbits


# -

# ## Part 2 

# +
def get_orbit(value, orbdir):
    keys = []
    for key, val in orbdir.items():
        if value in val:
            keys.append(key)
    return keys

def find_santa(key, orbdir):
    planets = []
    print(key)
    if key in orbdir:
        for p in orbdir[key]:
            planets.append(p)
        print(planets)
    planets.append(get_orbit(key, orbdir))
    if 'SAN' in planets:
        return 1
    else:
        for i in planets:
            return 1 + find_santa(i, orbdir)


# -

find_santa('YOU', orbit_dir)
