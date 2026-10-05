# Q15. Forward Chaining

facts = ["rain", "cloudy"]

rules = {
    "rain": "wet_ground",
    "wet_ground": "slippery",
    "cloudy": "umbrella"
}

for condition, result in rules.items():
    if condition in facts:
        facts.append(result)
        print("New fact:", result)

print("\nFinal Facts:")
print(facts)