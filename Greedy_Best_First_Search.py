def greedy_best_first_search(graph, h, start, goal):
    frontier = [(h[start], [start])]    # each item is (heuristic value, path)
    visited = [start]

    while frontier:
        best = min(frontier)            # pick the path whose last node has the smallest h
        frontier.remove(best)
        path = best[1]
        node = path[-1]                 # last node of that path

        if node == goal:                # goal found, return the path
            return path

        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.append(neighbor)
                frontier.append((h[neighbor], path + [neighbor]))

    return None                         # no path exists


# ---- Take the graph and heuristic values as input ----
graph = {}
h = {}
n = int(input("Enter number of nodes: "))

for i in range(1, n + 1):               # loops from 1 to n
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
    path = greedy_best_first_search(graph, h, start, goal)

    if path:
        print("Start node:", start)
        print("Goal node:", goal)
        print("Path:", " -> ".join(path))
        print("Steps:", len(path) - 1)
    else:
        print("No path found from", start, "to", goal)
