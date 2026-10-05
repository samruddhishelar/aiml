
facts = {
    "rain",
    "wet_ground"
}


rules = [
    ("rain", "wet_ground"),
    ("wet_ground", "slippery"),
    ("slippery", "drive_slowly")
]


changed = True

while changed:
    changed = False

    for condition, conclusion in rules:
        if condition in facts and conclusion not in facts:
            facts.add(conclusion)
            changed = True


print("Knowledge Base:")

for fact in facts:
    print("-", fact)


query = input("\nEnter a fact to check: ")

if query in facts:
    print("True:", query, "is known.")
else:
    print("False:", query, "is not known.")