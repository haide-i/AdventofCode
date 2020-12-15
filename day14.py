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

def apply_bitmask(bits, mask_bit):
    if mask_bit != 'X':
        return mask_bit
    else:
        return bits


# + tags=[]
f = open('data/day14_data.csv')
positions = {}
for line in f:
    if line.startswith('mask'):
        mask = line.lstrip('mask = ').rstrip('\n')
    if line.startswith('mem'):
        position = int(line.split(']')[0].replace(']', '').split('[')[-1])
        value =  "{0:036b}".format(int(line.split(' ')[-1]))
        value = ''.join(list(map(apply_bitmask, value, mask)))
        positions[position] = value
total = 0
for key, item in positions.items():
    total += int(item, 2)
print(total)


# -

# ## Part 2

def memory_decoder()


f = open('data/day14_data.csv')
positions = {}
for line in f:
    if line.startswith('mask'):
        mask = line.lstrip('mask = ').rstrip('\n')
    if line.startswith('mem'):
        position = int(line.split(']')[0].replace(']', '').split('[')[-1])
        value =  "{0:036b}".format(int(line.split(' ')[-1]))
        positions[position] = value
total = 0

