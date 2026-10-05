# Q20. AO* Algorithm

graph = {
    'A': [['B', 'C'], ['D']],
    'B': [['E']],
    'C': [['F']],
    'D': [['G']],
    'E': [],
    'F': [],
    'G': []
}

cost = {
    'A': 0,
    'B': 1,
    'C': 1,
    'D': 3,
    'E': 2,
    'F': 2,
    'G': 1
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