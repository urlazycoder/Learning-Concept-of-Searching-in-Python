def minimax(depth, index, is_max, values, max_depth):
    # leaf node: return its value
    if depth == max_depth:
        return values[index]

    # children of a node at position 'index' are at 2*index and 2*index + 1
    left = minimax(depth + 1, index * 2, not is_max, values, max_depth)
    right = minimax(depth + 1, index * 2 + 1, not is_max, values, max_depth)

    if is_max:
        return max(left, right)     # MAX player picks the bigger value
    else:
        return min(left, right)     # MIN player picks the smaller value


# ---- Take the game tree as input ----
max_depth = int(input("Enter depth of the tree: "))
total_leaves = 2 ** max_depth       # a binary tree has 2^depth leaf nodes

print("Enter", total_leaves, "leaf values (separated by spaces):")
values = list(map(int, input().split()))

# ---- Check the number of values ----
if len(values) != total_leaves:
    print("You must enter exactly", total_leaves, "values")
else:
    # MAX plays first at the root
    left_value = minimax(1, 0, False, values, max_depth)
    right_value = minimax(1, 1, False, values, max_depth)
    best_value = max(left_value, right_value)

    print("Value of left branch:", left_value)
    print("Value of right branch:", right_value)

    if left_value >= right_value:
        print("MAX should choose: left branch")
    else:
        print("MAX should choose: right branch")

    print("Minimax value of the root:", best_value)
