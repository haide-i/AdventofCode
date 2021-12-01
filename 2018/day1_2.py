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

import csv
import requests

f = open('./data/day1.csv')
data = [float(n) for n in f.readlines()]


freq = 0
for i in data:
    freq += i
freq

double = False
freq = 0
freq_list = [0]
while not double:
    for i in data:
        freq += i
        if freq in freq_list:
            double = True
            result = freq
            break
        else:
            freq_list.append(freq)
result
