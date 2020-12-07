import fileinput
import re

class Graph(object):
    def __init__(self):
        self.graph = dict()

    def add_edge(self, tail, head):
        if tail not in self.graph:
            self.graph[tail] = set()
        self.graph[tail].add(head)

    def edges(self, tail):
        result = set()
        for head in self.edges_helper(tail):
            result.add(head)
        return result

    def edges_helper(self, tail):
        if tail in self.graph:
            for head in self.graph[tail]:
                yield head
                yield from self.edges_helper(head)

    def dump(self):
        for tail, head in self.graph.items():
            print(tail, '=>', head)

def main():
    container_re = re.compile('(?P<color>\w+ \w+) bags contain')
    containee_re = re.compile('(?P<count>\d+) (?P<color>\w+ \w+) bags?')

    graph = Graph()
    for line in fileinput.input():
        m = container_re.match(line)
        container = m.group('color')
        end = m.end()
        while m := containee_re.search(line, end):
            containee = m.group('color')
            graph.add_edge(containee, container)
            end = m.end()

    #graph.dump()

    print(len(graph.edges('shiny gold')))

if __name__ == "__main__":
    main()
