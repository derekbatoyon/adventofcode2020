import fileinput
import sys

neighbor_offets = [
    (-1, -1, -1),
    (-1, -1,  0),
    (-1, -1,  1),
    (-1,  0, -1),
    (-1,  0,  0),
    (-1,  0,  1),
    (-1,  1, -1),
    (-1,  1,  0),
    (-1,  1,  1),
    ( 0, -1, -1),
    ( 0, -1,  0),
    ( 0, -1,  1),
    ( 0,  0, -1),
    ( 0,  0,  1),
    ( 0,  1, -1),
    ( 0,  1,  0),
    ( 0,  1,  1),
    ( 1, -1, -1),
    ( 1, -1,  0),
    ( 1, -1,  1),
    ( 1,  0, -1),
    ( 1,  0,  0),
    ( 1,  0,  1),
    ( 1,  1, -1),
    ( 1,  1,  0),
    ( 1,  1,  1),
]

def determine_state(cubes, cube):
    active_count = 0
    for offset in neighbor_offets:
        neighbor = tuple(a+b for a, b in zip(cube, offset))
        if neighbor in cubes:
            active_count += 1

    if cube in cubes:
        # If a cube is active and exactly 2 or 3 of its neighbors are also active,
        # the cube remains active. Otherwise, the cube becomes inactive.
        return active_count == 2 or active_count == 3
    else:
        # If a cube is inactive but exactly 3 of its neighbors are active, the
        # cube becomes active. Otherwise, the cube remains inactive.
        return active_count == 3

def find_bounds(cubes):
    xmin = xmax = ymin = ymax = zmin = zmax = None
    for x, y, z in cubes:
        xmin = x if xmin is None or x < xmin else xmin
        xmax = x if xmax is None or x > xmax else xmax
        ymin = y if ymin is None or y < ymin else ymin
        ymax = y if ymax is None or y > ymax else ymax
        zmin = z if zmin is None or z < zmin else zmin
        zmax = z if zmax is None or z > zmax else zmax
    return xmin, xmax, ymin, ymax, zmin, zmax

def get_initial_state():
    cubes = set()
    input = [line.strip() for line in fileinput.input()]
    for y, line in enumerate(input):
        for x, state in enumerate(line):
            if state == '#':
                cubes.add((x, y, 0))
    return cubes

def run_cycle(cubes):
    new_cubes = set()
    xmin, xmax, ymin, ymax, zmin, zmax = find_bounds(cubes)
    for x in range(xmin-1, xmax+2):
        for y in range(ymin-1, ymax+2):
            for z in range(zmin-1, zmax+2):
                cube = (x, y, z)
                if determine_state(cubes, cube):
                    new_cubes.add(cube)
    return new_cubes

def print_cubes(cubes):
    xmin, xmax, ymin, ymax, zmin, zmax = find_bounds(cubes)
    letter = {True: '#', False: '.'}
    for z in range(zmin, zmax+1):
        sys.stderr.write('\nz={}\n'.format(z))
        for y in range(ymin, ymax+1):
            line = ''.join(letter[(x, y, z) in cubes] for x in range(xmin, xmax+1))
            sys.stderr.write('{}\n'.format(line))

def main():
    cubes = get_initial_state()
    sys.stderr.write('Before any cycles:\n')
    print_cubes(cubes)

    for i in range(6):
        cubes = run_cycle(cubes)
        sys.stderr.write('\n\nAfter {} cycle:\n'.format(i+1))
        print_cubes(cubes)

    print(len(cubes))

if __name__ == "__main__":
    main()
