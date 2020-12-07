import fileinput
import re

class Edge(object):
    def __init__(self, color, count):
        self.color = color
        self.count = count

class Graph(object):
    def __init__(self):
        self.graph = dict()

    def add_edge(self, tail, head, count):
        if tail not in self.graph:
            self.graph[tail] = set()
        self.graph[tail].add(Edge(head, count))

    def edges(self, tail):
        result = set()
        for edge in self.edges_helper(tail):
            result.add(edge.color)
        return result

    def edges_helper(self, tail):
        if tail in self.graph:
            for edge in self.graph[tail]:
                yield edge
                yield from self.edges_helper(edge.color)

    def count(self, tail):
        total = 0
        if tail in self.graph:
            for edge in self.graph[tail]:
                total += edge.count
                total += edge.count * self.count(edge.color)
        return total

    def dump(self):
        for tail, edge in self.graph.items():
            print(tail, '=>', [head.color for head in edge])

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
            count = int(m.group('count'))
            graph.add_edge(container, containee, count)
            end = m.end()

    #graph.dump()

    print(len(graph.edges('shiny gold')))
    print(graph.count('shiny gold'))

if __name__ == "__main__":
    main()
