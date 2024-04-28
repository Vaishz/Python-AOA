# Kruskal's Algorithm
def kruskal_mst(graph):
    V = len(graph)
    result = []         #edges of mst found
    
    # Sort edges by weight
    edges = []          #all edges
    for i in range(V):
        for j in range(i+1, V):
            if graph[i][j] != 0:
                edges.append((i, j, graph[i][j]))       #(src,dest,wt)
    edges.sort(key=lambda x: x[2])      #x[2] means 3rd element, sort by 3rd elmt, ie wt
    
    parent = [i for i in range(V)]
    rank = [0] * V
    
    def find(u):
        if parent[u] != u:
            parent[u] = find(parent[u])
        return parent[u]
    
    def union(u, v):
        u_root = find(u)
        v_root = find(v)
        
        if rank[u_root] < rank[v_root]:
            parent[u_root] = v_root
        elif rank[u_root] > rank[v_root]:
            parent[v_root] = u_root
        else:
            parent[v_root] = u_root
            rank[u_root] += 1
            
    
    for edge in edges:
        u, v, weight = edge
        u_root = find(u)
        v_root = find(v)
        
        if u_root != v_root:
            result.append((u, v, weight))
            union(u_root, v_root)
    
    return result

# Prim's Algorithm
def prim_mst(graph):
    V = len(graph)
    parent = [-1] * V
    key = [float('inf')] * V
    mst_set = [False] * V
    
    key[0] = 0
    parent[0] = -1
    
    for _ in range(V):
        u = min_key(key, mst_set)
        mst_set[u] = True
        
        for v in range(V):
            if graph[u][v] != 0 and not mst_set[v] and graph[u][v] < key[v]:
                parent[v] = u
                key[v] = graph[u][v]
    
    result = [(parent[i], i, graph[i][parent[i]]) for i in range(1, V)]
    return result

def min_key(key, mst_set):
    min_val = float('inf')
    min_index = -1
    for v in range(len(key)):
        if key[v] < min_val and not mst_set[v]:
            min_val = key[v]
            min_index = v
    return min_index

# Example Usage
graph = [
    [0, 10, 6, 5],
    [10, 0, 0, 15],
    [6, 0, 0, 4],
    [5, 15, 4, 0]
]

print("Kruskal's MST:")
print(kruskal_mst(graph))

print("\nPrim's MST:")
print(prim_mst(graph))

#The parent list initially assigns each vertex to itself, indicating that each vertex is its own parent. This will be used in the union-find algorithm for detecting cycles.
#The rank list is used to keep track of the depth of the tree for each vertex in the union-find algorithm. Initially, all ranks are set to 0.