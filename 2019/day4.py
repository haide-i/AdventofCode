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
import time

# ## Part 1

s = 125730
e = 579381
count = 0
start = time.time()
for i in range(s, e):
    pwd = np.asarray(list(map(int, list(str(i)))))
    diff = np.diff(pwd)
    if np.all((diff >= 0)) & np.any((diff == 0)):
        count += 1
end = time.time()
print(end-start)
print(count)

# ## Part 2

count = 0
start = time.time()
for i in range(s, e):
    pwd = np.asarray(list(map(int, list(str(i)))))
    diff = np.diff(pwd)
    _, counts = np.unique(pwd, return_counts=True)
    if np.all(diff >= 0) & np.any((counts == 2)):
        count += 1
end = time.time()
print(end - start)
print(count)
