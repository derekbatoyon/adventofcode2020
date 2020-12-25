import fileinput
import re

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
    hexgrid = dict()
    for line in fileinput.input():
        location = (0, 0)
        for direction in parse_direction(line):
            location = move(location, direction)
        try:
            color = hexgrid[location]
        except KeyError:
            color = False
        hexgrid[location] = not color

    print(sum(hexgrid.values()))

if __name__ == "__main__":
    main()
