import fileinput
import re

def check(line):
    m = regex.match(line)
    p1 = int(m.group(1)) - 1
    p2 = int(m.group(2)) - 1
    if p1 < 0 or p2 < 0:
        raise IndexError
    chr = m.group(3)
    password = m.group(4)
    return (password[p1] == chr) ^ (password[p2] == chr)

def main():
    valid = 0
    for line in fileinput.input():
        if check(line):
            valid += 1
    print(valid)

if __name__ == "__main__":
    regex = re.compile('(\d+)-(\d+)\s+(\w):\s+(\w+)')
    main()
