# djikstra algorithm

import heapq

def shortestPath(graph, start, end):
    # Create a priority queue to store vertices that need to be visited
    queue = []
    # Push the starting vertex to the queue
    heapq.heappush(queue, (0, start))
    # Create a dictionary to store the shortest distance from the start vertex to each vertex
    distance = {vertex: float('infinity') for vertex in graph}
    distance[start] = 0
    # Create a dictionary to store the previous vertex in the shortest path
    previous = {vertex: None for vertex in graph}
    # Create a set to store visited vertices
    visited = set()
    
    while queue:
        # Pop the vertex with the smallest distance from the queue
        current_distance, current_vertex = heapq.heappop(queue)
        # If the vertex has been visited, skip it
        if current_vertex in visited:
            continue
        # Mark the vertex as visited
        visited.add(current_vertex)
        # If the current vertex is the end vertex, reconstruct the shortest path
        if current_vertex == end:
            path = []
            while previous[current_vertex] is not None:
                path.insert(0, current_vertex)
                current_vertex = previous[current_vertex]
            path.insert(0, start)
            return path
        # Update the distance to each neighbor of the current vertex
        for neighbor, weight in graph[current_vertex].items():
            distance_to_neighbor = current_distance + weight
            if distance_to_neighbor < distance[neighbor]:
                distance[neighbor] = distance_to_neighbor
                previous[neighbor] = current_vertex
                heapq.heappush(queue, (distance_to_neighbor, neighbor))
    
    return None

# Example usage:
graph = {
    'A': {'B': 5, 'C': 3},
    'B': {'A': 5, 'C': 2, 'D': 1},
    'C': {'A': 3, 'B': 2, 'D': 3},
    'D': {'B': 1, 'C': 3}
}

print("Shortest path from A to D:", shortestPath(graph, 'A', 'D'))


# ADJACENCY MATRIX

def shortestPath(graph, start, end):
    # Create a priority queue to store vertices that need to be visited
    queue = []
    # Push the starting vertex to the queue
    heapq.heappush(queue, (0, start))
    # Create a dictionary to store the shortest distance from the start vertex to each vertex
    distance = {vertex: float('infinity') for vertex in range(len(graph))}
    distance[start] = 0
    # Create a dictionary to store the previous vertex in the shortest path
    previous = {vertex: None for vertex in range(len(graph))}
    # Create a set to store visited vertices
    visited = set()
    
    while queue:
        # Pop the vertex with the smallest distance from the queue
        current_distance, current_vertex = heapq.heappop(queue)
        # If the vertex has been visited, skip it
        if current_vertex in visited:
            continue
        # Mark the vertex as visited
        visited.add(current_vertex)
        # If the current vertex is the end vertex, reconstruct the shortest path
        if current_vertex == end:
            path = []
            while previous[current_vertex] is not None:
                path.insert(0, current_vertex)
                current_vertex = previous[current_vertex]
            path.insert(0, start)
            return path
        # Update the distance to each neighbor of the current vertex
        for neighbor, weight in enumerate(graph[current_vertex]):
            if weight > 0:
                distance_to_neighbor = current_distance + weight
                if distance_to_neighbor < distance[neighbor]:
                    distance[neighbor] = distance_to_neighbor
                    previous[neighbor] = current_vertex
                    heapq.heappush(queue, (distance_to_neighbor, neighbor))
    
    return None

# Example usage:
graph = [
    [0, 5, 3, 0],
    [5, 0, 2, 1],
    [3, 2, 0, 3],
    [0, 1, 3, 0]
]

print("Shortest path from 0 to 3:", shortestPath(graph, 0, 3))