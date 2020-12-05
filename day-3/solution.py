#!/usr/bin/env python3

from functools import reduce

with open('./input.txt') as infile:
    puzzle_input = [line.strip() for line in infile.readlines()]

width = len(puzzle_input[0])
height = len(puzzle_input)

def tree_at_coord(x, y):
    return puzzle_input[y][x%width] == '#'

def trees_encountered(step_x, step_y):
    x,y,count = 0,0,0
    while y < height-1:
        x+=step_x
        y+=step_y
        count += tree_at_coord(x,y)
    return count


# Part 1 ######################################################################
print('Trees encountered:', trees_encountered(3,1))


# Part 2 ######################################################################
slopes = [
    (1,1),
    (3,1),
    (5,1),
    (7,1),
    (1,2)
]
prod_of_slopes = reduce(lambda a,b: a*trees_encountered(*b), slopes, 1)
print('Product of trees, on all slopes:', prod_of_slopes)
