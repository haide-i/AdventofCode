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

from collections import Counter

f = open('./data/day2.csv')
data = [n.rstrip("\n") for n in f.readlines()]

threes = 0
twos = 0
for line in data:
    counter = Counter(line)
    all_val = counter.values()
    if 2 in all_val:
        twos += 1
    if 3 in all_val:
        threes += 1
result = twos * threes
print(twos, threes, result)


# +
end = False
for idx, line in enumerate(data):
    for scd_line in data[idx+1:]:
        count = sum(1 for a, b in zip(line, scd_line) if a != b)
        if count == 1:
            rslt = [line, scd_line]
            end = True
            break
    if end:
        break
        # print(line, scd_line, count)

print(rslt)
