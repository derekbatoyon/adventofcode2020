import fileinput
import sys

def rotate_left(seq, n=1):
    for i in range(n):
        first = seq.pop(0)
        seq.append(first)

def rotate_right(seq, n=1):
    for i in range(n):
        last = seq.pop()
        seq.insert(0, first)

def print_cups(f, cups, current):
    f.write('cups: ')
    for cup in cups:
        if cup == current:
            f.write('({})'.format(cup))
        else:
            f.write(' {} '.format(cup))
    f.write('\n')

def main(args):
    cups = [int(c) for c in args.cups]
    current = cups[0]

    for move in range(args.moves):
        sys.stderr.write('-- move {} --\n'.format(move+1))
        print_cups(sys.stderr, cups, current)

        current_index = cups.index(current)
        picked_up = cups[current_index+1:current_index+4]
        del cups[current_index+1:current_index+4]
        picked_up_count = len(picked_up)
        if picked_up_count < 3:
            picked_up[picked_up_count:picked_up_count] = cups[0:3-picked_up_count]
            del cups[0:3-picked_up_count]

        destination = current-1
        minimum = min(cups)
        while destination not in cups:
            destination -= 1
            if destination < minimum:
                destination = max(cups)
                break

        index = cups.index(destination) + 1
        cups[index:index] = picked_up

        current_index = cups.index(current)
        current = cups[(current_index+1)%len(cups)]

        sys.stderr.write('pick up: {}'.format(picked_up[0]))
        for cup in picked_up[1:]:
            sys.stderr.write(', {}'.format(cup))
        sys.stderr.write('\ndestination: {}\n\n'.format(destination))

        index = move % 10
        if index < current_index:
            rotate_left(cups, current_index-index)
        elif index > current_index:
            rotate_right(cups, current_index-index)

    sys.stderr.write('-- final --\n'.format(move))
    print_cups(sys.stderr, cups, current)

    index = cups.index(1)
    print('{}{}'.format(''.join(str(n) for n in cups[index+1:]), ''.join(str(n) for n in cups[0:index])))

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description='Crab Cups')
    parser.add_argument('cups', metavar='C', type=str, help='initial labeling')
    parser.add_argument('--moves', dest='moves', type=int,  default=10, help='the numebr of moves to execute')
    args = parser.parse_args()
    main(args)
