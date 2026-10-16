def f(x):
    return -x**2 + 4*x

x = 0

step = 1

print("Hill Climbing Process")
print("---------------------")

while True:
    current_value = f(x)

    left_x = x - step
    right_x = x + step

    left_value = f(left_x)
    right_value = f(right_x)

    print("x =", x, "F(x) =", current_value)

    if left_value > current_value:
        x = left_x
    elif right_value > current_value:
        x = right_x
    else:
        break

print("---------------------")
print("Maximum found at x =", x)
print("Maximum value F(x) =", f(x))