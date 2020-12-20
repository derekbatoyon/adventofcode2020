import fileinput
import math
import re

def ToInt(lst):
    return sum(pow(2, i) if c == '#' else 0 for i, c in enumerate(lst))

class Tile(object):
    def __init__(self, tileid, data):
        length = len(data)
        assert all(len(row) == length for row in data)

        self.tileid = tileid
        self.front = [
            ToInt(reversed(data[0])),
            ToInt(reversed([row[-1] for row in data])),
            ToInt(data[-1]),
            ToInt([row[0] for row in data]),
        ]
        self.back = [
            ToInt(data[0]),
            ToInt(reversed([row[0] for row in data])),
            ToInt(reversed(data[-1])),
            ToInt([row[-1] for row in data]),
        ]

def read_tiles():
    tileid_regex = re.compile('Tile\s+(?P<tileid>\d+):$')

    def read_tile(input):
        tileid = None
        data = []
        for line in input:
            if line.isspace():
                yield Tile(tileid, data)
                tileid = None
                data = []
            elif m := tileid_regex.match(line):
                tileid = int(m.group('tileid'))
            else:
                data.append(line.strip())
        if len(data):
            yield Tile(tileid, data)

    return [tile for tile in read_tile(fileinput.input())]

def find_corners(tiles):
    corners = []
    for tile1 in tiles:
        common_edges = 0
        for edge in tile1.front:
            for tile2 in tiles:
                if tile1.tileid != tile2.tileid:
                    if edge in tile2.front or edge in tile2.back:
                        common_edges += 1
        if common_edges == 2:
            corners.append(tile1)
    return corners

def main():
    tiles = read_tiles()
    corners = find_corners(tiles)

    print(math.prod(tile.tileid for tile in corners))

if __name__ == "__main__":
    main()
