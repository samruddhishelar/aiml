# Q24. Knowledge Graph

entities = ["Rudra", "Raha", "Python", "AI", "Machine Learning"]

types = {
    "Rudra": "Student",
    "Raha": "Teacher",
    "Python": "Programming Language",
    "AI": "Subject",
    "Machine Learning": "AI Topic"
}

properties = {
    "Rudra": ["name", "age"],
    "Raha": ["name", "subject"],
    "Python": ["name", "type"],
    "AI": ["name", "field"],
    "Machine Learning": ["name", "field"]
}

relationships = [
    ("Rudra", "studies", "AI"),
    ("Raha", "teaches", "AI"),
    ("Rudra", "hasTeacher", "Raha"),
    ("AI", "includes", "Machine Learning"),
    ("Machine Learning", "uses", "Python")
]

print("Entities:")
for e in entities:
    print(e)

print("\nTypes:")
for entity, entity_type in types.items():
    print(entity, "is a", entity_type)

print("\nProperties:")
for entity, props in properties.items():
    print(entity, "has properties:", props)

print("\nRelationships:")
for subject, relation, obj in relationships:
    print((subject, relation, obj))