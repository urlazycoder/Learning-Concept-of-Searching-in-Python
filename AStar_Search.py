def a_star_search(graph, h, start, goal):
    frontier = [(h[start], 0, [start])]   # each item is (f, g, path)
    best_g = {start: 0}                   # cheapest cost found so far to each node

    while frontier:
        best = min(frontier)              # pick the path with the smallest f = g + h
        frontier.remove(best)
        f, g, path = best
        node = path[-1]                   # last node of that path

        if node == goal:                  # goal found, return the path and its cost
            return path, g

        for neighbor in graph[node]:
            new_g = g + graph[node][neighbor]        # cost so far + cost of this step

            # only add the neighbor if this is the cheapest way found so far
            if neighbor not in best_g or new_g < best_g[neighbor]:
                best_g[neighbor] = new_g
                new_f = new_g + h[neighbor]
                frontier.append((new_f, new_g, path + [neighbor]))

    return None, None                     # no path exists


# ---- Take the graph, costs and heuristic values as input ----
graph = {}
h = {}
n = int(input("Enter number of nodes: "))

for i in range(1, n + 1):                 # loops from 1 to n
    node = input("Enter node " + str(i) + ": ")
    h[node] = int(input("Enter heuristic value of " + node + ": "))
    neighbors = input("Enter neighbors of " + node + " (separated by spaces): ").split()

    graph[node] = {}
    for neighbor in neighbors:
        cost = int(input("Enter cost from " + node + " to " + neighbor + ": "))
        graph[node][neighbor] = cost

# ---- Take start and goal as input ----
start = input("Enter start node: ")
goal = input("Enter goal node: ")

# ---- Check that the nodes exist ----
if start not in graph or goal not in graph:
    print("Start or goal node is not in the graph")
else:
    path, total_cost = a_star_search(graph, h, start, goal)

    if path:
        print("Start node:", start)
        print("Goal node:", goal)
        print("Path:", " -> ".join(path))
        print("Total cost:", total_cost)
    else:
        print("No path found from", start, "to", goal)
