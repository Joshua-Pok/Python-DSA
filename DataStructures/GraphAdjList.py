from collections import deque
class GraphAdjList: 
    def __init__(self):
        self.graph = {}

    def add_vertex(self, v):
        if v not in self.graph:
            self.graph[v] = []

    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def display(self):
        for vertex in self.graph:
            print(vertex, "->",  self.graph[vertex])


    def BFS(self, start):
        visited = set()
        queue = deque([start]) # Creates a list with one element, starting node.
        result = []

        while queue:
            vertex = queue.popleft();
            if vertex not in visited:
                visited.add(vertex)
                result.append(vertex)
                queue.extend(self.graph[vertex]) #append children to the queue
        return result


