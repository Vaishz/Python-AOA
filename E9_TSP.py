INF = 10**9

def travel_salesman(path, visited, current, current_cost):
    global cost, bestPath

    if len(path) == n:
        if tsp_g[current][0] != 0:
            current_cost += tsp_g[current][0]  # Complete the cycle
            if current_cost < cost:
                cost = current_cost
                bestPath = path[:]   #creates a copy of the path list and assigns it to bestPath. This ensures that bestPath holds a separate copy of the sequence of cities visited in the best path found so far, independent of any changes made to the path list in subsequent iterations of the algorithm
        return

    for i in range(n):
        if not visited[i] and tsp_g[current][i] != 0:
            visited[i] = 1
            path.append(i)
            travel_salesman(path, visited, i, current_cost + tsp_g[current][i])
            path.pop()
            visited[i] = 0

if __name__ == "__main__":
    n = int(input("Enter the number of cities: "))

    tsp_g = []
    cost = INF
    bestPath = []

    print("Enter the distance matrix:")
    for _ in range(n):
        tsp_g.append(list(map(int, input().split())))

    path = [0]  # Start from city 0
    visited = [0] * n  # Initially all cities are unvisited
    visited[0] = 1  # Mark city 0 as visited
    travel_salesman(path, visited, 0, 0)

    print("Shortest Path:", *bestPath, "0")
    print("Minimum Cost:", cost)