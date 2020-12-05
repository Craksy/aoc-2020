#!/usr/bin/env python3
with open('./input.txt', 'r') as puz:
    puzzle_input = [line.strip() for line in puz.readlines()]

binmap = {
    'F':'0',
    'L':'0',
    'B':'1',
    'R':'1',
    }
trans = 'FBRL'.maketrans(binmap)

def seat_to_int(seat):
    return int(seat.translate(trans), base=2)

# Part 1 ######################################################################
max_id = max(seat_to_int(seat) for seat in puzzle_input)
print('Highest seat id:',max_id)

# Part 2 ######################################################################
min_id = min(seat_to_int(seat) for seat in puzzle_input)
back_most = ((max_id>>3)-1)<<3
front_most = ((min_id>>3)+1)<<3
for i in range(front_most, back_most):
    if not i in map(seat_to_int, puzzle_input):
        print('Your seat must be', i)
        break
