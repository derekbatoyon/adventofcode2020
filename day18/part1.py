import fileinput
import re

def process(line):
    stack = ['0', '+']

    operation = {
        '+': lambda a, b: a + b,
        '*': lambda a, b: a * b,
    }

    tokens = re.split('\s+|(?<=\()|(?=\))', line)
    for token in tokens:
        if len(token) == 0:
            continue
        elif token.isdigit():
            operator = stack.pop()
            a = int(stack.pop())
            b = int(token)
            result = operation[operator](a, b)
            stack.append(result)
        elif token == '+' or token == '*':
            stack.append(token)
        elif token == '(':
            stack.append('0')
            stack.append('+')
        elif token == ')':
            a = int(stack.pop())
            operator = stack.pop()
            b = int(stack.pop())
            result = operation[operator](a, b)
            stack.append(result)
        else:
            raise RuntimeError

    assert len(stack) == 1
    return stack[0]

def main():
    print(sum(process(line) for line in fileinput.input()))

if __name__ == "__main__":
    main()
