"""SimpleGraph.py
@author lmartin5

This file contains the SimpleGraph class. It represents a simple 
graph (undirected edges, no loops, no multi-edges). Graphs are created 
with edge sets composed of natural number pairs. The highest number that appears
in the edge set is assumed to be the number of vertices, so for an 8 vertex graph
the highest number used in the edge set should be 8. It does not matter which order
the vertices are in the edge-tuples, but they will be rearranged to be ascending order
for ease in finding the book embedding of the graph.

ex.
edge_set = [(1, 2), (2, 3), (1, 3)]
my_graph = SimpleGraph(edge_set)
"""

import copy
import itertools

class SimpleGraph():

    def __init__(self, edge_set):
        self.verify_edge_set(edge_set)
        self.num_edges = len(self.edges)

        highest_vertex_number = 0
        for edge in self.edges:
            if edge[0] > highest_vertex_number:
                highest_vertex_number = edge[0]
            if edge[1] > highest_vertex_number:
                highest_vertex_number = edge[1]
        self.num_vertices = highest_vertex_number

        self.vertices = list(range(1, self.num_vertices + 1))

    def verify_edge_set(self, edges):
        edge_set = []

        for edge in edges:
            if (type(edge) is not tuple) or (len(edge) is not 2):
                raise Exception("All edges in a SimpleGraph must be 2-tuples.")
            
            vertex_a = edge[0]
            vertex_b = edge[1]

            if (type(vertex_a) is not int) or (type(vertex_b) is not int):
                raise Exception("Only integers can be used as vertices in a SimpleGraph.")

            if (vertex_a < 1) or (vertex_b < 1):
                raise Exception("Only natural numbers can be used as vertices in a SimpleGraph.")

            # ignoring any loop edges or repeat edges
            if vertex_a is not vertex_b:
                if vertex_a < vertex_b:
                    new_edge = (vertex_a, vertex_b)
                else:
                    new_edge = (vertex_b, vertex_a)

                edge_seen = False
                for seen_edge in edge_set:
                    if (seen_edge[0] is new_edge[0]) and (seen_edge[1] is new_edge[1]):
                        edge_seen = True

                if not edge_seen:
                    edge_set.append(new_edge)

        self.edges = edge_set

    def copy(self, deepcopy=True):
        graph_copy = SimpleGraph([])
        graph_copy.num_edges = self.num_edges
        graph_copy.num_vertices = self.num_vertices
        graph_copy.vertices = copy.copy(self.vertices)

        if deepcopy:
            graph_copy.edges = copy.deepcopy(self.edges)
        else:
            graph_copy.edges = copy.copy(self.edges)

        return graph_copy

    def __str__(self):
        pretty_print = "SimpleGraph G = (V, E)\n"
        pretty_print += "|V| = " + str(self.num_vertices) + ", |E| = " + str(self.num_edges) + "\n"
        pretty_print += "V = {"
        for vertex in self.vertices:
            pretty_print += str(vertex) + ", "
        pretty_print += "\b\b}\n"
        pretty_print += "E = {"
        for edge in self.edges:
            pretty_print += "{" + str(edge[0]) + ", " + str(edge[1]) + "}, "
        pretty_print += "\b\b}"
        return pretty_print

    def complete_graph(n):
        edge_set = []
        verts = list(range(1, n + 1))
        for element in itertools.product(verts, verts):
            if element[0] < element[1]:
                edge_set.append(element)

        return SimpleGraph(edge_set)

    def complete_bipartite_graph(n, m):
        edge_set = []
        set_a = list(range(1, n + 1))
        set_b = list(range(n + 1, n + m + 1))
        for element in itertools.product(set_a, set_b):
            edge_set.append(element)

        return SimpleGraph(edge_set)
    