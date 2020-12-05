#!/usr/bin/env python3


with open('./input.txt', 'r') as infile:
    puzzle_input = [line[:-1] for line in infile.readlines()]

def split_line(line):
    rule, password = line.split(': ')
    count, letter = rule.split(' ')
    cmin, cmax = count.split('-')

    return int(cmin), int(cmax), letter, password

def check_pass(cmin, cmax, letter, password):
    """check that `password` contains `letter` between cmin-cmax times"""
    return cmin <= password.count(letter) <= cmax

def check_pass_2(pos_a, pos_b, letter, password):
    """check if 1, but only 1, of the positions `a` and `b` of `password` is
    `letter`"""
    a = password[pos_a-1] == letter
    b = password[pos_b-1] == letter
    return a != b



print('Part 1:', sum(check_pass(*split_line(line)) for line in puzzle_input))
print('Part 2:', sum(check_pass_2(*split_line(line)) for line in puzzle_input))
