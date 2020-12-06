import fileinput

def get_group():
    group = {}
    for line in fileinput.input():
        line = line.strip()
        if len(line) == 0:
            yield group
            group.clear()
        group.update(dict([(question, True) for question in line]))
    yield group

def main():
    print(sum([len(group) for group in get_group()]))

if __name__ == "__main__":
    main()
