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

import re


def calculate(expr):
    expr = expr.lstrip('(').rstrip(')').split(' ')
    total = int(expr[0])
    i = 1
    while i < len(expr):
        if expr[i] == '*':
            total *= int(expr[i+1])
        elif expr[i] == '+':
            total += int(expr[i+1])
        i += 2
    return total


def add_first(expr):
    expr = expr.replace('(', ' ').replace(')', ' ')
    while re.search('[0-9]* \+ [0-9]*', expr) is not None:
        addition = re.search('[0-9]* \+ [0-9]*', expr).group()
        parts = addition.split(' ')
        result = int(parts[0]) + int(parts[-1])
        expr = expr.replace(addition, str(result), 1)
    total = calculate(expr)
    return total



# + tags=[]
f = open('data/day18_data.csv')
total = 0
part = 2
for line in f:
    line = line.rstrip('\n')
    while len(re.findall('\([^\(\)]*\)', line))!=0:
        brackets = re.findall('\([^\(\)]*\)', line)
        if part==1:
            calculated = list(map(calculate, brackets))
        if part==2:
            calculated = list(map(add_first, brackets))
        for i in range(len(brackets)):
            line = line.replace(brackets[i], str(calculated[i]))
    if part==1:
        total += int(calculate(line))
    if part==2:
        total += int(add_first(line))

print(total)
