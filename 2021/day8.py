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

import itertools

f = open('./data/day8.csv')
patterns = []
output = []
for line in f.readlines():
    a, b = line.rstrip('\n').split('|')
    patterns.append(a.rstrip(' ').split(' '))
    output.append(b.lstrip(' ').split(' '))

# # Part 1

digits = {1: 2, 4: 4, 7: 3, 8: 7}
occurrence = dict.fromkeys(digits.keys())
output_merged = list(itertools.chain(*output))
for d, ctr in digits.items():
    occurrence[d] = sum(map(lambda x : len(x)==ctr, output_merged))
print(occurrence)
print(sum(occurrence.values()))


# # Part 2

# +
def mapping(patterns):
    mapped = {}
    mapped['a'] = rule_one(patterns)
    mapped['c'], mapped['f'] = rule_six(patterns)
    mapped['b'], mapped['e'] = rule_five(patterns, mapped)
    mapped['d'] = rule_four(patterns, mapped)
    already = [list(x)[0] for x in mapped.values()]
    mapped['g'] = set('abcdefg').difference(set(already))
    values = [list(x)[0] for x in mapped.values()]
    actually_mapped = dict(zip(values, mapped.keys()))
    return actually_mapped

def rule_one(inputs):
    one = next(filter(lambda x : len(x) == 2, inputs), None)
    seven = next(filter(lambda x : len(x) == 3, inputs), None)
    return set(seven).difference(set(one))

def rule_six(inputs):
    one = set(next(filter(lambda x : len(x) == 2, inputs), None))
    f = one.intersection(set(next(filter(lambda x : ((len(x)==6) & (len(one.intersection(set(x))) == 1)), inputs), None)))
    c = one.difference(f)
    return c, f

def rule_five(inputs, mapped):
    one = set(next(filter(lambda x : len(x) == 2, inputs), None))
    two_or_five = [x for x in inputs if ((len(x)==5) & len(one.intersection(set(x))) == 1)]
    three = next(filter(lambda x : ((len(x)==5) & (len(one.intersection(set(x)))==2)), inputs), None)
    two = next(filter(lambda x : len(mapped['c'].intersection(set(x)))==1, two_or_five), None)
    five = next(filter(lambda x : len(mapped['f'].intersection(set(x)))==1, two_or_five), None)
    b = set(five).difference(set(three))
    e = set(two).difference(set(three))
    return b, e

def rule_four(inputs, mapped):
    four = next(filter(lambda x : len(x)==4, inputs), None)
    existing = mapped['b'].union(mapped['c'], mapped['f'])
    d = set(four).difference(existing)
    return d

def apply_map(string, mapped, numbers):
    right_string = set([list(mapped[x])[0] for x in string])
    right_number = [key for key, n in numbers.items() if n==right_string]
    return right_number[0]

def translate(patterns, output):
    numbers = {0: set(['a', 'b', 'c', 'e', 'f', 'g']),
               1: set(['c', 'f']),
               2: set(['a', 'c', 'd', 'e', 'g']),
               3: set(['a', 'c', 'd', 'f', 'g']),
               4: set(['b', 'c', 'd', 'f']),
               5: set(['a', 'b', 'd', 'f', 'g']),
               6: set(['a', 'b', 'd', 'e', 'f', 'g']),
               7: set(['a', 'c', 'f']),
               8: set(['a', 'b', 'c', 'd', 'e', 'f', 'g']),
               9: set(['a', 'b', 'c', 'd', 'f', 'g'])}
    mapped = mapping(patterns)
    output_numbers = [str(apply_map(x, mapped, numbers)) for x in output]
    final = int("".join(output_numbers))
    return final


# +

output_values = list(map(lambda x, y: translate(x, y), patterns, output))
result = sum(output_values)
print(result)

