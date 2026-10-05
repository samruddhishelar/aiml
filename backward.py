# Q19. Backward Chaining

facts = ["rain", "cloudy"]

rules = {
    "wet_ground": "rain",
    "slippery": "wet_ground",
    "umbrella": "rain"
}


def backward(goal):
    if goal in facts:
        return True

    if goal in rules:
        return backward(rules[goal])

    return False


goal = "slippery"

if backward(goal):
    print(goal, "can be proved.")
else:
    print(goal, "cannot be proved.")