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


def find_nr(data):
    one = []
    two = []
    for i in data:
        for j in data:
            for k in data:
                if (i+j+k) == 2020:
                    return i, j, k


path = Path.cwd()
data = np.loadtxt(path / 'day1_data.txt')
i, j, k = find_nr(data)
print(i, j, k, i*j*k)
