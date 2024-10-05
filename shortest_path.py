from collections import deque

def shortest_path(graph, start, end):
    visited = set()
    queue = deque([(start, [start])])
    
    while queue:
        current_node, path = queue.popleft()
        
        if current_node == end:
            return path
        
        for neighbor in graph[current_node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, path + [neighbor]))
                
    return None  

graph = {
    0: [1, 2],
    1: [0, 3, 4],
    2: [0, 5],
    3: [1],
    4: [1, 5],
    5: [2, 4]
}

print(shortest_path(graph, 0, 4))
