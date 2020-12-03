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


# ## Part 1 + 2

# +
def pos_im(data, mode, idx):
    if mode == 0:
        return data[data[idx]]
    if mode == 1:
        return data[idx]

def modes(op):
    if len(op) == 1:
        return int(op[0]), 0, 0
    elif len(op) == 4:
        return int(op[-1]), int(op[-3]), int(op[-4])
    elif (len(op) == 3):
        return int(op[-1]), int(op[-3]), 0
    elif (len(op) == 2):
        return int(op[-1]), 0, 0

def opcode(data, i, *input_data):
    op = data[i]
    code, a, b = modes(list(map(int, list(str(op)))))
    if code == 1:
        data[data[i+3]] = pos_im(data, a, i+1) + pos_im(data, b, i+2)
        i += 4
        return opcode(data, i)
    elif code == 2:
        data[data[i+3]] = pos_im(data, a, i+1) * pos_im(data, b, i+2)
        i += 4
        return opcode(data, i)
    elif code == 3:
        data[data[i+1]] = input_data[0]
        i += 2
        return opcode(data, i)
    elif code == 4:
        print(pos_im(data, a, i+1))
        i += 2
        return opcode(data, i)
    elif code == 5:
        if pos_im(data, a, i+1) != 0:
            i = pos_im(data, b, i+2)
        else:
            i += 3
        return opcode(data, i)
    elif code == 6:
        if pos_im(data, a, i+1) == 0:
            i = pos_im(data, b, i+2)
        else:
            i += 3
        return opcode(data, i)
    elif code == 7:
        if pos_im(data, a, i+1) < pos_im(data, b, i+2):
            data[data[i+3]] = 1
        else:
            data[data[i+3]] = 0
        i += 4
        return opcode(data, i)
    elif code == 8:
        if pos_im(data, a, i+1) == pos_im(data, b, i+2):
            data[data[i+3]] = 1
        else:
            data[data[i+3]] = 0
        i += 4
        return opcode(data, i)
    elif code == 9:
        return 0
    else:
        print('fail')

def run(data, parameter):
    return opcode(data, 0, parameter)


# -

data = np.loadtxt('./data/day5_data.csv', delimiter=',', dtype='int')
t = run(data, 5)
