import heapq

def dijkstra(graph, start, end):
    n = len(graph)
    distances = [float('inf')] * n
    distances[start] = 0
    priority_queue = [(0, start)]
    predecessors = [-1] * n  # To store the shortest path tree
    
    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)
        
        if current_node == end:
            break
        
        if current_distance > distances[current_node]:
            continue
        
        for neighbor in range(n):
            if graph[current_node][neighbor] != 0:  # There is an edge
                distance = current_distance + graph[current_node][neighbor]
                
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    predecessors[neighbor] = current_node
                    heapq.heappush(priority_queue, (distance, neighbor))
    
    # Reconstruct the shortest path
    path = []
    node = end
    while node != -1:
        path.insert(0, node)
        node = predecessors[node]
    
    return distances[end], path

# Adjacency matrix representation of the graph
G = [
    [0, 4, 0, 0, 0, 0, 0, 8, 0],  # Node 0
    [4, 0, 8, 0, 0, 0, 0, 11, 0], # Node 1
    [0, 8, 0, 7, 0, 4, 0, 2, 2],  # Node 2
    [0, 0, 7, 0, 9, 14, 0, 0, 0], # Node 3
    [0, 0, 0, 9, 0, 10, 0, 0, 0], # Node 4
    [0, 0, 4, 14, 10, 0, 2, 0, 0],# Node 5
    [0, 0, 0, 0, 0, 2, 0, 1, 6],  # Node 6
    [8, 11, 2, 0, 0, 0, 1, 0, 7], # Node 7
    [0, 0, 2, 0, 0, 0, 6, 7, 0]   # Node 8
]

start_node = 0
end_node = 4
distance, path = dijkstra(G, start_node, end_node)
print("Shortest distance:", distance)
print("Path:", path)

# ==========================================================

