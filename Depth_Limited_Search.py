def depth_limited_search(graph, start, goal, limit):
    stack = [[start]]          # each item is a path, e.g. ['A', 'C']

    while stack:
        path = stack.pop()          # take the LAST path added (DFS style)
        node = path[-1]             # last node of that path
        depth = len(path) - 1       # depth of this node (start is depth 0)

        if node == goal:            # goal found, return the path
            return path

        if depth < limit:           # only go deeper if the limit is not reached
            for neighbor in reversed(graph[node]):
                if neighbor not in path:      # avoid going in circles
                    stack.append(path + [neighbor])

    return None                     # goal not found within the depth limit


# ---- Take the graph as input ----
graph = {}
n = int(input("Enter number of nodes: "))

for i in range(1, n + 1):           # loops from 1 to n
    node = input("Enter node " + str(i) + ": ")
    neighbors = input("Enter neighbors of " + node + " (separated by spaces): ").split()
    graph[node] = neighbors

# ---- Take start, goal and depth limit as input ----
start = input("Enter start node: ")
goal = input("Enter goal node: ")
limit = int(input("Enter depth limit: "))

# ---- Check that the nodes exist ----
if start not in graph or goal not in graph:
    print("Start or goal node is not in the graph")
else:
    path = depth_limited_search(graph, start, goal, limit)

    if path:
        print("Start node:", start)
        print("Goal node:", goal)
        print("Depth limit:", limit)
        print("Path:", " -> ".join(path))
        print("Steps:", len(path) - 1)
    else:
        print("Goal not found within depth limit", limit)
