def valid(next, numbers):
    for i in range(len(numbers)):
        for j in range(i, len(numbers)):
            if numbers[i] + numbers[j] == next:
                return True
    return False

def main(args):
    numbers = [0] * args.preamble
    with open(args.input, "r") as input:
        for i in range(args.preamble):
            numbers[i] = int(input.readline())

        for line in input:
            next_number = int(line)
            if valid(next_number, numbers):
                numbers = numbers[1:] + [next_number]
            else:
                print(next_number)
                break

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('input', help='Input files')
    parser.add_argument('-p', '--preamble', type=int, default=25, help='Length of preamble')
    args = parser.parse_args()
    main(args)
