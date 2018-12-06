from random import choices
import networkx as nx

def percolate(G, beta, unWeighted=True):
    '''
    percolate G with probability beta
    Return: percolated subgraphs
    Note: Here we don't consider Directed/Weighted graph 
    '''
    edges_percolated = []
    G_percolated = nx.Graph()
    assert(G_percolated.number_of_nodes() == 0)
    numPercolatedEdges = int(beta*G.number_of_edges())
    G_percolated.add_nodes_from(list(G.nodes))
    if unWeighted:
        edges_percolated = choices(list(G.edges), k=numPercolatedEdges)
        assert(len(edges_percolated) ==  numPercolatedEdges)
        G_percolated.add_edges_from(edges_percolated)
#     else:
#         bond percolation probability depends on the edge's weight
    return G_percolated