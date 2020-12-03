import fileinput

from math import prod

def count_encounters(trees, right, down):
    columns = len(trees[0])
    encounters = 0
    column = 0
    for row in trees[::down]:
        if row[column] == '#':
            encounters += 1
        column = (column + right) % columns
    return encounters

def main():
    trees = [line.strip() for line in fileinput.input()]

    columns = len(trees[0])
    for row in trees[1:]:
        assert len(row) == columns

    slopes = [(1, 1),
              (3, 1),
              (5, 1),
              (7, 1),
              (1, 2)]

    print(prod([count_encounters(trees, right, down) for right, down in slopes]))

if __name__ == "__main__":
    main()
