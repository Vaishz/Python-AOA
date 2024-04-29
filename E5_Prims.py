def Min_Key(V,dist,mst):
    min_val=9999
    min_index=-1
    for v in range(V):
        if (dist[v] < min_val and not mst[v]):
            min_val = dist[v]
            min_index = v
    return min_index

def Prim(graph,V):
    key = [9999] * V
    mst = [False] * V
    parent = [-1] * V
  
    key[0] = 0
    parent[0] = -1
    
    for a in range(V):
        u = Min_Key(V,key,mst)
        mst[u] = True
        for v in range(V):
            if (graph[u][v] and not mst[v] and graph[u][v] < key[v]):
                key[v] = graph[u][v]
                parent[v] = u
    print("Edge \t Weight")
    for i in range(1,V):
        print(parent[i],"-",i,"\t",graph[i][parent[i]])

V = int(input("Enter the no of vertices: "))
G = []
print("Enter the adjacency matrix:")
for i in range(V):
    data = list(map( int , input().split()))
    G.append(data)
Prim(G,V)

'''0 5 10 0 20
5 0 4 2 0 
10 4 0 3 0
0 2 3 0 5
20 0 0 5 0'''