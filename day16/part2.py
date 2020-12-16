import fileinput
import re

from math import prod

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

    def valid_ticket(self, ticket):
        return all(self.valid_for_at_least_one_field(value) for value in ticket)

    def __iter__(self):
        return iter(self.rules)

    def __getitem__(self, key):
        return self.rules[key]

def determine_rule_mapping(rules, tickets):
    ticket_count = len(tickets)
    field_count = len(tickets[0])
    candidates = {field: [] for field in rules}
    for field in rules:
        for position in range(field_count):
            valid_tickets = sum(rules[field].is_valid(ticket[position]) for ticket in tickets)
            if valid_tickets == ticket_count:
                candidates[field].append(position)

    fields = sorted(candidates.keys(), key=lambda field: len(candidates[field]))
    for index, field in enumerate(fields):
        assert len(candidates[field]) == 1, 'Cannot solve this way!'
        position = candidates[field][0]
        for other_field in fields[index+1:]:
            candidates[other_field].remove(position)

    return {f: p[0] for f, p in candidates.items()}

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
    return (rules, your_ticket, nearby_tickets)

def main():
    (rules, your_ticket, nearby_tickets) = read_input()
    valid_tickets = list(filter(lambda t: rules.valid_ticket(t), nearby_tickets))
    field_mapping = determine_rule_mapping(rules, valid_tickets)
    relavent_fields = filter(lambda f: f.startswith('departure'), rules)
    relavent_positions = [field_mapping[field] for field in relavent_fields]
    print(prod([your_ticket[position] for position in relavent_positions]))

if __name__ == "__main__":
    main()
