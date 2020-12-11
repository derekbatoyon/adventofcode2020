import fileinput

def count_arrangements(start, jolts):
    if len(jolts) == 0:
        return 1
    count = 0
    for i in range(len(jolts)):
        j = jolts[i]
        if j <= start+3:
            count += count_arrangements(j, jolts[i+1:])
    return count

def calculate_arrangements(streak):
    if streak in cache:
        return cache[streak]
    simulated_jolts = list(range(3, streak+4)) + [streak+6]
    count = count_arrangements(0, simulated_jolts)
    cache[streak] = count
    return count

def main():
    jolts = sorted([int(line) for line in fileinput.input()])
    end = max(jolts) + 3
    jolts = jolts + [end]

    streak = 0
    arrangements = 1
    last_jolt = 0
    for jolt in jolts:
        difference = jolt - last_jolt
        last_jolt = jolt
        if difference == 1:
            streak += 1
        elif difference == 3:
            arrangements *= calculate_arrangements(streak)
            streak = 0
        else:
            raise RuntimeError
    print(arrangements)

if __name__ == "__main__":
    cache = {}
    main()
