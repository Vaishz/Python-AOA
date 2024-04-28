def Prim(graph):
    parent = [-1] * len(graph)  # Stores parent of each vertex in MST
    key = [float('inf')] * len(graph)  # Stores minimum key value for each vertex
    mstSet = [False] * len(graph)   # Keeps track of vertices included in MST

    key[0] = 0  # Starting from the first vertex

    for _ in range(len(graph)):
        min_index = -1  # Initialize min_index outside the loop

        # Find the vertex with the minimum key value from the set of vertices
        # not yet included in MST
        for v in range(len(graph)):
            if not mstSet[v] and key[v] < key[min_index]:
                min_index = v

        # Add the found vertex to MST
        mstSet[min_index] = True

        # Update key and parent for adjacent vertices of the picked vertex.
        # Consider only those vertices which are not yet included in MST
        for v in range(len(graph)):
            if graph[min_index][v] > 0 and not mstSet[v] and graph[min_index][v] < key[v]:
                parent[v] = min_index
                key[v] = graph[min_index][v]

    return parent  # Return the parent list representing the MST

# Example usage:
graph = [
  [0, 2, 0, 6, 0],
  [2, 0, 3, 8, 5],
  [0, 3, 0, 0, 7],
  [6, 8, 0, 0, 9],
  [0, 5, 7, 9, 0]
]

mst_parent = Prim(graph)

# Print the constructed MST (you can modify this part for different output formats)
for i in range(1, len(graph)):
    print(mst_parent[i], "-", i, "\t", graph[i][mst_parent[i]])
