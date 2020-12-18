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

f = open('data/day15_data.csv')
numbers = f.read().split(',')
tst = 2020
i = len(numbers)
current_number = 0
while (i < tst):
    try:
        index = numbers.index(str(current_number))
        if numbers.count(current_number) == 1:
            new_number = len(numbers) - index
            numbers.append(str(current_number))
        else:
            index = len(numbers) - 1 - numbers[::-1].index(str(current_number))
            new_number = len(numbers) - index
            numbers.append(str(current_number))
    except:
        new_number = 0
        numbers.append(str(current_number))
    current_number = new_number
    i += 1
print(numbers[-1])

# ## Part 2

# + tags=[]
import numpy as np
import time
f = open('data/day15_data.csv')
numbers = f.read().split(',')
numbers = {int(numbers[i]): i for i in range(len(numbers))}
i = len(numbers)
current_number = 0
start = time.time()
while (i < 29999999):
    # print(current_number)
    if current_number in numbers.keys():
        last_index = numbers[current_number]
        new_number = i - last_index
    else:
        new_number = 0
    numbers[current_number] = i
    current_number = new_number
    i+=1

end=time.time()
print(end-start)
print(current_number)
