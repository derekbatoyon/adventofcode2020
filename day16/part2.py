import fileinput
import re
import sys

from math import prod

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

    def valid_ticket(self, ticket):
        for value in ticket:
            if not self.valid_for_at_least_one_field(value):
                return False
        return True

    def valid_value(self, field, value):
        return any(value >= range[0] and value <= range[1] for range in self.rules[field])

    def __iter__(self):
        return iter(self.rules)

    def __getitem__(self, key):
        return self.rules[key]

def determine_rule_mapping(rules, tickets):
    ticket_count = len(tickets)
    field_count = len(tickets[0])
    candidates = {field: [] for field in rules}
    for field in rules:
        sys.stderr.write('analyze {}\n'.format(field))
        for position in range(field_count):
            valid_tickets = sum([rules.valid_value(field, ticket[position]) for ticket in tickets])
            if valid_tickets == ticket_count:
                sys.stderr.write('position {} candidate for {}\n'.format(position, field))
                candidates[field].append(position)

    fields = sorted(candidates.keys(), key=lambda field: len(candidates[field]))
    for index, field in enumerate(fields):
        assert len(candidates[field]) == 1, 'Cannot solve this way!'
        position = candidates[field][0]
        sys.stderr.write('{} is in position {}\n'.format(field, position))
        for other_field in fields[index+1:]:
            candidates[other_field].remove(position)

    return {f: p[0] for f, p in candidates.items()}

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

    valid_tickets = list(filter(lambda t: rules.valid_ticket(t), nearby_tickets))
    field_mapping = determine_rule_mapping(rules, valid_tickets)
    relavent_fields = filter(lambda f: f.startswith('departure'), rules)
    relavent_positions = [field_mapping[field] for field in relavent_fields]
    print(prod([your_ticket[position] for position in relavent_positions]))

if __name__ == "__main__":
    main()
