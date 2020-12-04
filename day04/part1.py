import fileinput

expected_keys = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
expected_keys.sort()
optional_key = 'cid'

def validate(passport):
    keys = list(passport)
    if optional_key in keys:
        keys.remove(optional_key)
    keys.sort()
    return keys == expected_keys

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
