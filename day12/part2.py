import fileinput
import re

# left means rotate counter-clockwise
# 0 steps            1 step             2 steps                 3 steps
# ....w..            .......            .......            .......
# .......            w......            .......            .......
# ...s... => left => ...s... => left => ...s... => left => ...s...
# .......            .......            .......            ......w
# .......            .......            ..w....            .......
#  (1, 2)            (-2, 1)           (-1 ,-2)            (2, -1)

counterclockwise = {
    0: lambda x, y: (x, y),
    1: lambda x, y: (-y, x),
    2: lambda x, y: (-x, -y),
    3: lambda x, y: (y, -x),
}

# right means rotate clockwise
# 0 steps             1 step              2 steps             3 steps
# ....w..             .......             .......             .......
# .......             .......             .......             w......
# ...s... => right => ...s... => right => ...s... => right => ...s...
# .......             ......w             .......             .......
# .......             .......             ..w....             .......
#  (1, 2)             (2, -1)            (-1 ,-2)             (-2, 1)

clockwise = {
    0: lambda x, y: (x, y),
    1: lambda x, y: (y, -x),
    2: lambda x, y: (-x, -y),
    3: lambda x, y: (-y, x),
}

def process(command, argument, ship, waypoint):
    longitude = waypoint[0]
    latitude = waypoint[1]
    if command == 'N':
        return ship, (longitude, latitude + argument)
    if command == 'S':
        return ship, (longitude, latitude - argument)
    if command == 'E':
        return ship, (longitude + argument, latitude)
    if command == 'W':
        return ship, (longitude - argument, latitude)

    if command == 'L':
        (quotient, remainder) = divmod(argument, 90)
        assert(remainder == 0)
        (longitude, latitude) = counterclockwise[quotient % 4](longitude, latitude)
        return ship, (longitude, latitude)

    if command == 'R':
        (quotient, remainder) = divmod(argument, 90)
        assert(remainder == 0)
        (longitude, latitude) = clockwise[quotient % 4](longitude, latitude)
        return ship, (longitude, latitude)

    if command == 'F':
        x = ship[0]
        y = ship[1]
        x += longitude * argument
        y += latitude * argument
        return (x, y), waypoint

def main():
    regex = re.compile('(?P<command>\w)(?P<argument>\d+)')

    ship = (0, 0)
    waypoint = (10, 1)

    for line in fileinput.input():
        m = regex.match(line)
        ship, waypoint = process(m.group('command'), int(m.group('argument')), ship, waypoint)

    print(abs(ship[0]) + abs(ship[1]))

if __name__ == "__main__":
    main()
