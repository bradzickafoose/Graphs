"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph from v1 to v2
        """
        # Check if they exist
        if v1 in self.vertices and v2 in self.vertices:
          # Add the edge
          self.vertices[v1].add(v2)
        else:
          print("ERROR ADDING EDGE: Vertex not found")

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        if vertex_id in self.vertices:
          return self.vertices[vertex_id]
        else:
          return None

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        # Create a q and enqueue starting vertex
        queue = Queue()
        queue.enqueue([starting_vertex])
        # Create a set of traversed vertices
        visited = set()
        # While queue is not empty:
        while queue.size() > 0:
          # dequeue/pop the first vertex
          path = queue.dequeue()
          # if not visited
          if path[-1] not in visited:
            # Do the thing
            print(path[-1])
            # mark as visited
            visited.add(path[-1])
            #enqueue all neighbors
            for next_vert in self.get_neighbors(path[-1]):
              new_path = list(path)
              new_path.append(next_vert)
              queue.enqueue(new_path)


    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        # Create a empty stack and push the starting vertex ID
        stack = Stack()
        stack.push(starting_vertex)
        # Create a Set to store visited vertices
        visited = set()
        # While the stack is not empty
        while stack.size() > 0:
          # Pop the first vertex
          vertex = stack.pop()
          # If that vertex has not been visited
          if vertex not in visited:
            # Mark it as visited
            print(vertex)
            visited.add(vertex)
            # Then add all its neighbors to the top of the stack
            for next_vert in self.get_neighbors(vertex):
              stack.push(next_vert)

    def dft_recursive(self, starting_vertex, visited=None):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        # Check if visited has been initialized
        if visited is None:
          # If not, initialize to an empty set
          visited = set()
        # Mark the node as visited
        print(starting_vertex)
        visited.add(starting_vertex)
        # Call DFT recursive on each nighbor that has not been visited
        for neighbor in self.get_neighbors(starting_vertex):
          if neighbor not in visited:
            self.dft_recursive(neighbor, visited)

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        # Create an empty queue and enqueue A PATH TO the starting vertex ID
        queue = Queue()
        queue.enqueue([starting_vertex])
        #Create a Set to store visited vertices
        visited = set()
        # While the queue is not empty
        while queue.size() > 0:
          # Dequeue the first path
          path = queue.dequeue()
          # Grab the last vertex from the path
          last_vertex = path[-1]
          # If that vertex has not been visited
          if last_vertex not in visited:
            # Check if it is the target
            if last_vertex == destination_vertex:
              # If so, return path
              return path
            # Mark it as visited...
            visited.add(last_vertex)
            # Then add a path to its neighbors to the back of the queue
            for neighbor in self.get_neighbors(last_vertex):
              # Copy the path
              path_copy = path.copy()
              # Append the neighbor to the nsvk
              path_copy.append(neighbor)
              queue.enqueue(path_copy)

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        # Create an empty stack and push A PATH TO the starting vertex ID
        stack = Stack()
        stack.push([starting_vertex])
        #Create a Set to store visited vertices
        visited = set()
        # While the stack is not empty
        while stack.size() > 0:
          # Pop the first path
          path = stack.pop()
          # Grab the last vertex from the path
          last_vertex = path[-1]
          # If that vertex has not been visited
          if last_vertex not in visited:
            # Check if it is the target
            if last_vertex == destination_vertex:
              # If so, return path
              return path
            # Mark it as visited...
            visited.add(last_vertex)
            # Then add a path to its neighbors to the top of the stack
            for neighbor in self.get_neighbors(last_vertex):
              # Copy the path
              path_copy = path.copy()
              # Append the neighbor to the back
              path_copy.append(neighbor)
              stack.push(path_copy)


    def dfs_recursive(self, starting_vertex, destination_vertex, visited=None, path=None):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        # Check if visited has been initialized
        if visited is None:
          # If not, initialize to an empty set
          visited = set()
        # Check if path has been initialized
        if path is None:
          # If not, initialize to an empty array (since it needs to be in order)
          path = []
        visited.add(starting_vertex)
        # Add vertex to the path
        path = path + [starting_vertex]
        # If we are at the destination value, return the path
        if starting_vertex == destination_vertex:
          return path
        # Otherwise, call DFS_recursive on each unvisited neighbor
        for neighbor in self.get_neighbors(starting_vertex):
          if neighbor not in visited:
            new_path = self.dfs_recursive(neighbor, destination_vertex, visited, path)
            if new_path is not None:
              return new_path
        return None

if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))
