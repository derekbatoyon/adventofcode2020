import fileinput
import re

def read_rules(input):
    rule_definition = re.compile('(?P<ruleid>\d+):\s+(?P<rule>.+)$')

    rules = dict()
    for line in input:
        if m := rule_definition.match(line):
            ruleid = m.group('ruleid')
            rule = m.group('rule')
            rules[int(ruleid)] = rule
        else:
            break

    assert line.isspace()
    return rules

def build_pattern(rules, ruleid):
    rule = rules[ruleid]

    if m := re.match('"(?P<literal>.*)"$', rule):
        return m.group('literal')

    rule_pattern = '('
    for token in rule.split():
        if token == '|':
            rule_pattern += '|'
        elif token.isdigit():
            rule_pattern += build_pattern(rules, int(token))
        else:
            raise RuntimeError

    rule_pattern += ')'
    return rule_pattern

def check_rule0(rules, line):
    rule42 = re.compile(build_pattern(rules, 42))
    rule31 = re.compile(build_pattern(rules, 31))

    line = line.strip()

    rule42_matches = 0
    rule31_matches = 0

    index = 0
    while m := rule42.match(line, index):
        rule42_matches += 1
        index = m.end()
    while m := rule31.match(line, index):
        rule31_matches += 1
        index = m.end()
    return index == len(line) and rule31_matches> 0 and rule42_matches > rule31_matches

def main():
    input = fileinput.input()
    rules = read_rules(input)

    matches = 0
    for line in input:
        if match := check_rule0(rules, line):
            matches += 1

    print(matches)

if __name__ == "__main__":
    main()
