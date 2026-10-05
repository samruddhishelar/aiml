# Q18. Tower of Hanoi

def tower_of_hanoi(n, source, target, auxiliary):

    if n == 1:
        print("Move disk 1 from", source, "to", target)
        return

    tower_of_hanoi(n - 1, source, auxiliary, target)

    print("Move disk", n, "from", source, "to", target)

    tower_of_hanoi(n - 1, auxiliary, target, source)


n = 3

print("Steps to solve Tower of Hanoi:")

tower_of_hanoi(n, 'A', 'C', 'B')