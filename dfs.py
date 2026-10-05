# Q6. DFS Traversal for a Graph

graph = {
    'A': ['B', 'C', 'E'],
    'B': ['A', 'D'],
    'C': ['A', 'F'],
    'D': ['B', 'E'],
    'E': ['A', 'D', 'F'],
    'F': ['C', 'E']
}

def dfs(node, visited):
    if node not in visited:
        print(node, end=" ")
        visited.add(node)

        for neighbor in graph[node]:
            dfs(neighbor, visited)

visited = set()

print("DFS Traversal:")
dfs('A', visited)