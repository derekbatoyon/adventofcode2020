import fileinput
import re
import sys

class HexGrid:
    def __init__(self):
        self.grid = dict()

    def flip(self, location):
        try:
            color = self.grid[location]
        except KeyError:
            color = False
        self.grid[location] = not color

    def test(self, location):
        try:
            color = self.grid[location]
        except KeyError:
            color = False
        return color

    def cycle(self):
        directions = ['e', 'w', 'ne', 'nw', 'se', 'sw']
        maybe_flip_to_black = set()
        flip_to_black = []
        flip_to_white = []
        black_tiles = [location for location, color in self.grid.items() if color]
        for black_tile in black_tiles:
            adjacent_count = 0
            adjacents = [move(black_tile, direction) for direction in directions]
            for adjacent in adjacents:
                if self.test(adjacent):
                    adjacent_count += 1
                else:
                    maybe_flip_to_black.add(adjacent)
            if adjacent_count == 0 or adjacent_count > 2:
                flip_to_white.append(black_tile)
        for white_tile in maybe_flip_to_black:
            adjacents = [move(white_tile, direction) for direction in directions]
            adjacent_count = sum(self.test(adjacent) for adjacent in adjacents)
            if adjacent_count == 2:
                flip_to_black.append(white_tile)

        for white_tile in flip_to_black:
            self.grid[white_tile] = True
        for black_tile in flip_to_white:
            self.grid[black_tile] = False

    def count(self):
        return sum(self.grid.values())

def parse_direction(line):
    direction_regex = re.compile('(e|se|sw|w|nw|ne)')
    pos = 0
    while m := direction_regex.match(line, pos):
        yield m.group(1)
        pos = m.end()

def move(location, direction):
    x, y = location
    if y % 2 == 0:
        return {
            'e': lambda x, y: (x+1, y),
            'w': lambda x, y: (x-1, y),
            'ne': lambda x, y: (x, y+1),
            'nw': lambda x, y: (x-1, y+1),
            'se': lambda x, y: (x, y-1),
            'sw': lambda x, y: (x-1, y-1),
        }[direction](x, y)
    else:
        return {
            'e': lambda x, y: (x+1, y),
            'w': lambda x, y: (x-1, y),
            'ne': lambda x, y: (x+1, y+1),
            'nw': lambda x, y: (x, y+1),
            'se': lambda x, y: (x+1, y-1),
            'sw': lambda x, y: (x, y-1),
        }[direction](x, y)

def main():
    hexgrid = HexGrid()
    for line in fileinput.input():
        location = (0, 0)
        for direction in parse_direction(line):
            location = move(location, direction)
        hexgrid.flip(location)

    sys.stderr.write('Day {}: {}\n'.format(0, hexgrid.count()))
    for day in range(100):
        hexgrid.cycle()
        sys.stderr.write('Day {}: {}\n'.format(day+1, hexgrid.count()))

    print(hexgrid.count())

if __name__ == "__main__":
    main()
