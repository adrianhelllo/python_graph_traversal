class Graph:
    def __init__(self, size):
        self.adjacency_matrix = [[None] * size for _ in range(size)]
        self.vertex_data = [''] * size
        self.size = size

    def add_vertex_data(self, vertex, data):
        if 0 <= vertex < self.size:
            self.vertex_data[vertex] = data

    def add_edge(self, f, t, weight):
        if 0 <= f < self.size and 0 <= t < self.size:
            self.adjacency_matrix[f][t] = weight

    def print_graph(self):
        print("Adj. Matrix:")
        for row in self.adjacency_matrix:
            print(' '.join(map(lambda x: str(x) if x is not None else '-', row)))
        print("Vertex data:")
        for vertex, data in enumerate(self.vertex_data):
            print(f"Vertex {vertex}: {data}")

    def dfs_util(self, v, visited):
        visited[v] = True
        print(self.vertex_data[v], end=' ')

        for i in range(self.size):
            if self.adjacency_matrix[v][i] is not None and not visited[i]:
                self.dfs_util(i, visited)

    def dfs(self, start_vertex_data):
        visited = [False] * self.size
        start_vertex = self.vertex_data.index(start_vertex_data)
        self.dfs_util(start_vertex, visited)

    def bfs(self, start_vertex_data):
        queue = [self.vertex_data.index(start_vertex_data)]
        visited = [False] * self.size
        visited[queue[0]] = True

        while queue:
            current_vertex = queue.pop(0)
            print(self.vertex_data[current_vertex], end=" ")

            for i in range(self.size):
                if self.adjacency_matrix[current_vertex][i] is not None and not visited[i]:
                    queue.append(i)
                    visited[i]

g = Graph(4)
g.add_vertex_data(0, 'A')
g.add_vertex_data(1, 'B')
g.add_vertex_data(2, 'C')
g.add_vertex_data(3, 'D')
g.add_edge(0, 1, 0)
g.add_edge(0, 3, 1)
g.add_edge(1, 0, 2)
g.add_edge(1, 2, 3)
g.add_edge(2, 3, 4)

g.print_graph()

g.bfs('C')