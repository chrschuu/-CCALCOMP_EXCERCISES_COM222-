# -*- coding: utf-8 -*-
"""exercise1.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/github/robitussin/CCALCOMP_EXERCISES/blob/main/exercise1.ipynb

# Exercise 1

Please follow the instructions in each number. Do not remove or modify the pre-defined code!
"""

# Add a vertex to the set of vertices and the graph
def add_vertex(v):
  global graph
  global vertices_no
  global vertices
  if v in vertices:
    print("Vertex ", v, " already exists")
  else:
    vertices_no = vertices_no + 1
    vertices.append(v)
    if vertices_no > 1:
        for vertex in graph:
            vertex.append(0)
    temp = []
    for i in range(vertices_no):
        temp.append(0)
    graph.append(temp)

# Add an edge between vertex v1 and v2 with edge weight e
def add_edge(v1, v2, e):
    global graph
    global vertices_no
    global vertices
    # Check if vertex v1 is a valid vertex
    if v1 not in vertices:
        print("Vertex ", v1, " does not exist.")
    # Check if vertex v1 is a valid vertex
    elif v2 not in vertices:
        print("Vertex ", v2, " does not exist.")
    # Since this code is not restricted to a directed or
    # an undirected graph, an edge between v1 v2 does not
    # imply that an edge exists between v2 and v1
    else:
        index1 = vertices.index(v1)
        index2 = vertices.index(v2)
        graph[index1][index2] = e

# Print the graph
def print_graph():
  global graph
  global vertices_no
  for i in range(vertices_no):
    for j in range(vertices_no):
      if graph[i][j] != 0:
        print(vertices[i], " -> ", vertices[j],
              " edge weight: ", graph[i][j])

# stores the vertices in the graph
vertices = []
# stores the number of vertices in the graph
vertices_no = 0
graph = []

"""<img src="https://github.com/robitussin/CCALCOMP_EXERCISES/blob/main/images/directed%20graph2.png?raw=true"/>

1. Print the edges and vertices of the graph in set representation. (`25 points`)
"""

print("Vertices: A, B, C, D, E")
print("Edges:\nA->D | Cost: 60\nA->C | Cost: 12\nE->A | Cost: 7\nC->D | Cost: 32\nC->B | Cost: B\nB->A | Cost: 10")

"""2. Implement the weighted graph in python code. Use the print_graph() function. (`25 points`)"""

# Add a vertex to the set of vertices and the graph
def add_vertex(v):
    global graph
    global vertices_no
    global vertices
    if v in vertices:
        print("Vertex ", v, " already exists")
    else:
        vertices_no = vertices_no + 1
        vertices.append(v)
        if vertices_no > 1:
            for vertex in graph:
                vertex.append(0)
        temp = []
        for i in range(vertices_no):
            temp.append(0)
        graph.append(temp)

# Add an edge between vertex v1 and v2 with edge weight e
def add_edge(v1, v2, e):
    global graph
    global vertices_no
    global vertices
    # Check if vertex v1 is a valid vertex
    if v1 not in vertices:
        print("Vertex ", v1, " does not exist.")
    # Check if vertex v2 is a valid vertex
    elif v2 not in vertices:
        print("Vertex ", v2, " does not exist.")
    else:
        index1 = vertices.index(v1)
        index2 = vertices.index(v2)
        graph[index1][index2] = e

# Print the graph
def print_graph():
    global graph
    global vertices_no
    for i in range(vertices_no):
        for j in range(vertices_no):
            if graph[i][j] != 0:
                print(vertices[i], " -> ", vertices[j], " edge weight: ", graph[i][j])


# stores the vertices in the graph
vertices = []
# stores the number of vertices in the graph
vertices_no = 0
graph = []

# Add vertices
add_vertex('A')
add_vertex('B')
add_vertex('C')
add_vertex('D')
add_vertex('E')

# Add edges with weights
add_edge('A', 'B', 10)
add_edge('E', 'A', 7)
add_edge('B', 'C', 20)
add_edge('C', 'A', 12)
add_edge('A', 'D', 60)
add_edge('D', 'C', 32)

# Print the graph
print_graph()

"""3. (Travelling Salesman Problem)
You decided to go on a trip around the philippines. Being a computer scientist, you wanted to find the route that would cost the least amount of money to travel all four cities. Find the route and print the total cost of the optimal route. (`50 points`)

(Note: You can start at any origin (e.g. Manila))

<img src="https://github.com/robitussin/CCALCOMP_EXERCISES/blob/main/images/trip.png?raw=true" width="500" height="600"/>
"""

import copy

# Clear global data
vertices = []
num_vertices = 0
graph = []

# Define city names and edge details
cities = ['Manila', 'Tacloban', 'Davao', 'Puerto Princesa']
num_cities = len(cities)
city_edges = [['Manila', 'Tacloban', 1000], ['Tacloban', 'Davao', 2000],
              ['Davao', 'Puerto Princesa', 4000], ['Puerto Princesa', 'Manila', 8000],
              ['Manila', 'Davao', 5000], ['Puerto Princesa', 'Tacloban', 1500]]

# Function to add vertices to the graph
def add_vertex(city):
    vertices.append(city)

# Function to add edges to the graph
def add_edge(city1, city2, cost):
    index1 = vertices.index(city1)
    index2 = vertices.index(city2)
    graph[index1][index2] = cost

# Create graph
for _ in range(num_cities):
    graph.append([0] * num_cities)

for city in cities:
    add_vertex(city)

for edge in city_edges:
    add_edge(edge[0], edge[1], edge[2])
    add_edge(edge[1], edge[0], edge[2])

# Breadth-First Search (BFS)
min_cost = float('inf')
min_path = []

queue = [[[i], 0] for i in range(num_cities)]

while queue:
    front = queue.pop(0)
    visited = len(front[0])

    if visited == num_cities:
        if min_cost > front[1]:
            min_path, min_cost = front
            continue

    for i in range(num_cities):
        cost = graph[front[0][-1]][i]
        if cost <= 0 or i in front[0]:
            continue

        temp = copy.deepcopy(front)
        temp[0].append(i)
        temp[1] += cost
        queue.append(temp)

# Output results
route = '->'.join([cities[i] for i in min_path])
print(f"Minimum cost: {min_cost} pesos")
print(f"Route: {route}")