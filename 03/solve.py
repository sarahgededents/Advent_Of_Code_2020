def tree_count(trees, down, right):
    count = 0
    row, col = 0, 0
    while row < len(trees):
        if trees[row][col % len(trees[row])] == '#':
            count += 1
        row += down
        col += right
    return count

def count_iter(trees):
    return tree_count(trees, 1, 1) * tree_count(trees, 1, 3) * tree_count(trees, 1, 5) * tree_count(trees, 1, 7) * tree_count(trees, 2, 1)

trees = []
with open("input", "r") as f:
    for line in f:
        trees.append(line.strip())
print(count_iter(trees))