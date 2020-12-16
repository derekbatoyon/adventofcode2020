import fileinput
import re

class Range(object):
    def __init__(self, arg):
        (self.lowerbound, self.upperbound) = tuple(int(n) for n in arg.split('-'))

class Rule(object):
    def __init__(self, args):
        self.ranges = [Range(arg) for arg in args]

    def is_valid(self, value):
        return any(value >= range.lowerbound and value <= range.upperbound for range in self.ranges)

class Rules(object):
    def __init__(self):
        self.rules = dict()

    def add_rule(self, field, rule):
        self.rules[field] = rule

    def valid_for_at_least_one_field(self, value):
        return any(rule.is_valid(value) for rule in self.rules.values())

def check_error_rate(rules, tickets):
    error = 0
    for ticket in tickets:
        for value in ticket:
            if not rules.valid_for_at_least_one_field(value):
                error += value
    return error

def read_input():
    rules_regex = re.compile('(?P<field>[^:]+):\s+(?P<range1>\d+-\d+)\s+or\s+(?P<range2>\d+-\d+)$')
    rules = Rules()

    input = fileinput.input()
    for line in input:
        if m:= rules_regex.match(line):
            rules.add_rule(m.group('field'), Rule(m.group('range1', 'range2')))
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
    return (rules, nearby_tickets)

def main():
    (rules, nearby_tickets) = read_input()
    print(check_error_rate(rules, nearby_tickets))

if __name__ == "__main__":
    main()
