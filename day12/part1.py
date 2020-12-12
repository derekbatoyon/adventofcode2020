import fileinput
import re

left_turns = {
    'N': 'NWSE',
    'W':  'WSEN',
    'S':   'SENW',
    'E':    'ENWS',
}

right_turns = {
    'N': 'NESW',
    'E':  'ESWN',
    'S':   'SWNE',
    'W':    'WNES',
}

def process(command, argument, direction, longitude, latitude):
    if command == 'N':
        return direction, longitude, latitude + argument
    if command == 'S':
        return direction, longitude, latitude - argument
    if command == 'E':
        return direction, longitude + argument, latitude
    if command == 'W':
        return direction, longitude - argument, latitude
    if command == 'L':
        (quotient, remainder) = divmod(argument, 90)
        assert(remainder == 0)
        new_direction = left_turns[direction][quotient % 4]
        return new_direction, longitude, latitude
    if command == 'R':
        (quotient, remainder) = divmod(argument, 90)
        assert(remainder == 0)
        new_direction = right_turns[direction][quotient % 4]
        return new_direction, longitude, latitude
    if command == 'F':
        return process(direction, argument, direction, longitude, latitude)

def main():
    regex = re.compile('(?P<command>\w)(?P<argument>\d+)')

    direction = 'E'
    longitude = 0
    latitude = 0

    for line in fileinput.input():
        m = regex.match(line)
        direction, longitude, latitude = process(m.group('command'), int(m.group('argument')), direction, longitude, latitude)

    print(abs(longitude) + abs(latitude))

if __name__ == "__main__":
    main()
