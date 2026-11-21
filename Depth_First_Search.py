def dfs(graph, start, goal):
    stack = [[start]]          # each item is a path, e.g. ['A', 'C']
    visited = []

    while stack:
        path = stack.pop()          # take the LAST path added (this makes it DFS)
        node = path[-1]             # last node of that path

        if node == goal:            # goal found, return the path
            return path

        if node not in visited:
            visited.append(node)

            # reversed() so neighbors are explored in the order they were entered
            for neighbor in reversed(graph[node]):
                if neighbor not in visited:
                    stack.append(path + [neighbor])

    return None                     # no path exists


# ---- Take the graph as input ----
graph = {}
n = int(input("Enter number of nodes: "))

for i in range(1, n + 1):           # loops from 1 to n
    node = input("Enter node " + str(i) + ": ")
    neighbors = input("Enter neighbors of " + node + " (separated by spaces): ").split()
    graph[node] = neighbors

# ---- Take start and goal as input ----
start = input("Enter start node: ")
goal = input("Enter goal node: ")

# ---- Check that the nodes exist ----
if start not in graph or goal not in graph:
    print("Start or goal node is not in the graph")
else:
    path = dfs(graph, start, goal)

    if path:
        print("Start node:", start)
        print("Goal node:", goal)
        print("Path:", " -> ".join(path))
        print("Steps:", len(path) - 1)
    else:
        print("No path found from", start, "to", goal)
