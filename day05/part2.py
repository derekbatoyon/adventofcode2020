import fileinput
import re

def main():
    regex = re.compile('([FB]{7})([LR]{3})$')
    trans = str.maketrans('FBLR', '0101')

    ids = [int(line.translate(trans), 2) for line in fileinput.input()]
    ids.sort()

    previous = ids[0]
    for id in ids[1:]:
        if id != previous + 1:
            print(previous + 1)
        previous = id

if __name__ == "__main__":
    main()
