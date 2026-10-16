

graph = {
    'A': [['B'], ['C']],
    'B': [['D','E']],
    'C': [['F'],['G']],
    'D': [['H'],['I']],
    'E': [['J']],
    'F': [],
    'G': [],
    'H': [],
    'I': [],
    'J': [],
}

cost = {
    'A': 0,
    'B': 1,
    'C': 1,
    'D': 2,
    'E': 2,
    'F': 2,
    'G': 1,
    'H': 2,
    'I': 3,
    'J': 1,

}

def ao_star(node):

    if not graph[node]:
        return cost[node]

    values = []

    for group in graph[node]:

        total = 0

        for child in group:
            total += ao_star(child)

        values.append(total)

    return cost[node] + min(values)


result = ao_star('A')

print("Minimum cost:", result)