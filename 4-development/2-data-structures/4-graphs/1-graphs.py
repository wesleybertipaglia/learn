# Ordered: No (nodes and edges do not have a strict order)
# Mutable: Yes
# Duplicates: Edges can be duplicated (depending on the type of graph)
# Indexing: No (nodes and edges are typically accessed through traversal)
# Different Data Types: Yes (nodes and edges can hold various types of data)

class Graph:
    def __init__(self):
        self.graph = {}

    # Add a node to the graph
    def add_node(self, node):
        if node not in self.graph:
            self.graph[node] = []

    # Add an edge between two nodes
    def add_edge(self, node1, node2):
        if node1 not in self.graph:
            self.add_node(node1)
        if node2 not in self.graph:
            self.add_node(node2)
        self.graph[node1].append(node2)
        self.graph[node2].append(node1)

    # Print the graph
    def print_graph(self):
        for node in self.graph:
            print(f"{node}: {self.graph[node]}")

    # Perform a depth-first search (DFS)
    def dfs(self, start):
        visited = set()
        self._dfs_recursive(start, visited)

    def _dfs_recursive(self, node, visited):
        if node not in visited:
            print(node, end=' ')
            visited.add(node)
            for neighbor in self.graph[node]:
                if neighbor not in visited:
                    self._dfs_recursive(neighbor, visited)

    # Perform a breadth-first search (BFS)
    def bfs(self, start):
        visited = set()
        queue = [start]
        while queue:
            node = queue.pop(0)
            if node not in visited:
                print(node, end=' ')
                visited.add(node)
                queue.extend(neighbor for neighbor in self.graph[node] if neighbor not in visited)

# Create a graph and perform operations
graph = Graph()
graph.add_edge('A', 'B')
graph.add_edge('A', 'C')
graph.add_edge('B', 'D')
graph.add_edge('C', 'D')
graph.add_edge('D', 'E')

# Print the graph
graph.print_graph()
# Output:
# A: ['B', 'C']
# B: ['A', 'D']
# C: ['A', 'D']
# D: ['B', 'C', 'E']
# E: ['D']

# Perform DFS and BFS
print("\nDFS:")
graph.dfs('A')  # Output: A B D C E 

print("\nBFS:")
graph.bfs('A')  # Output: A B C D E
