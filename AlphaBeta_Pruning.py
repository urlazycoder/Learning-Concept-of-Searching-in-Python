def alpha_beta(depth, index, is_max, values, max_depth, alpha, beta):
    # leaf node: return its value
    if depth == max_depth:
        return values[index]

    if is_max:
        best = float('-inf')
        for child in [index * 2, index * 2 + 1]:
            value = alpha_beta(depth + 1, child, False, values, max_depth, alpha, beta)
            best = max(best, value)         # MAX keeps the bigger value
            alpha = max(alpha, best)        # update alpha (best MAX can guarantee)

            if beta <= alpha:               # MIN above will never allow this, so stop
                print("Pruned: skipped remaining branch at depth", depth, ", node", index)
                break
        return best
    else:
        best = float('inf')
        for child in [index * 2, index * 2 + 1]:
            value = alpha_beta(depth + 1, child, True, values, max_depth, alpha, beta)
            best = min(best, value)         # MIN keeps the smaller value
            beta = min(beta, best)          # update beta (best MIN can guarantee)

            if beta <= alpha:               # MAX above will never allow this, so stop
                print("Pruned: skipped remaining branch at depth", depth, ", node", index)
                break
        return best


# ---- Take the game tree as input ----
max_depth = int(input("Enter depth of the tree: "))
total_leaves = 2 ** max_depth       # a binary tree has 2^depth leaf nodes

print("Enter", total_leaves, "leaf values (separated by spaces):")
values = list(map(int, input().split()))

# ---- Check the number of values ----
if len(values) != total_leaves:
    print("You must enter exactly", total_leaves, "values")
else:
    # MAX plays first at the root, alpha starts at -infinity, beta at +infinity
    result = alpha_beta(0, 0, True, values, max_depth, float('-inf'), float('inf'))
    print("Value of the root (MAX):", result)
