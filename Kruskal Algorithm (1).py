#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Make a set from the vertices
def make_set(vertice):
   parent[vertice] = vertice


#Find sets that meets the algorithm conditions
def find_set(vertice):
   if parent[vertice] != vertice:
       parent[vertice] = find_set(parent[vertice])
   return parent[vertice]


# joins two sets: set, which includes 'vertice1' and set, which
# includes 'vertice2'
def union(u, v, edges):
   ancestor1 = find_set(u)
   ancestor2 = find_set(v)
   # if u and v are not connected by a path
   if ancestor1 != ancestor2:
       for edge in edges:
           parent[ancestor1] = ancestor2

#The Kruskal Algorithm
def kruskal(graph):
   kmst = set()
   #Make a set of vertices
   for vertice in graph['V']:
       make_set(vertice)
       
   #put edges into a list
   edges = list(graph['E'])
   # sort edges in ascending order
   edges.sort()
   for edge in edges:
       weight, u, v = edge
       # checks if current edge do not close cycle
       if find_set(u) != find_set(v):
           kmst.add(edge)
           union(u, v, edges)

   return kmst


# In[ ]:




