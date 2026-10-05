# Q2. Map Coloring using CSP

def is_safe(v, graph, color, c):
    for i in range(len(graph)):
        if graph[v][i] == 1 and color[i] == c:
            return False
    return True


def graph_coloring(graph, m, color, v):
    if v == len(graph):
        return True

    for c in range(1, m + 1):
        if is_safe(v, graph, color, c):
            color[v] = c

            if graph_coloring(graph, m, color, v + 1):
                return True

            color[v] = 0

    return False


graph = [
    [0, 1, 1, 0],
    [1, 0, 1, 0],
    [0, 1, 0, 1],
    [1, 0, 1, 0]
]

m = 3
color = [0] * len(graph)

if graph_coloring(graph, m, color, 0):
    color_names = ["", "Red", "Green", "Blue"]
    vertices = ["A", "B", "C", "D"]

    print("Graph Coloring Solution:")

    for i in range(len(vertices)):
        print(vertices[i], "->", color_names[color[i]])
else:
    print("No solution exists with", m, "colors.")