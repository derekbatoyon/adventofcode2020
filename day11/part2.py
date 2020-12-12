import itertools

EMPTY_SEAT = 'L'
OCCUPIED_SEAT = '#'
FLOOR = '.'

adjacents = [
    (-1, -1),
    (-1, 0),
    (-1, 1),
    (0, -1),
    (0, 1),
    (1, -1),
    (1, 0),
    (1, 1)
]

class Counter(object):
    def __init__(self):
        self.counter = 0
    def count(self):
        self.counter += 1
    def get_count(self):
        return self.counter

def print_layout(grid):
    for row in grid:
        print(''.join(row))

def update(row, col, grid, counter):
    seat = grid[row][col]
    if seat == FLOOR:
        return FLOOR

    adjacent_occupied = 0
    for dr, dc in adjacents:
        r = row
        c = col
        while True:
            r += dr
            c += dc
            if r < 0 or c < 0:
                break

            try:
                if grid[r][c] == OCCUPIED_SEAT:
                    adjacent_occupied += 1
                if grid[r][c] != FLOOR:
                    break
            except IndexError:
                break

    if seat == EMPTY_SEAT and adjacent_occupied == 0:
        counter.count()
        return OCCUPIED_SEAT
    if seat == OCCUPIED_SEAT and adjacent_occupied >= 5:
        counter.count()
        return EMPTY_SEAT
    return seat

def main(args):
    with open(args.input, "r") as input:
        grid = [[pos for pos in line.strip()] for line in input]

    rows = len(grid)
    cols = len(grid[0])

    keep_going = lambda r: True
    round = 0
    if args.rounds:
        keep_going = lambda r: r < args.rounds

    while keep_going(round):
        counter = Counter()
        new_grid = [[update(row, col, grid, counter) for col in range(cols)] for row in range(rows)]
        if counter.get_count() == 0:
            break
        grid = new_grid
        round += 1

    if args.rounds:
        print_layout(grid)
    else:
        print(sum([1 for seat in itertools.chain(*grid) if seat == OCCUPIED_SEAT]))

def test(args):
    with open(args.input, "r") as input:
        grid = [[pos for pos in line.strip()] for line in input]

    if args.input == 'example1.txt':
        update(4, 3, grid, Counter())
    if args.input == 'example2.txt':
        update(1, 1, grid, Counter())
    if args.input == 'example3.txt':
        update(3, 3, grid, Counter())

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('input', help='Input file')
    parser.add_argument('-r', '--rounds', type=int, help='Number of rounds')
    args = parser.parse_args()
#    test(args)
    main(args)
