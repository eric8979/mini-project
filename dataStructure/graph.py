# Original code from...
# https://stackabuse.com/courses/graphs-in-python-theory-and-implementation/lessons/representing-graphs-in-code/

# Ways to represent Graphs
    # List of Edges
    # Adjacency Matrix
    # Adjacency List <-- Implemented below!

class Graph:
    def __init__(self, nodeCount, directed=True):
        self.nodeCount = nodeCount
        self.directed = directed
        self.adj_list = {node: set() for node in range(self.nodeCount)}

    def add_edge(self, node1, node2, weight=1):
        self.adj_list[node1].add((node2, weight))
        if not self.directed:
            self.adj_list[node2].add((node1, weight))

    def print_adj_list(self):
        for key in self.adj_list.keys():
            print("node", key, ": ", self.adj_list[key])

graph = Graph(5)

graph.add_edge(0, 0, 25)
graph.add_edge(0, 1, 5)
graph.add_edge(0, 2, 3)
graph.add_edge(1, 3, 1)
graph.add_edge(1, 4, 15)
graph.add_edge(4, 2, 7)
graph.add_edge(4, 3, 11)

graph.print_adj_list()

# node(vertex): {(node, weight), (node, weight), ...}
# set: {}
# tuple: ()
