class Graph:
    def __init__(self, size):
        self.adjacency_matrix = [[0] * size for _ in range(size)]
        self.vertex_data = [''] * size
        self.size = size

    def add_vertex_data(self, vertex, data):
        if 0 <= vertex < self.size:
            self.vertex_data[vertex] = data

    def add_edge(self, f, t):
        if 0 <= f < self.size and 0 <= t < self.size:
            self.adjacency_matrix[f][t] = 1
            self.adjacency_matrix[t][f] = 1 #undirectional graph

    def print_graph(self):
        print("Adj. Matrix:")
        for row in self.adjacency_matrix:
            print(' '.join(map(str, row)))
        print("Vertex data:")
        for vertex, data in enumerate(self.vertex_data):
            print(f"Vertex {vertex}: {data}")

g = Graph(4)
g.add_vertex_data(0, 'A')
g.add_vertex_data(1, 'B')
g.add_vertex_data(2, 'C')
g.add_vertex_data(3, 'D')
g.add_edge(0, 1)
g.add_edge(0, 3)
g.add_edge(1, 3)
g.add_edge(1, 2)
g.add_edge(2, 3)

g.print_graph()