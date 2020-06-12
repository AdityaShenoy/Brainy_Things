class Node:

  def __init__(self, value):
    self.value = value
    self.neighbors = []

class Graph:

  def __init__(self):
    self.nodes = dict()
  
  def addEdge(self, node1, node2):
    if node1 not in self.nodes:
      self.nodes[node1] = Node(node1)
    if node2 not in self.nodes:
      self.nodes[node2] = Node(node2)
    self.nodes[node1].neighbors.append(self.nodes[node2])
  
  def bfs(self, start, key):
    if start not in self.nodes:
      print('Node not present in the graph')
      return
    
    visited = {node: False for node in self.nodes.values()}

    queue = [self.nodes[start]]
    visited[self.nodes[start]] = True

    while queue:

      node = queue.pop(0)
      print(node.value, end=' ')
      if node.value == key:
        print('\nKey found')
        return

      for neighbor in node.neighbors:
        if not visited[neighbor]:
          queue.append(neighbor)
          visited[neighbor] = True
      
    print('\nKey not found')

  
g = Graph()

edges = [(1, 2), (1, 3), (2, 4), (2, 5), (3, 5), (4, 5), (4, 6), (5, 6)]
for node1, node2 in edges:
  g.addEdge(node1, node2)
  g.addEdge(node2, node1)

g.bfs(1, 7)