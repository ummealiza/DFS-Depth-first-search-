# -*- coding: utf-8 -*-
"""DFS Code

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1mMnGyEp-vO4qA29scwMdQczCBihnaRSY
"""

# Using a Python dictionary to act as an adjacency list
graph = {
    'A' : ['B','C'],
    'B' : ['D', 'E'],
    'C' : ['F'],
    'D' : [],
    'E' : ['F'],
    'F' : []
}
visited = set() # Set to keep track of visited nodes.
# this is function which takes 3 parameters
def dfs(visited, graph, node):
    if node not in visited:
        print (node)
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)

# Driver Code
dfs(visited, graph, 'A')

graph = {
  '25' : ['45', '35'],
  '45' : ['19', '10'],
  '19' : ['2','6'],
  '10' : ['9', '29'],
  '35' : ['17', '23'],
  '17' : ['24', '49'],
  '23' : ['8', '190'],
  '2' : [],
  '6' : [],
  '9' : [],
  '29' : [],
  '24' : [],
  '49' : [],
  '8' : [],
  '190': []
}

visited = set()
def dfs(visited, graph, node):
    if node not in visited:
        print (node)
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)

# Driver Code
dfs(visited, graph, '25')