# Q25. Ontological Engineering

classes = ["Person", "Student", "Teacher"]

subclasses = {
    "Student": "Person",
    "Teacher": "Person"
}

properties = {
    "Student": ["name", "age"],
    "Teacher": ["name", "subject"]
}

relationships = [
    ("Rudra", "isA", "Student"),
    ("Raha", "isA", "Teacher"),
    ("Rudra", "hasTeacher", "Raha")
]

print("Classes:")
for c in classes:
    print(c)

print("\nSubclasses:")
for child, parent in subclasses.items():
    print(child, "is a subclass of", parent)

print("\nRelationships:")
for subject, relation, obj in relationships:
    print((subject, relation, obj))