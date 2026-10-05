# Q7. A* Search Algorithm
# Source = V1, Destination = V6

import heapq

graph = {
    'V1': [('V2', 2), ('V3', 4)],
    'V2': [('V1', 2), ('V4', 3)],
    'V3': [('V1', 4), ('V4', 1), ('V5', 5)],
    'V4': [('V2', 3), ('V3', 1), ('V6', 2)],
    'V5': [('V3', 5), ('V6', 1)],
    'V6': [('V4', 2), ('V5', 1)]
}

heuristic = {
    'V1': 5,
    'V2': 5,
    'V3': 3,
    'V4': 2,
    'V5': 1,
    'V6': 0
}

def a_star(start, goal):
    priority_queue = [
        (heuristic[start], 0, start, [start])
    ]

    visited = set()

    while priority_queue:
        f, g, node, path = heapq.heappop(priority_queue)

        if node in visited:
            continue

        visited.add(node)

        if node == goal:
            return path, g

        for neighbor, cost in graph[node]:
            if neighbor not in visited:
                new_g = g + cost
                new_f = new_g + heuristic[neighbor]

                heapq.heappush(
                    priority_queue,
                    (new_f, new_g, neighbor, path + [neighbor])
                )

    return None, None

start = 'V1'
goal = 'V6'

path, cost = a_star(start, goal)

print("Source:", start)
print("Destination:", goal)
print("Shortest Path:", " -> ".join(path))
print("Total Cost:", cost)