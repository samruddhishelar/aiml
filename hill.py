# Q9. Hill Climbing Algorithm

def f(x):
    return -(x - 3) ** 2 + 10

x = 0

while True:
    current = f(x)

    if f(x + 1) > current:
        x = x + 1
    else:
        break

print("Maximum x:", x)
print("Maximum value:", f(x))