import re

def parse_passport(txt):
    """
    >>> data = '''ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
    ... byr:1937 iyr:2017 cid:147 hgt:183cm'''
    >>> parse_passport(data)
    {'ecl': 'gry', 'pid': '860033327', 'eyr': '2020', 'hcl': '#fffffd', 'byr': '1937', 'iyr': '2017', 'cid': '147', 'hgt': '183cm'}
    """

    pp = {}
    for kv in txt.split():
        k,v = kv.split(':')
        pp[k] = v
    return pp


def parse_passports(txt):
    pps_txt = txt.split('\n')
    pps = [parse_passport(pp_txt) for pp_txt in pps_txt]
    return pps


def valid_passport(passport):
    """
    Passport must have 7 keys, cid is optional
    """
    keys = {'byr','iyr','eyr','hgt','hcl','ecl','pid'}
    return set(passport) >= keys

def valid_height(val):
    try:
        num, unit = re.match(r'(\d{2,3})(cm|in)$', val).groups()
    except AttributeError:
        return False
    if unit == 'cm':
        return 150 <= int(num) <= 193
    elif unit == 'in':
        return 59 <= int(num) <= 76

def valid_hcl(val):
    res = re.match(r'\#[a-f0-9]{6}$', val)
    return res

def valid_values(passport):
    keys = {'byr':lambda val: 1920 <= int(val) <= 2002,
            'iyr':lambda val: 2010 <= int(val) <= 2020,
            'eyr':lambda val: 2020 <= int(val) <= 2030,
            'hgt':valid_height,
            'hcl':valid_hcl, #lambda val: re.match(r'\#(a-f0-9){6}', val),
            'ecl':lambda val: val in set('amb blu brn gry grn hzl oth'.split()),
            'pid':lambda val: re.match(r'[0-9]{9}$', val)
            }

    for key, val in passport.items():
        if key not in keys:
            continue
        if not keys[key](val):
            print("FAIL", key, passport)
            return False
    return True

with open('../inputs/day_4_input.txt') as input:
    passports = parse_passports(input.read())
    valid_passports = sum([valid_passport(passport) and valid_values(passport) for passport in passports])
    print(valid_passports)

