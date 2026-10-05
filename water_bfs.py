# Q12. Water Jug Problem using BFS

from collections import deque

def water_jug():
    queue = deque([((0, 0), [])])
    visited = set()

    while queue:
        (x, y), path = queue.popleft()

        if (x, y) in visited:
            continue

        visited.add((x, y))
        new_path = path + [(x, y)]

        if x == 2 or y == 2:
            print("Solution Path:")
            for state in new_path:
                print(state)
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
                queue.append((state, new_path))

water_jug()