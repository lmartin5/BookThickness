"""main.py
@author lmartin5

This file contains example runs of how the GraphManager class can be
used to search for one-page Mobius book embeddings of a graph. It also contains examples of 
looking for an embedding for one permutation.
"""

from BookThickness.SimpleGraph import SimpleGraph

def main():
    # examples of creating simple graph from edge sets, complete graphs, and complete bipartite graphs
    edge_set = [(1, 2), (2, 3), (3, 4), (7, 1)]
    graph_a = SimpleGraph(edge_set)
    graph_b = SimpleGraph.complete_graph(6)
    graph_c = SimpleGraph.complete_bipartite_graph(4, 4)
    print(graph_a, graph_b, graph_c, sep="\n\n")

main()