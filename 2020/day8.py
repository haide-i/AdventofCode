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

# +
def do_op(instr, i, accumulator, idxlist=[]):
    if (i in idxlist) and (len(idxlist) != 0):
        return accumulator, 'repeat'
    else:
        idxlist.append(i)
    if (i >= len(instr)):
        return accumulator, 'terminate'
    else:
        if instr[i][0] == 'nop':
            i += 1
        elif instr[i][0] == 'acc':
            if instr[i][1][0] == '+':
                accumulator = accumulator + int(instr[i][1][1:])
            elif instr[i][1][0] == '-':
                accumulator = accumulator - int(instr[i][1][1:])
            i += 1
        elif instr[i][0] == 'jmp':
            if instr[i][1][0] == '+':
                i += int(instr[i][1][1:])
            elif instr[i][1][0] == '-':
                i -= int(instr[i][1][1:])
        return do_op(instr, i, accumulator, idxlist)
        
    
# -

f = open('data/dummy.csv')
operations = []
for line in f:
    line = line.rstrip('\n')
    operation = line.split(' ')
    operations.append(operation)
print(operations)
accumulator = 0
do_op(operations, 0, 0)

# ## Part 2

f = open('data/day8_data.csv')
operations = []
for line in f:
    line = line.rstrip('\n')
    operation = line.split(' ')
    operations.append(operation)
for idx, i in enumerate(operations):
    op_cp = operations.copy()
    if i[0] == 'jmp':
        op_cp[idx][0] = 'nop'
        value, check = do_op(op_cp.copy(), 0, 0, idxlist=[])
        op_cp[idx][0] = 'jmp'
        if check == 'terminate':
            print(check, value)

for idx, i in enumerate(operations):
    op_cp = operations.copy()
    if i[0] == 'nop':
        op_cp[idx][0] == 'jmp'
        value, check = do_op(op_cp, 0, 0)
        if check == 'terminate':
            print(check, value)
