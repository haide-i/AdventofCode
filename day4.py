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

# ## Part 1

# + tags=[]
f = open('data/day4_data.csv')
fields = ['byr:', 'iyr:', 'eyr:', 'hgt:', 'hcl:', 'ecl:', 'pid:', 'cid:']
passports = []
person = ''
for line in f:
    line = line.replace('\n', '')
    if line.islower():
        person = person + ' ' + line.rstrip(' ')
    else:
        person = person.lstrip(' ')
        passports.append(person)
        person = ''
passports.append(person.lstrip(' '))
invalid = 0
for p in passports:
    for f in fields[:-1]:
        if f not in p:
            invalid += 1
            break
valid = len(passports) - invalid
print(valid, invalid, len(passports))
# -

# ## Part 2

# + tags=[]
import re
def is_valid(key, value):
    valid = False
    if key == 'byr':
        if 1920 <= int(value) <= 2002:
            valid = True
    elif key == 'iyr':
        if 2010 <= int(value) <= 2020:
            valid = True
    elif key == 'eyr':
        if 2020 <= int(value) <= 2030:
            valid = True
    elif key == 'hgt':
        if value[-2:] == 'cm':
            if 150 <= int(value[:-2]) <= 193:
                valid = True
        elif value[-2:] == 'in':
            if 59 <= int(value[:-2]) <= 76:
                valid = True
    elif key == 'hcl':
        if re.match(r"#[0-9a-f]{6}", value) is not None:
            valid = True
    elif key == 'ecl':
        colors = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
        if value in colors:
            valid = True
    elif key == 'pid':
        if re.match(r"[0-9]{9}", value) is not None and len(value)==9:
            valid = True
    elif key == 'cid':
        valid = True
    return valid

invalid = 0
for p in passports:
    skip = False
    next_p = False
    entries = p.split(' ')
    for f in fields[:-1]:
        if f not in p:
            invalid += 1
            next_p = True
            break
    if not next_p: 
        for e in entries:
            key, value = e.split(':')
            if not is_valid(key, value):
                invalid += 1
                break
valid = len(passports[:54]) - invalid
print(valid, invalid)
