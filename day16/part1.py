import fileinput
import re
import sys

class Rules(object):
    def __init__(self):
        self.rules = dict()

    def add_rule(self, field, ranges):
        self.rules[field] = ranges

    def valid_for_at_least_one_field(self, value):
        for field, rule in self.rules.items():
            for range in rule:
                if value >= range[0] and value <= range[1]:
                    return True
        sys.stderr.write('{} is invalid\n'.format(value))
        return False

def check_error_rate(rules, tickets):
    error = 0
    for ticket in tickets:
        for value in ticket:
            if not rules.valid_for_at_least_one_field(value):
                error += value
    return error

def main():
    rules_regex = re.compile('(?P<field>[^:]+):\s+(?P<range1>\d+-\d+)\s+or\s+(?P<range2>\d+-\d+)$')
    rules = Rules()

    input = fileinput.input()
    for line in input:
        if m:= rules_regex.match(line):
            range1 = tuple([int(n) for n in m.group('range1').split('-')])
            range2 = tuple([int(n) for n in m.group('range2').split('-')])
            rules.add_rule(m.group('field'), [range1, range2])
        else:
            break

    for line in input:
        line = line.strip()
        if line == 'your ticket:':
            continue
        if line == 'nearby tickets:':
            break
        if len(line):
            your_ticket = [int(n) for n in line.split(',')]

    nearby_tickets = [[int(n) for n in line.split(',')] for line in input]

    print(check_error_rate(rules, nearby_tickets))

if __name__ == "__main__":
    main()
