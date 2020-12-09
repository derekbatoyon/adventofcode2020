def valid(next, numbers):
    for i in range(len(numbers)):
        for j in range(i, len(numbers)):
            if numbers[i] + numbers[j] == next:
                return True
    return False

def process(numbers, preamble):
    for step, target in enumerate(numbers[preamble:]):
        if not valid(target, numbers[step:step+preamble]):
            break
    for i in range(len(numbers)):
        sum = 0
        for j in range(i, len(numbers)):
            sum += numbers[j]
            if sum == target:
                subset = numbers[i:j+1]
                print(min(subset) + max(subset))
                return
            elif sum > target:
                break

def main(args):
    with open(args.input, "r") as input:
        numbers = [int(line) for line in input]
    process(numbers, args.preamble)

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('input', help='Input files')
    parser.add_argument('-p', '--preamble', type=int, default=25, help='Length of preamble')
    args = parser.parse_args()
    main(args)
