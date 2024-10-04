def isCyclicUtil(v, visited, parent, adj):
    visited[v] = True
    for i in adj[v]:
        if not visited[i]:
            if isCyclicUtil(i, visited, v, adj):
                return True
        elif i != parent:
            return True
    return False

def isCyclic(V, adj):
    visited = [False] * V
    for i in range(V):
        if not visited[i]:
            if isCyclicUtil(i, visited, -1, adj):
                return True
    return False

V = 5
adj = [[1], [0, 2, 4], [1, 3], [2, 4], [1, 3]]
print(isCyclic(V, adj))  
