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
from pathlib import Path
from itertools import combinations
import time


def find_2(data):
    for i in combinations(data, 3):
        if (i[0] + i[1] + i[2]) == 2020:
            return i, i[0]*i[1]*i[2]


# + tags=[]
path = Path.cwd()
data = np.loadtxt(path / 'data' / 'day1_data.txt')
l, m = find_2(data)
print(l, m)
