# Q5. Depth Limited Search (DLS)

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': [],
    'F': []
}

def dls(node, goal, depth):
    if node == goal:
        return True

    if depth <= 0:
        return False

    for neighbor in graph[node]:
        if dls(neighbor, goal, depth - 1):
            return True

    return False

start = 'A'
goal = 'F'
limit = 2

if dls(start, goal, limit):
    print("Goal Found")
else:
    print("Goal Not Found")