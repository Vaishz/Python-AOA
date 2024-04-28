def Prims(graph):
    parent = [-1] * len(graph)
    key = [9999] * len(graph)   # stores minimum key value for each vertex
    mst = [False] * len(graph) # keeps track whether vertex is added or not

    key[0] = 0  # Starting from the first vertex

    for _ in range(len(graph)):
        # Find the vertex with the minimum key value
        key[0] = 0
        parent[0]=-1
        for v in range(len(graph)):
            if key[v] < min_key and not mst[v]:
                min_key = key[v]
                min_index = v

        mst[min_index] = True

        # Update key and parent for adjacent vertices
        for v in range(len(graph)):
            if graph[min_index][v] and not mst[v] and graph[min_index][v] < key[v]:
                key[v] = graph[min_index][v]
                parent[v] = min_index

    # Print the constructed MST
    print("Edge \tWeight")
    for i in range(1, len(graph)):
        print(parent[i], "-", i, "\t", graph[i][parent[i]])

# Example usage:
graph = [
    [0, 2, 0, 6, 0],
    [2, 0, 3, 8, 5],
    [0, 3, 0, 0, 7],
    [6, 8, 0, 0, 9],
    [0, 5, 7, 9, 0]
]

Prims(graph)
