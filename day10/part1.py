import fileinput

def main():
    count1 = 0
    count3 = 1
    jolts = [0] + sorted([int(line) for line in fileinput.input()])
    for i in range(1, len(jolts)):
        difference = jolts[i] - jolts[i-1]
        if difference == 1:
            count1 += 1
        elif difference == 3:
            count3 += 1
        else:
            raise RuntimeError
    print(count1 * count3)

if __name__ == "__main__":
    main()
