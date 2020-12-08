#!/usr/bin/env python3
from functools import reduce

with open('./input.txt') as fp:
    puzzle_input = [group.strip().split() for group in fp.read().split('\n\n')]

def get_unique(group):
    return len(set(''.join(group)))

def get_shared(group):
    return len(reduce(lambda a,b: a&set(b), group, set(group[0])))

# Part 1 ######################################################################
print("sum of all groups unique answers:", sum(get_unique(g) for g in puzzle_input))

# Part 2 ######################################################################
print("sum of all groups shared answers:", sum(get_shared(g) for g in puzzle_input))
