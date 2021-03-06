import fileinput
import re

def check(line):
    m = regex.match(line)
    min = int(m.group('min'))
    max = int(m.group('max'))
    chr = m.group('chr')
    password = m.group('password')
    c = password.count(chr)
    return c >= min and c <= max

def main():
    print(sum([check(line) for line in fileinput.input()]))

if __name__ == "__main__":
    regex = re.compile('(?P<min>\d+)-(?P<max>\d+)\s+(?P<chr>\w):\s+(?P<password>\w+)')
    main()
