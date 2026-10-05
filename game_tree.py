# Q4. Game Tree Representation

game_tree = {
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": ["F", "G"],
    "D": [],
    "E": [],
    "F": [],
    "G": []
}


def display_tree(node, level=0):
    print(" " * level + node)

    for child in game_tree[node]:
        display_tree(child, level + 1)


print("Game Tree:")
display_tree("A")