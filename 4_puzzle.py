# Q8. 4-Puzzle using A* Search

import heapq

goal = (1, 2, 3, 0)

def h(state):
    count = 0

    for i in range(4):
        if state[i] != 0 and state[i] != goal[i]:
            count += 1

    return count

def astar(start):
    queue = [(h(start), 0, start, [])]
    visited = set()

    while queue:
        f, cost, state, path = heapq.heappop(queue)

        if state in visited:
            continue

        visited.add(state)

        if state == goal:
            return path + [state]

        zero = state.index(0)

        moves = {
            0: [1, 2],
            1: [0, 3],
            2: [0, 3],
            3: [1, 2]
        }

        for pos in moves[zero]:
            new_state = list(state)

            new_state[zero], new_state[pos] = \
                new_state[pos], new_state[zero]

            new_state = tuple(new_state)

            if new_state not in visited:
                new_cost = cost + 1
                f = new_cost + h(new_state)

                heapq.heappush(
                    queue,
                    (f, new_cost, new_state, path + [state])
                )

    return None

start = (1, 0, 3, 2)

solution = astar(start)

print("Solution:")

for state in solution:
    print(state[0], state[1])
    print(state[2], state[3])
    print()