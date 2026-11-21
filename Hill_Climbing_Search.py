def hill_climbing(graph, h, start, goal):
    current = start
    path = [start]

    while current != goal:
        # find the neighbor with the smallest heuristic value
        best = None
        for neighbor in graph[current]:
            if best is None or h[neighbor] < h[best]:
                best = neighbor

        # stop if there is no neighbor, or no neighbor is better than the current node
        if best is None or h[best] >= h[current]:
            break

        current = best              # move to the best neighbor
        path.append(current)

    return path


# ---- Take the graph and heuristic values as input ----
graph = {}
h = {}
n = int(input("Enter number of nodes: "))

for i in range(1, n + 1):           # loops from 1 to n
    node = input("Enter node " + str(i) + ": ")
    h[node] = int(input("Enter heuristic value of " + node + ": "))
    neighbors = input("Enter neighbors of " + node + " (separated by spaces): ").split()
    graph[node] = neighbors

# ---- Take start and goal as input ----
start = input("Enter start node: ")
goal = input("Enter goal node: ")

# ---- Check that the nodes exist ----
if start not in graph or goal not in graph:
    print("Start or goal node is not in the graph")
else:
    path = hill_climbing(graph, h, start, goal)

    print("Start node:", start)
    print("Path:", " -> ".join(path))

    if path[-1] == goal:
        print("Goal reached:", goal)
    else:
        print("Stuck at node", path[-1], "(local optimum), goal", goal, "not reached")
