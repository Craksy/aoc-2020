#!/usr/bin/env python3
import re

with open('./input.txt', 'r') as infile:
    puzzle_input = infile.read()


passports_raw = puzzle_input.split('\n\n')

# Each item is a field name and a list of one or more rules.
# Each rule is a tuple containing a patter and optionally a range.
required_fields = {
    'byr': [(r'^(\d{4})$', range(1920, 2003))],
    'iyr': [(r'^(\d{4})$', range(2010, 2021))],
    'eyr': [(r'^(\d{4})$', range(2020, 2031))],
    'hgt': [(r'^(\d{3})cm$', range(150, 194)), ('^(\d{2})in$', range(59,77))],
    'hcl': [(r'^#[0-9a-f]{6}$', None)],
    'ecl': [(r'^(amb|blu|brn|gry|grn|hzl|oth)$', None)],
    'pid': [(r'^[0-9]{9}$', None)]
}

def pass_to_dict(passport):
    """compile a dictionary from raw string data"""
    pairs = [p.split(':') for p in passport.strip().split()]
    return {k:v for k,v in pairs}

def validate_passport(passport_dict):
    """check if a passport contains all required fields"""
    return all(f in passport_dict for f in required_fields)

def check_pattern_range(value, pattern, valid_range=None):
    """check if a value matches a pattern and potentially a range"""
    m = re.match(pattern, value)
    if not m:
        return False
    if valid_range and int(m.group(1)) not in valid_range:
        return False
    return True

def check_field(value, rules):
    """Check if the value of field mathes any of the rules provided"""
    return any(check_pattern_range(value, *rule) for rule in rules)

def validate_fields(passport_dict):
    """Check if every field matching at least on of the corresponding rules"""
    if not validate_passport(passport_dict):
        return False
    return all(check_field(passport_dict[field], rules) for field,rules in required_fields.items())


# Part 1 ######################################################################
valid_passports = sum(validate_passport(pass_to_dict(p)) for p in passports_raw)
print('Valid passports:', valid_passports)

# Part 2 ######################################################################
valid_passports_and_fields = sum(validate_fields(pass_to_dict(p)) for p in passports_raw)
print('Valid passports with valid field values:', valid_passports_and_fields)
