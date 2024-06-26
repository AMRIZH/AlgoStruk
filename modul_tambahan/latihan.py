import heapq

def dijkstra(graph, start):
    n = len(graph)
    distances = [float('inf')] * n
    distances[start] = 0
    priority_queue = [(0, start)]
    
    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)
        
        if current_distance > distances[current_node]:
            continue
        
        for neighbor in range(n):
            if graph[current_node][neighbor] != 0:  # There is an edge
                distance = current_distance + graph[current_node][neighbor]
                
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(priority_queue, (distance, neighbor))
    
    return distances

# Example graph represented as an adjacency matrix
graph = [
    [0, 1, 4, 0],
    [1, 0, 2, 5],
    [4, 2, 0, 1],
    [0, 5, 1, 0]
]

start_node = 0
print(dijkstra(graph, start_node))

# =========================================================
def greedy_tsp(graph, start):
    n = len(graph)
    visited = [False] * n
    path = [start]
    total_cost = 0
    current_node = start
    visited[start] = True
    
    for _ in range(n - 1):
        nearest_neighbor = None
        shortest_distance = float('inf')
        
        for neighbor in range(n):
            if not visited[neighbor] and graph[current_node][neighbor] < shortest_distance:
                nearest_neighbor = neighbor
                shortest_distance = graph[current_node][neighbor]
                
        path.append(nearest_neighbor)
        visited[nearest_neighbor] = True
        total_cost += shortest_distance
        current_node = nearest_neighbor
        
    total_cost += graph[current_node][start]
    path.append(start)
    
    return path, total_cost

# Example graph represented as an adjacency matrix
graph = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

start_node = 0
path, cost = greedy_tsp(graph, start_node)
print("Path:", path)
print("Total cost:", cost)
