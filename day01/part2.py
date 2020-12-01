import fileinput

def main():
    target_sum = 2020

    values = []
    for line in fileinput.input():
        value = int(line)
        if value <= 2020:
            values.append(value)

    n = len(values)
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                x = values[i]
                y = values[j]
                z = values[k]
                if x + y + z == target_sum:
                    print(x * y * z)

if __name__ == "__main__":
    main()
