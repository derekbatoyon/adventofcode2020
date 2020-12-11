import fileinput

def main():
    count1 = 0
    count3 = 1
    jolts = sorted([int(line) for line in fileinput.input()])
    last_jolt = 0
    for jolt in jolts:
        difference = jolt - last_jolt
        last_jolt = jolt
        if difference == 1:
            count1 += 1
        elif difference == 3:
            count3 += 1
        else:
            raise RuntimeError
    print(count1 * count3)

if __name__ == "__main__":
    main()
