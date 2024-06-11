# Adjacency List representation in Python
class AdjNode:
    def __init__(self, data):
        self.vertex = data
        self.next = None

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [None] * self.V

    # Function to add an edge in an undirected graph
    def add_edge(self, src, dest):
        # Adding the node to the source node
        node = AdjNode(dest)
        node.next = self.graph[src]
        self.graph[src] = node

        # Adding the source node to the destination as it is an undirected graph
        node = AdjNode(src)
        node.next = self.graph[dest]
        self.graph[dest] = node

    # Function to print the graph
    def print_graph(self):
        for i in range(self.V):
            temp = self.graph[i]
            print("Adjacency list of vertex {}: ".format(i), end="")
            while temp:
                print(" -> {}".format(temp.vertex), end="")
                temp = temp.next
            print(" \n")

# Driver program to test the above graph class
graph = Graph(4)
graph.add_edge(0, 1)
graph.add_edge(0, 2)
graph.add_edge(0, 3)
graph.add_edge(1, 0)
graph.add_edge(1, 2)
graph.add_edge(2, 0)
graph.add_edge(2, 1)
graph.add_edge(3, 0)

graph.print_graph()

#output
# Adjacency list of vertex 0:  -> 3 -> 2 -> 1

#================================================================================================
class Graph:
    # Initialisasi matriks
    def __init__(self, size):
        self.adjMatrix = []
        for i in range(size):
            self.adjMatrix.append([0 for _ in range(size)])
        self.size = size

    # Tambah edges
    def add_edge(self, v1, v2):
        if v1 == v2:
            print("Verteks yang sama %d dan %d" % (v1, v2))
            return
        self.adjMatrix[v1][v2] = 1
        self.adjMatrix[v2][v1] = 1

    # Hapus edges
    def remove_edge(self, v1, v2):
        if self.adjMatrix[v1][v2] == 0:
            print("Tidak terdapat edge antara %d dan %d" % (v1, v2))
            return
        self.adjMatrix[v1][v2] = 0
        self.adjMatrix[v2][v1] = 0

    def __len__(self):
        return self.size

    # Print the matrix
    def print_matrix(self):
        for row in self.adjMatrix:
            for val in row:
                print('{:4}'.format(val), end=' ')
            print()

# Driver program to test the above graph class
g = Graph(5)
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 0)
g.add_edge(2, 3)

g.print_matrix()

# output
#    0    1    1    0    0