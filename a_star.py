# Q1. A* Search Algorithm

graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'D': 2, 'E': 5},
    'C': {'F': 3},
    'D': {'G': 3},
    'E': {'G': 1},
    'F': {'G': 2},
    'G': {}
}

h = {
    'A': 6,
    'B': 5,
    'C': 4,
    'D': 3,
    'E': 2,
    'F': 2,
    'G': 0
}


def a_star(start, goal):
    open_list = [start]
    g_cost = {start: 0}
    parent = {start: None}

    while open_list:
        current = min(
            open_list,
            key=lambda node: g_cost[node] + h[node]
        )

        if current == goal:
            break

        open_list.remove(current)

        for neighbor, cost in graph[current].items():
            new_cost = g_cost[current] + cost

            if neighbor not in g_cost or new_cost < g_cost[neighbor]:
                g_cost[neighbor] = new_cost
                parent[neighbor] = current

                if neighbor not in open_list:
                    open_list.append(neighbor)

    path = []
    current = goal

    while current is not None:
        path.append(current)
        current = parent[current]

    path.reverse()

    return path, g_cost[goal]


source = 'A'
destination = 'G'

path, cost = a_star(source, destination)

print("Shortest Path:", " -> ".join(path))
print("Shortest Path Cost:", cost)