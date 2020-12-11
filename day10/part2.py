import fileinput

# This is not useful for large amounts of data.
def count_arrangements(start, jolts, arrangements=[]):
    if len(jolts) == 0:
        return 1
    count = 0
    for i in range(len(jolts)):
        j = jolts[i]
        if j <= start+3:
            count += count_arrangements(j, jolts[i+1:], arrangements + [j])
    return count

def main():
    jolts = sorted([int(line) for line in fileinput.input()])
    print(count_arrangements(0, jolts))

if __name__ == "__main__":
    main()
