from collections import deque

# Classic water jug problem: 4-litre jug, 3-litre jug, measure exactly 2 litres
cap1 = 4
cap2 = 3
target = 2

start = (0, 0)                              # state = (water in jug 1, water in jug 2)
queue = deque([[(start, "Start")]])         # each item is a path of (state, action)
visited = [start]
solution = None

while queue:
    path = queue.popleft()
    x, y = path[-1][0]                      # current state

    if x == target or y == target:          # goal: either jug has 2 litres
        solution = path
        break

    # all possible moves from the current state
    moves = [
        ((cap1, y), "Fill the 4L jug"),
        ((x, cap2), "Fill the 3L jug"),
        ((0, y), "Empty the 4L jug"),
        ((x, 0), "Empty the 3L jug"),
    ]

    pour = min(x, cap2 - y)                 # pour 4L jug into 3L jug
    moves.append(((x - pour, y + pour), "Pour 4L jug into 3L jug"))

    pour = min(y, cap1 - x)                 # pour 3L jug into 4L jug
    moves.append(((x + pour, y - pour), "Pour 3L jug into 4L jug"))

    for state, action in moves:
        if state not in visited:
            visited.append(state)
            queue.append(path + [(state, action)])

# ---- Show only the steps ----
print("Start:", solution[0][0])

for i in range(1, len(solution)):
    state, action = solution[i]
    print("Step " + str(i) + ":", action, "->", state)
