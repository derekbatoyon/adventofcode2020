import fileinput
import re

year = re.compile('\d\d\d\d$')
height = re.compile('(?P<value>\d+)(?P<unit>cm|in)$')
hair_color = re.compile('#[0-9a-f]{6}$')
pid = re.compile('\d{9}$')

expected_keys = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
expected_keys.sort()
optional_key = 'cid'

def validate_byr(value):
    # four digits; at least 1920 and at most 2002
    m = year.match(value)
    return m is not None and int(value) in range(1920, 2003)

def validate_iyr(value):
    # four digits; at least 2010 and at most 2020
    m = year.match(value)
    return m is not None and int(value) in range(2010, 2021)

def validate_eyr(value):
    # four digits; at least 2020 and at most 2030
    m = year.match(value)
    return m is not None and int(value) in range(2020, 2031)

def validate_hgt(value):
    # a number followed by either cm or in:
    #   If cm, the number must be at least 150 and at most 193
    #   If in, the number must be at least 59 and at most 76
    m = height.match(value)
    if m:
        value = int(m.group('value'))
        unit = m.group('unit')
        return unit == 'cm' and value in range(150, 194) or unit == 'in' and value in range(59, 77)

def validate_hcl(value):
    # a # followed by exactly six characters 0-9 or a-f
    m = hair_color.match(value)
    return m is not None

def validate_ecl(value):
    # exactly one of: amb blu brn gry grn hzl oth
    return value in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']

def validate_pid(value):
    # a nine-digit number, including leading zeroes
    m = pid.match(value)
    return m is not None

validator = {
    'byr' : lambda v: validate_byr(v),
    'iyr' : lambda v: validate_iyr(v),
    'eyr' : lambda v: validate_eyr(v),
    'hgt' : lambda v: validate_hgt(v),
    'hcl' : lambda v: validate_hcl(v),
    'ecl' : lambda v: validate_ecl(v),
    'pid' : lambda v: validate_pid(v),
    'cid' : lambda v: True
}

def validate(passport):
    keys = list(passport)
    if optional_key in keys:
        keys.remove(optional_key)
    keys.sort()
    return keys == expected_keys and all([validator[key](value) for key, value in passport.items()])

def get_passport():
    info = {}
    for line in fileinput.input():
        if len(line) == 0 or line.isspace():
            yield info
            info.clear()
        info.update(dict([pair.split(':') for pair in line.split()]))
    yield info

def main():
    print([validate(passport) for passport in get_passport()].count(True))

if __name__ == "__main__":
    main()
