import re
import pyperclip

def parse_passport(line):
    """
    >>> line = 'eyr:2033 hgt:177cm pid:173cm ecl:utc byr:2029 hcl:#efcc98 iyr:2023'
    >>> parse_passport(line)
    {'eyr': '2033', 'hgt': '177cm', 'pid': '173cm', 'ecl': 'utc', 'byr': '2029', 'hcl': '#efcc98', 'iyr': '2023'}
    """
    pp = {}
    for information in line.split():
        category, data = information.split(':')
        pp[category] = data
    return pp

with open("inputs/day_4_input.txt", "r") as input:
    lines = [line.strip('\n') for line in input.readlines()]
    passports = [parse_passport(line) for line in lines]

    valid_passports = 0
    for passport in passports:
        if len(passport) == 8:
            valid_passports += 1
        elif len(passport) == 7 and 'cid' not in passport:
            valid_passports += 1

        
# Below is my original solution. Harrison created a dictionary from the start which turns out to be useful later.
    # for index, line in enumerate(lines):
    #     data = sorted(line.split())
    #     if len(data) == 8:
    #         valid_passports += 1
    #     if len(data) == 7:
    #         check = ''.join(data)
    #         if 'cid:' not in check:
    #             valid_passports += 1


print(valid_passports)
pyperclip.copy(valid_passports)

def data_validation(passport):
    """
    >>> passport = {'eyr': '2033', 'hgt': '177cm', 'pid': '173cm', 'ecl': 'utc', 'byr': '2029', 'hcl': '#efcc98', 'iyr': '2023'}
    >>> data_validation(passport)
    False

    >>> passport_2 =  {'hcl': '#888785', 'hgt': '164cm', 'byr': '2001', 'iyr': '2015', 'cid': '88', 'pid': '545766238', 'ecl': 'hzl', 'eyr': '2022'}
    >>> data_validation(passport_2)
    True
    """
    if not (1920 <= int(passport['byr']) <= 2002):
        return False

    if not (2010 <= int(passport['iyr']) <= 2020):
        return False

    if not (2020 <= int(passport['eyr']) <= 2030):
        return False

    if 'in' in passport['hgt']:
        if not (59 <= int(passport['hgt'][:-2]) <= 76):
            return False

    if 'cm' in passport['hgt']:
        if not (150 <= int(passport['hgt'][:-2]) <= 193):
            return False

    if not (re.match(r'\#[0-9a-f]{6}$', passport['hcl'])):
        return False

    if not (passport['ecl'] in set("amb blu brn gry grn hzl oth".split())):
        return False

    if not (re.match(r'\d{9}$', passport['pid'])):
        return False

    return True
    

    
with open("inputs/day_4_input.txt", "r") as input:
    lines = [line.strip('\n') for line in input.readlines()]
    passports = [parse_passport(line) for line in lines]

    valid_passports = 0
    for passport in passports:
        if len(passport) == 8:
            valid_passports += data_validation(passport)
        elif len(passport) == 7 and 'cid' not in passport:
            valid_passports += data_validation(passport)


print(valid_passports)
pyperclip.copy(valid_passports)
if __name__ == "__main__":
    import doctest
    doctest.testmod()
