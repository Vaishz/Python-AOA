def minDistance(V, dist, visited):
    min_dist = 9999
    min_index = -1
    for v in range(V):
        if dist[v] < min_dist and not visited[v]:
            min_dist = dist[v]
            min_index = v                       #1
    return min_index

def Dijkstra(graph, V, src):     #V is no of vertices                       
    dist = [9999] * V
    dist[src] = 0
    visited = [False] * V

    for a in range(V): 
        u = minDistance(V, dist, visited)       #index store hoga of min dist
        visited[u] = True
        for v in range(V):
            if graph[u][v] > 0 and not visited[v] and dist[u] + graph[u][v] < dist[v]:
                dist[v] = dist[u] + graph[u][v]

    print("Vertex \t Distance")
    for node in range(V):
        print(node, "\t\t", dist[node])

n = int(input("Enter number of vertices: "))
print("Enter the adjacency Matrix:")
G = []
for _ in range(n):
    data = list(map(int, input().split()))
    G.append(data)

s = int(input("Enter the source vertex: "))
Dijkstra(G, n, s)


#min_index is a variable used to keep track of the index of the vertex with the minimum distance found so far
'''0 5 10 0 20
5 0 4 2 0 
10 4 0 3 0
0 2 3 0 5
20 0 0 5 0''' 
