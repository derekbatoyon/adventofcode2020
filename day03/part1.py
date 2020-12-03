import fileinput

right = 3
down = 1

def main():
    trees = [line.strip() for line in fileinput.input()]

    columns = len(trees[0])
    for row in trees[1:]:
        assert len(row) == columns

    encounters = 0
    column = 0
    for row in trees:
        if row[column] == '#':
            encounters += 1
        column = (column + right) % columns

    print(encounters)

if __name__ == "__main__":
    main()
