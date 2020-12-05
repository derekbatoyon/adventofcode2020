import fileinput
import re

def main():
    regex = re.compile('([FB]{7})([LR]{3})$')
    trans = str.maketrans('FBLR', '0101')

    max = None
    for line in fileinput.input():
        m = regex.match(line)
        if m:
            id = int(line.translate(trans), 2)
            if max is None or id > max:
                max = id

    print(max)

if __name__ == "__main__":
    main()
