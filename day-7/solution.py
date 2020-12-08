#!/usr/bin/env python3

with open('./input.txt') as fp:
    puzzle_input = [rule.strip() for rule in fp.readlines()]

def parse_rule(rule):
    """
    return a (clr, rules) tuple where clr is the bag color, and rules is a dict that maps {color: count}
    """
    bag_color, contains = rule.split(' bags contain ')
    subrules = {}
    for sr in contains.split(', '):
        if sr == 'no other bags.':
            subrules = None
        else:
            sr = sr.split()
            count = int(sr[0])
            color = ' '.join(sr[1:3])
            subrules[color] = count

    return bag_color, subrules

rule_dict = {}
for rule in puzzle_input:
    k,v = parse_rule(rule)
    rule_dict[k] = v


def can_be_in(target):
    """return a list of all colors of bag which `target` can be in """
    return [color for color,rules in rule_dict.items() if rules and target in rules]

def possible_outer(target):
    possible = []
    parents = can_be_in(target)
    possible.extend(parents)
    for p in parents:
        possible.extend(possible_outer(p))

    return set(possible)

def get_bag_count(target):
    rules = rule_dict[target]
    return 0 if not rules else sum(v+get_bag_count(k)*v for k,v in rules.items())

print('Possible outer bags:', len(possible_outer('shiny gold')))
print('Total inner bag count:', get_bag_count('shiny gold'))
