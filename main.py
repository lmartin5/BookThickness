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
    print(graph_b)

    # examples of search for 2-page, then 3-page, embedding of a simple graph given a vertex ordering
    # K6 is not 2-page embeddable, but is 3-page embeddable
    spine = [1, 2, 3, 4, 5, 6]
    embedding = graph_b.find_n_page_embedding(2, spine)
    print(embedding)
    embedding = graph_b.find_n_page_embedding(3, spine)
    print(embedding)

main()