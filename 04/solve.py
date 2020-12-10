import re

def valid_hgt(height):
    if height[-2:] not in ['cm', 'in']:
        return False
    if height[-2:] == 'cm':
        if not ('150' <= height[:3] <= '193'):
            return False
    if height[-2:] == 'in':
        if not ('59' <= height[:2] <= '76'):
            return False
    return True

def valid_arg(passport):
    if not ('1920' <= passport['byr'] <= '2002'):
        return False
    if not ('2010' <= passport['iyr'] <= '2020'):
        return False
    if not ('2020' <= passport['eyr'] <= '2030'):
        return False
    if not valid_hgt(passport['hgt']):
        return False
    if not re.match("^#[0-9a-f]{6}$", passport['hcl']):
        return False
    if passport['ecl'] not in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
        return False
    if not (len(passport['pid']) == 9 and passport['pid'].isdigit()):
        return False
    return True

def valid(passport):
    if len(passport) == 7 and 'cid' not in passport.keys() or len(passport) == 8:
        if valid_arg(passport):
            return True
    return False

def count_valid(passports):
    count = 0
    for passport in passports:
        if valid(passport):
            count += 1
    return count

with open("input", "r") as f:
    passports =[{}]
    for line in f:
        elmts = line.split()
        for elmt in elmts:
            key, value = elmt.split(':')
            passports[-1][key] = value
        if not elmts:
            passports.append({})
    print(count_valid(passports))