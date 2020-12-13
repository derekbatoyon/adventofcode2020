import fileinput
import math
import numpy as np

def check(result):
    for x in result:
        (f, _) = math.modf(x)
        if not math.isclose(f, 0.0):
            return False
    return True

def test(time, bus_matrix, offset_matrix):
    times = offset_matrix + time
    result = np.linalg.solve(bus_matrix, times)
    return check(result)

def process(buses):
    interval = max(buses)

    offset = buses[interval]
    offset_matrix = np.array([t - offset for t in buses.values()])

    bus_count = len(buses)
    bus_matrix = np.zeros((bus_count, bus_count))
    for i, bus in enumerate(buses):
        bus_matrix[i][i] = bus

    count = 1
    while not test(count * interval, bus_matrix, offset_matrix):
        count += 1

    print(count * interval + offset_matrix[0])

def main():
    input = fileinput.input()
    line = input.readline()
    if ',' not in line:
        line = input.readline()

    buses = dict()
    for i, bus in enumerate(line.split(',')):
        if bus != 'x':
            buses[int(bus)] = i

    process(buses)

if __name__ == "__main__":
    main()
