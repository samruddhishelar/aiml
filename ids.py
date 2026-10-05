# Q17. Iterative Deepening Depth First Search

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': [],
    'E': [],
    'F': [],
    'G': []
}

def depth_limited_search(node, goal, depth, path):

    path.append(node)

    if node == goal:
        return True

    if depth == 0:
        path.pop()
        return False

    for neighbor in graph[node]:
        if depth_limited_search(neighbor, goal, depth - 1, path):
            return True

    path.pop()
    return False


def iddfs(start, goal, max_depth):

    for depth in range(max_depth + 1):

        path = []

        if depth_limited_search(start, goal, depth, path):
            return path

    return None


start = 'A'
goal = 'G'

path = iddfs(start, goal, 5)

print("Path:", " -> ".join(path))