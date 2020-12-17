import fileinput

def neighbor_offets():
    s = (-1, 0, 1)
    for x in s:
        for y in s:
            for z in s:
                for w in s:
                    if x != 0 or y != 0 or z != 0 or w != 0:
                        yield x, y, z, w

def determine_state(cubes, cube):
    active_count = 0
    for offset in neighbor_offets():
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
    xmin = xmax = ymin = ymax = zmin = zmax = wmin = wmax = None
    for x, y, z, w in cubes:
        xmin = x if xmin is None or x < xmin else xmin
        xmax = x if xmax is None or x > xmax else xmax
        ymin = y if ymin is None or y < ymin else ymin
        ymax = y if ymax is None or y > ymax else ymax
        zmin = z if zmin is None or z < zmin else zmin
        zmax = z if zmax is None or z > zmax else zmax
        wmin = w if wmin is None or w < wmin else wmin
        wmax = w if wmax is None or w > wmax else wmax
    return xmin, xmax, ymin, ymax, zmin, zmax, wmin, wmax

def get_initial_state():
    cubes = set()
    input = [line.strip() for line in fileinput.input()]
    for y, line in enumerate(input):
        for x, state in enumerate(line):
            if state == '#':
                cubes.add((x, y, 0, 0))
    return cubes

def run_cycle(cubes):
    new_cubes = set()
    xmin, xmax, ymin, ymax, zmin, zmax, wmin, wmax = find_bounds(cubes)
    for x in range(xmin-1, xmax+2):
        for y in range(ymin-1, ymax+2):
            for z in range(zmin-1, zmax+2):
                for w in range(wmin-1, wmax+2):
                    cube = (x, y, z, w)
                    if determine_state(cubes, cube):
                        new_cubes.add(cube)
    return new_cubes

def main():
    cubes = get_initial_state()

    for i in range(6):
        cubes = run_cycle(cubes)

    print(len(cubes))

if __name__ == "__main__":
    main()
