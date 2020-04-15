import sys
sys.path.append('../graph')
from util import Queue

def earliest_ancestor(ancestors, starting_node):
    family = Graph()

    for (parent, child) in ancestors:
      family.add_vertex(parent)
      family.add_vertex(child)
      family.add_edge(child, parent)

    # BFS
    queue = Queue()
    queue.enqueue([starting_node])

    longest_path_length = 1
    earliest_ancestor = -1

    while queue.size() > 0:
      path = queue.dequeue()
      current_node = path[-1]

      if len(path) >= longest_path_length and current_node < earliest_ancestor:
          longest_path_length = len(path)
          earliest_ancestor = current_node

      if len(path) > longest_path_length:
        longest_path_length = len(path)
        earliest_ancestor = current_node

      neighbors = family.vertices[current_node]
      for ancestor in neighbors:
        path_copy = list(path)
        path_copy.append(ancestor)
        queue.enqueue(path_copy)

    return earliest_ancestor


class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        if vertex_id not in self.vertices:
          self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph from v1 to v2
        """
        # Check if they exist
        if v1 in self.vertices and v2 in self.vertices:
          # Add the edge
          self.vertices[v1].add(v2)


test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]
starting_node = 7
print(earliest_ancestor(test_ancestors, starting_node)) # 4