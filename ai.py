graph = {
  'A': ['B', 'C'],
  'B': ['A', 'D', 'E'],
  'C': ['A', 'F'],
  'D': ['B'],
  'E': ['B', 'F'],
  'F': ['C', 'E']
}

#algorithm BFS
visited = []
queue = []
def BFS(visited, graph, node):
    visited.append(node)
    queue.append(node)
    while queue:
        m = queue.pop(0)
        print(m, end=" ")
        for n in graph[m]:
            if n not in visited:
                queue.append(n)
                visited.append(n)
#to use
#BFS(visited, graph, 'A')   


#algoritm DFS
visited = set()
def DFS(visited, graph, node):
  if node not in visited:
    print(node, end= " ")
    visited.add(node)
    for n in graph[node]:
      DFS(visited, graph, n)

#to use
#DFS(visited, graph, 'A')

import mesa
import time

class agent_BFS(mesa.Agent):
  def __init__(self, ID, model):
    super().__init__(ID, model)
    self.graph = self.model.graph
    self.node = self.model.node 
    self.goal = self.model.goal

  def BFS(self, graph, node, goal):
    visited = []
    file = []

    visited.append(node)
    file.append(node)
    while file:
      m = file.pop(0)
      print(m, end=" ")
      if m == goal:
        return 1
      for n in graph[m]:
        if n not in visited:
          file.append(n)
          visited.append(n)
    return 0

  def step(self):
    start_time = time.perf_counter()
    self.BFS(self.graph, self.node, self.goal)
    end_time = time.perf_counter()
    total_time = end_time -start_time
    print(f"BFS time est: {total_time}")


class agent_DFS(mesa.Agent):
  def __init__(self, ID, model):
    super().__init__(ID, model)
    self.graph = self.model.graph
    self.node = self.model.node 
    self.goal = self.model.goal
    self.visited = set()
    self.end_time = 0
    self.found = False

  def DFS(self, graph, node, goal, visited):
    if node not in visited:
      if not self.found:
        visited.add(node)
        print(node, end=" ")
        if node == goal:
          self.end_time = time.perf_counter()
          self.found = True
        for n in graph[node]:
          self.DFS(graph, n, goal, visited)

  def step(self):
    start_time = time.perf_counter()
    self.DFS(self.graph, self.node, self.goal, self.visited)
    total_time = self.end_time - start_time
    print(f"DFS time est {total_time}")

class env(mesa.Model):
  def __init__(self):
    super().__init__()
    self.graph = {'5' : ['3','7'],
                  '3' : ['2', '4'],
                  '7' : ['8'],
                  '2' : [],
                  '4' : ['8'],
                  '8' : []}
    self.node = '5'
    self.goal = '8'
    self.A = agent_BFS(0, self)
    self.B = agent_DFS(1, self)
    self.plan = mesa.time.SimultaneousActivation(self)
    self.plan.add(self.A)
    self.plan.add(self.B)

  def step(self):
    self.plan.step()

model = env()
model.step()

