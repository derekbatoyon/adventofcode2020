import fileinput
import re

def check(line):
    m = regex.match(line)
    p1 = int(m.group('p1')) - 1
    p2 = int(m.group('p2')) - 1
    if p1 < 0 or p2 < 0:
        raise IndexError
    chr = m.group('chr')
    password = m.group('password')
    return (password[p1] == chr) ^ (password[p2] == chr)

def main():
    print(sum([check(line) for line in fileinput.input()]))

if __name__ == "__main__":
    regex = re.compile('(?P<p1>\d+)-(?P<p2>\d+)\s+(?P<chr>\w):\s+(?P<password>\w+)')
    main()
