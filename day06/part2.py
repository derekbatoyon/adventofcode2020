import fileinput

def get_group():
    group = []
    for line in fileinput.input():
        if len(line) == 0 or line.isspace():
            yield group
            group.clear()
            continue
        group.append(line.strip())
    yield group

def examine_group(group):
    result = set(group[0])
    for person in group[1:]:
        result =  result.intersection(set(person))
    return len(result)

def main():
    print(sum([examine_group(group) for group in get_group()]))

if __name__ == "__main__":
    main()
