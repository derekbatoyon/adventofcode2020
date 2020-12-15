import sys

def play(arg, until=30000000):
    numbers = [int(n) for n in arg.split(',')]
    turn = len(numbers)

    last = numbers.pop(-1)
    memory = {n: i+1 for i, n in enumerate(numbers)}

    while turn < until:
        if last in memory:
            speak = turn - memory[last]
        else:
            speak = 0
        memory[last] = turn
        turn += 1
        last = speak

    print(last)

if __name__ == "__main__":
    for arg in sys.argv[1:]:
        play(arg)
