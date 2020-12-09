#!/usr/bin/env python3

with open('./input.txt') as fp:
    puzzle_input = [line.strip() for line in fp.readlines()]


def read_instruction(inst):
    op, arg = inst.split()
    return op, int(arg)

def run_until_loop(program):
    acc = 0
    pc = 0
    instructions_executed = []

    while pc not in instructions_executed and pc < len(program):
        instructions_executed.append(pc)
        op, arg = read_instruction(program[pc])
        acc += arg if op == 'acc' else 0
        pc += arg if op == 'jmp' else 1
    return acc, instructions_executed, pc<(len(program)-1)


# Part 1 #####################################################################
acc, insts, did_loop = run_until_loop(puzzle_input)
print('Value of accumulator just before loop:', acc)


# Part 2 #####################################################################
# I really fucking hate this solution... I gotta be able to come up with
# something better than brute forcing it.

for i in insts:
    # loop through each instruction from the first run.
    # if it was either a jmp or nop instruction, change it, otherwise skip it
    # keep going untill the program doesn't loop
    program = puzzle_input[:]
    op,_ = read_instruction(program[i])
    if op == 'acc':
        continue
    if op == 'jmp':
        program[i] = program[i].replace('jmp', 'nop')
    else:
        program[i] = program[i].replace('nop', 'jmp')

    acc, _, did_loop = run_until_loop(program)
    if not did_loop:
        print('did not loop after changing instruction', i)
        print('value of accumulator:', acc)
        break
