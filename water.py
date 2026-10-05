# Q2. Water Jug Problem using BFS

from collections import deque

def water_jug():
    visited = set()
    queue = deque([(0, 0)])

    while queue:
        x, y = queue.popleft()

        if (x, y) in visited:
            continue

        visited.add((x, y))

        if x == 2 or y == 2:
            print("Solution:", (x, y))
            return

        states = [
            (4, y),
            (x, 3),
            (0, y),
            (x, 0),
            (max(0, x - (3 - y)), min(3, x + y)),
            (min(4, x + y), max(0, y - (4 - x)))
        ]

        for state in states:
            if state not in visited:
                queue.append(state)

water_jug()