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

import numpy as np

f = open('./data/day3.csv')
data = np.array([np.array(list((n.rstrip('\n'))), dtype='int') for n in f.readlines()])

# # Part 1

# +
data_tr = np.transpose(data)
gamma = ''
epsilon = ''
rows = np.shape(data_tr)[0]

for i in range(rows):

    nr_of_ones = np.count_nonzero(data_tr[:][i])
    if nr_of_ones > (np.shape(data_tr)[1]/2.):
        gamma += '1'
        epsilon += '0'
    else:
        gamma += '0'
        epsilon += '1'


int_gamma = int(gamma, 2)
int_epsilon = int(epsilon, 2)
print(int_gamma, int_epsilon, int_gamma*int_epsilon)
# -

# # Part 2

# +
ox_data = data
co_data = data

for i in range(np.shape(ox_data)[1]):
    nr_of_ones = np.count_nonzero(ox_data[:,i])
    if nr_of_ones >= (np.shape(ox_data)[0]/2.):
        ox_idxs = np.squeeze(np.where(ox_data[:,i]==1))
    else:
        ox_idxs = np.squeeze(np.where(ox_data[:,i]==0))
    ox_data = np.squeeze(np.take(ox_data, ox_idxs, axis=0))
    if ox_data.ndim == 1:
        break

for i in range(np.shape(co_data)[1]):
    nr_of_ones = np.count_nonzero(co_data[:,i])
    if nr_of_ones >= (np.shape(co_data)[0]/2.):
        co_idxs = np.squeeze(np.where(co_data[:,i]==0))
    else:
        co_idxs = np.squeeze(np.where(co_data[:,i]==1))
    co_data = np.squeeze(np.take(co_data, co_idxs, axis=0))
    if co_data.ndim == 1:
        break


ox_bits = "".join(np.char.mod('%i', ox_data))
co_bits = "".join(np.char.mod('%i', co_data))
int_ox = int(ox_bits, 2)
int_co = int(co_bits, 2)
print(int_ox, int_co, int_ox*int_co)

