class Graph:
    def __init__(self, graph) -> None:
        if graph is None:
            self.graph = {}
        self.graph = graph
    
    def add(self, vertex, edge):
        self.graph[vertex].append(edge)

    def breadthFirstSearch(self, vertex):
        visited = [vertex]
        queue = [vertex]
        while queue:
            dequeueVertex = queue.pop(0)
            print(dequeueVertex)
            for adjacentVertex in self.graph[dequeueVertex]:
                if adjacentVertex not in visited:
                    visited.append(adjacentVertex)
                    queue.append(adjacentVertex)


customGraph = {
    'a': ['b', 'c'],
    'b': ['a', 'd', 'e'],
    'c': ['a', 'e'],
    'd': ['b', 'e', 'f'],
    'e': ['d', 'f'],
    'f': ['d', 'e']
}

graph = Graph(customGraph)
graph.breadthFirstSearch('a')

    