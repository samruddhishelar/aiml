# Q10. Means-End Analysis

current = 2
goal = 10

while current != goal:
    print("Current:", current)

    if current < goal:
        print("Action: Add 2")
        current = current + 2
    else:
        print("Action: Subtract 2")
        current = current - 2

print("Goal reached:", current)