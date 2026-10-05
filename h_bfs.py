# Q15. Best First Search

from queue import PriorityQueue

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B', 'F'],
    'E': ['B', 'F'],
    'F': ['C', 'D', 'E']
}

h = {
    'A': 6,
    'B': 5,
    'C': 3,
    'D': 2,
    'E': 1,
    'F': 0
}

def best_first_search(start, goal):
    queue = PriorityQueue()
    queue.put((h[start], start))

    visited = set()
    parent = {start: None}

    while not queue.empty():
        _, current = queue.get()

        if current in visited:
            continue

        visited.add(current)
        print(current, end=" ")

        if current == goal:
            break

        for neighbor in graph[current]:
            if neighbor not in visited:
                parent[neighbor] = current
                queue.put((h[neighbor], neighbor))

    path = []
    current = goal

    while current is not None:
        path.append(current)
        current = parent.get(current)

    path.reverse()
    return path

start = 'A'
goal = 'F'

print("Best First Search Traversal:")
path = best_first_search(start, goal)

print("\n\nPath:", " -> ".join(path))

