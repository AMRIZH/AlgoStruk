import heapq

def dijkstra(graph, start, end):
    n = len(graph)
    distances = [float('inf')] * n  # Initialize distances to infinity
    distances[start] = 0  # Set the distance of the start node to 0
    priority_queue = [(0, start)]  # Create a priority queue with the start node
    predecessors = [-1] * n  # To store the shortest path tree
    
    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)  # Get the node with the smallest distance
        
        if current_node == end:  # If we have reached the end node, stop the algorithm
            break
        
        if current_distance > distances[current_node]:  # If the current distance is greater than the stored distance, skip to the next iteration
            continue
        
        for neighbor in range(n):  # Iterate through the neighbors of the current node
            if graph[current_node][neighbor] != 0:  # If there is an edge between the current node and the neighbor
                distance = current_distance + graph[current_node][neighbor]  # Calculate the distance to the neighbor
                
                if distance < distances[neighbor]:  # If the calculated distance is smaller than the stored distance, update the distance and predecessor
                    distances[neighbor] = distance
                    predecessors[neighbor] = current_node
                    heapq.heappush(priority_queue, (distance, neighbor))  # Add the neighbor to the priority queue
    
    # Reconstruct the shortest path
    path = []
    node = end
    while node != -1:  # Traverse the predecessors to construct the path
        path.insert(0, node)
        node = predecessors[node]
    
    return distances[end], path  # Return the shortest distance and the path

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
print("=========================================================")
# ==========================================================
# Function to find the approximate solution to the Traveling Salesman Problem (TSP) using the greedy algorith

def greedy_tsp(graph, start):
    n = len(graph)  # Number of nodes in the graph
    visited = [False] * n  # List to keep track of visited nodes
    path = [start]  # List to store the path
    total_cost = 0  # Variable to store the total cost of the path
    current_node = start  # Variable to keep track of the current node
    visited[start] = True  # Mark the starting node as visited
    
    for _ in range(n - 1):  # Iterate n-1 times to visit all nodes except the starting node
        nearest_neighbor = None  # Variable to store the nearest unvisited neighbor
        shortest_distance = float('inf')  # Variable to store the shortest distance to the nearest neighbor
        
        for neighbor in range(n):  # Iterate through all nodes to find the nearest unvisited neighbor
            if not visited[neighbor] and graph[current_node][neighbor] < shortest_distance and graph[current_node][neighbor] != 0:
                # If the neighbor is unvisited, the distance to the neighbor is shorter than the current shortest distance,
                # and there is an edge between the current node and the neighbor
                nearest_neighbor = neighbor  # Update the nearest neighbor
                shortest_distance = graph[current_node][neighbor]  # Update the shortest distance
                
        path.append(nearest_neighbor)  # Add the nearest neighbor to the path
        visited[nearest_neighbor] = True  # Mark the nearest neighbor as visited
        total_cost += shortest_distance  # Update the total cost
        current_node = nearest_neighbor  # Update the current node
        
    total_cost += graph[current_node][start]  # Add the cost of returning to the starting node
    path.append(start)  # Add the starting node to the path
    
    return path, total_cost  # Return the path and the total cost of the path


# Function to find the best path and the best total cost by running the greedy TSP algorithm from all starting points
# The function iterates through all nodes as starting points and finds the path and total cost using the greedy TSP algorithm
# It returns the best path and the best total cost among all starting points

def greedy_tsp_all_starts(graph):
    n = len(graph)  # Number of nodes in the graph
    best_path = None  # Variable to store the best path
    best_cost = float('inf')  # Variable to store the best total cost
    
    for start in range(n):  # Iterate through all nodes as starting points
        path, cost = greedy_tsp(graph, start)  # Find the path and total cost using the greedy TSP algorithm
        if cost < best_cost:  # If the total cost is smaller than the current best cost
            best_cost = cost  # Update the best cost
            best_path = path  # Update the best path
            
    return best_path, best_cost  # Return the best path and the best total cost


# Adjacency matrix representation of the graph
G = [
    [0, 5, 0, 4, 0, 6, 7, 0],  # Node H1
    [5, 0, 2, 4, 3, 0, 0, 0],  # Node H2
    [0, 2, 0, 1, 0, 0, 0, 0],  # Node H3
    [4, 4, 1, 0, 7, 0, 0, 0],  # Node H4
    [0, 3, 0, 7, 0, 8, 6, 4],  # Node H5
    [6, 0, 0, 0, 8, 0, 3, 0],  # Node H6
    [7, 0, 0, 0, 6, 3, 0, 2],  # Node H7
    [0, 0, 0, 0, 4, 0, 2, 0]   # Node H8
]
# Running the greedy TSP algorithm from H1
start_node = 0  # Starting from node H1 (index 0)
path, cost = greedy_tsp(G, start_node)
print("Path:", path)
print("Total cost:", cost)
print("=========================================================")

# Running the greedy TSP algorithm from all starting points
best_path, best_cost = greedy_tsp_all_starts(G)
print("Best Path:", best_path)
print("Best Total Cost:", best_cost)


