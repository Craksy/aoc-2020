#!/usr/bin/env python3

with open('./input.txt', 'r') as infile:
    puzzle_input = [int(line[:-1]) for line in infile.readlines()]

for i in puzzle_input:
    pair = 2020-i
    if pair in puzzle_input:
        print('part1:',i*pair)
        break


for i in puzzle_input:
    for j in puzzle_input:
        pair = 2020-i-j
        if pair in puzzle_input:
            print('part2:', i*j*pair)
            break
