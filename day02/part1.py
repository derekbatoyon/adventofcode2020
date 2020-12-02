import fileinput
import re

def check(line):
    m = regex.match(line)
    min = int(m.group(1))
    max = int(m.group(2))
    chr = m.group(3)
    password = m.group(4)
    c = password.count(chr)
    return c >= min and c <= max

def main():
    valid = 0
    for line in fileinput.input():
        if check(line):
            valid += 1
    print(valid)

if __name__ == "__main__":
    regex = re.compile('(\d+)-(\d+)\s+(\w):\s+(\w+)')
    main()
