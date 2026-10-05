# Q27. Euclidean Distance

import math

point1 = list(map(int, input("Data Point 1: ").split()))
point2 = list(map(int, input("Data Point 2: ").split()))

distance = math.sqrt(
    sum((a - b) ** 2 for a, b in zip(point1, point2))
)

print("Data Point 1:", point1)
print("Data Point 2:", point2)
print("Euclidean Distance =", round(distance, 3))