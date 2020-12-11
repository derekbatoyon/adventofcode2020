import fileinput

# This hacked-up mess was used to solve the puzzle.
def count_arrangements(start, jolts, arrangements=[]):
    if len(jolts) == 0:
        return 1
    count = 0
    for i in range(len(jolts)):
        j = jolts[i]
        if j <= start+3:
            count += count_arrangements(j, jolts[i+1:], arrangements + [j])
    return count

def calculate_arrangements(streak):
    if streak in cache:
        return cache[streak]
    simulated_jolts = list(range(3, 3+streak)) + [streak+5]
    count = count_arrangements(0, simulated_jolts)
    cache[streak] = count
    return count

def main():
    jolts = [0] + sorted([int(line) for line in fileinput.input()])
    end = max(jolts) + 3
    jolts = jolts + [end]
    differences = [jolts[i] - jolts[i-1] for i in range(1, len(jolts))]
    print(differences)
    streak = 0
    arrangements = 1
    for difference in differences:
        if difference == 1:
            streak += 1
        elif difference == 3:
            if streak > 0:
                arrangements *= calculate_arrangements(streak+1)
                print(streak, calculate_arrangements(streak+1))
                streak = 0
    print('answer:', arrangements)

if __name__ == "__main__":
    cache = {}
    main()
