def dfs(graph, first_vertex):
    visited = set()
    stack = [first_vertex]
    result = []

    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            result.append(vertex)
            # Add all unvisited neighbors to the stack
            for neighbor in reversed(graph[vertex]):
                if neighbor not in visited:
                    stack.append(neighbor)

    return result

def bfs(graph, first_vertex):
    visited = set()
    queue = [first_vertex]
    result = []

    while queue:
        vertex = queue.pop(0)
        if vertex not in visited:
            visited.add(vertex)
            result.append(vertex)
            # Add all unvisited neighbors to the queue
            for neighbor in graph[vertex]:
                if neighbor not in visited:
                    queue.append(neighbor)

    return result

# Example usage:
graph = {
    'A': ['B', 'F'],
    'B': ['A', 'C', 'C'],
    'C': ['B', 'B', 'D', 'E', 'F'],
    'D': ['C'],
    'E': ['C'],
    'F': ['A', 'C']
}

print("DFS traversal start from vertex A:", dfs(graph, 'A'))
print("BFS traversal start from vertex A:", bfs(graph, 'A'))
