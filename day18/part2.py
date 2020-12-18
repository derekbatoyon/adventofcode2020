import fileinput
import math

def simplify(line):
    stack = [0]
    operator = '+'

    tokens = line.split()
    for token in tokens:
        if token.isdigit():
            n = int(token)
            if operator == '+':
                stack[-1] += n
            else:
                stack.append(n)
        elif token == '+' or token == '*':
            operator = token
        else:
            raise RuntimeError

    return math.prod(stack)

def get_matching_parentheses(line):
    left, right = None, None
    for i in range(len(line)):
        if line[i] == '(':
            left = i
        elif line[i] == ')':
            right = i
            break
    return left, right

def process(line):
    left, right = get_matching_parentheses(line)
    while left is not None and right is not None:
        n = simplify(line[left+1:right])
        line = line[:left] + str(n) + line[right+1:]
        left, right = get_matching_parentheses(line)
    assert left is None and right is None
    return simplify(line)

def main():
    print(sum(process(line) for line in fileinput.input()))

if __name__ == "__main__":
    main()
