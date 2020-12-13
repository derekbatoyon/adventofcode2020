import fileinput
import math

def find_next_bus(departure_time, bus_schedule):
    bus_id = None
    closest = 0.0
    for id in bus_schedule:
        (f, _) = math.modf(departure_time / id)
        if f > closest:
            closest = f
            time = id * math.ceil(departure_time / id)
            bus_id = id

    wait = time - departure_time
    print(bus_id * wait)

def main():
    input = fileinput.input()
    departure_time = int(input.readline())
    bus_schedule = [int(id) for id in input.readline().split(',') if id != 'x']
    find_next_bus(departure_time, bus_schedule)

if __name__ == "__main__":
    main()
