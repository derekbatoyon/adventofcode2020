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

def check(rules, ruleid, line):
    rule_pattern = build_pattern(rules, ruleid) + '$'
    match = re.match(rule_pattern, line)
    return match is not None

def main():
    input = fileinput.input()
    rules = read_rules(input)

    matches = 0
    for line in input:
        if match := check(rules, 0, line):
            matches += 1

    print(matches)

if __name__ == "__main__":
    main()
