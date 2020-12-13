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
    interval = 1
    time = 0

    for bus_count in range(2, len(buses)+1):
        interval *= list(buses.keys())[bus_count-2]
        bus_matrix = np.zeros((bus_count, bus_count))
        for i, bus in enumerate(buses):
            if i == bus_count: break
            bus_matrix[i][i] = bus
        offset_matrix = np.array(list(buses.values())[:bus_count])

        while not test(time, bus_matrix, offset_matrix):
            time += interval

    print(time)

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
