"""main.py
@author lmartin5 <lmartin5@zagmail.gonzaga.edu>

This file contains example runs of how the SimpleGraph class can be
used to search for book thickness and book embeddings of a graph. It also contains examples of 
looking for an embedding using one specific permutation. To use the code to find the book thickness
of graphs, just create new edge sets and change the corresponding parameters, but feel free to experiment
in the other files as well.
"""

from BookThickness.SimpleGraph import SimpleGraph

def main():
    # examples of creating simple graph from edge sets, complete graphs, and complete bipartite graphs
    edge_set = [(1, 2), (2, 3), (3, 4), (7, 1)]
    graph_a = SimpleGraph(edge_set)
    graph_b = SimpleGraph.complete_graph(6)
    graph_c = SimpleGraph.complete_bipartite_graph(4, 4)
    
    print("Here is an example of a graph constructed from a list of edges.")
    print(graph_b, '\n')

    # examples of search for 2-page, then 3-page, embedding of a simple graph given a vertex ordering
    # K6 is not 2-page embeddable, but it is 3-page embeddable
    spine = [1, 2, 3, 4, 5, 6]
    embedding = graph_b.find_n_page_embedding(2, spine)
    print(embedding)
    embedding = graph_b.find_n_page_embedding(3, spine)
    print(embedding, '\n')

    # examples of searching for a valid book embedding with the fewest book pages, and hence finding book thickness
    # the parameter passed in tells the program the smallest page number to start looking
    # bt(K6) = 3
    embedding = graph_b.find_book_embedding(n=2)
    print(embedding, '\n')

    # total graphs embeddings
    print("Searching for an embedding of the total graph of Z_3 X Z_3 ...")
    # in the edge set, each the vertices labeled 1 - 9 will correspond to the elements
    # 1 = (0, 0), 2 = (0, 1), 3 = (0, 2), 4 = (1, 0), 5 = (1, 1), 6 = (1, 2), 7 = (2, 0), 8 = (2, 1), 9 = (2, 2)
    edges = [(1, 2), (1, 3), (1, 4), (1, 7), (2, 3), (2, 6), (2, 9), (3, 5), \
            (3, 8), (4, 7), (4, 8), (4, 9), (5, 6), \
            (5, 7), (5, 8), (5, 9), (6, 7), (6, 8), (6, 9), (8, 9)]
    z3xz3_total_graph = SimpleGraph(edges)
    embedding = z3xz3_total_graph.find_book_embedding(n=3)
    print(embedding)

main()