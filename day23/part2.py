import sys

from graphviz import Digraph

class Node:
    everything = []
    def __init__(self, value):
        Node.everything.append(self)
        self.prev = None
        self.next = None
        self.value = value
    def __iter__(self):
        yield self.value
        ptr = self.next
        while ptr is not None and ptr != self:
            yield ptr.value
            ptr = ptr.next
    def Next(self, n=1):
        node = self
        for i in range(n):
            node = node.next
        return node
    def Prev(self, n=1):
        node = self
        for i in range(n):
            node = node.prev
        return node
    def Graph(name, highlight=None):
        dot = Digraph(filename=name, format='pdf')
        for node in Node.everything:
            penwidth = 2.0 if node == highlight else 1.0
            dot.node(str(node.value), penwidth=str(penwidth))
            if node.next:
                dot.edge(str(node.value), str(node.next.value))
            if node.prev:
                dot.edge(str(node.value), str(node.prev.value))
        print(dot.render(cleanup=True))

def print_cups(f, cups, special_label=None):
    f.write('cups: ')
    for label in cups:
        format = '({})' if label == special_label else ' {} '
        f.write(format.format(label))
    f.write('\n')

def extract(extraction_point, n=3):
    remove = extraction_point.Next()
    keep = remove.Next(n)

    extraction_point.next = keep
    remove.prev = None
    keep.prev.next = None
    keep.prev = extraction_point

    return remove

def insert(insertion_point, new):
    remaining = insertion_point.Next()
    insertion_point.next = new
    new.prev = insertion_point
    while new.next:
        new = new.next
    new.next = remaining
    remaining.prev = new

def find_label(ptr, label):
    while ptr and ptr.value != label:
        ptr = ptr.next
    return ptr

def main(args):
    starting_cups = [int(c) for c in args.cups]
    minimum_label = min(starting_cups)
    maximum_label = max(starting_cups)
    maximum_label = maximum_label if args.maximum is None else max(maximum_label, args.maximum)

    cups = [None] * (maximum_label + 1)

    cups[starting_cups[0]] = current_cup = last_cup = Node(starting_cups[0])
    for cup_label in starting_cups[1:]:
        cups[cup_label] = cup = Node(cup_label)
        cup.prev = last_cup
        last_cup.next = cup
        last_cup = cup
    if args.maximum:
        for i in range(max(starting_cups), maximum_label):
            cup_label = i + 1
            cups[cup_label] = cup = Node(cup_label)
            cup.prev = last_cup
            last_cup.next = cup
            last_cup = cup
    last_cup.next = current_cup
    current_cup.prev = last_cup

    for move in range(args.moves):
        if args.debug:
            sys.stderr.write('-- move {} --\n'.format(move+1))
            if args.graph:
                Node.Graph('cups_move_{}'.format(move+1), current_cup)
            first_print_offset = move % len(starting_cups)
            print_cups(sys.stderr, current_cup.Prev(first_print_offset), current_cup.value)

        pickup = extract(current_cup)
        if args.debug:
            sys.stderr.write('pick up: {}\n'.format(', '.join(str(value) for value in pickup)))
            if args.graph:
                Node.Graph('pickup_move_{}'.format(move+1), current_cup)

        destination_label = current_cup.value - 1
        if destination_label < minimum_label:
            destination_label = maximum_label
        while find_label(pickup, destination_label):
            destination_label -= 1
            if destination_label < minimum_label:
                destination_label = maximum_label
        destination = cups[destination_label]

        if args.debug:
            sys.stderr.write('destination: {}\n\n'.format(destination.value))

        insert(destination, pickup)
        current_cup = current_cup.next

    if args.debug:
        sys.stderr.write('-- final --\n')
        if args.graph:
            Node.Graph('final', current_cup)
        first_print_offset = (move+1) % len(starting_cups)
        print_cups(sys.stderr, current_cup.Prev(first_print_offset), current_cup.value)

    label1 = cups[1].next.value
    label2 = cups[1].next.next.value
    if args.debug:
        sys.stderr.write('{} x {}\n'.format(label1, label2))
    print(label1 * label2)

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description='Crab Cups')
    parser.add_argument('cups', metavar='C', type=str, help='initial labeling')
    parser.add_argument('--moves', dest='moves', type=int,  default=10, help='the numebr of moves to execute')
    parser.add_argument('--max', dest='maximum', type=int, help='the highest numbered cup label')
    parser.add_argument('--debug', action='store_true', help='enable debug output')
    parser.add_argument('--graph', action='store_true', help='enable graph output')
    args = parser.parse_args()
    main(args)
