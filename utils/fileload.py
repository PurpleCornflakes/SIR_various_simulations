import networkx as nx
import numpy as np
from scipy.io import loadmat
from scipy.sparse import issparse

def load_matfile(file_, variable_name="network", unDirected=True, unWeighted = True):
    mat_variables = loadmat(file_)
    mat_matrix = mat_variables[variable_name]
    if issparse(mat_matrix):
        if unDirected:
            G = nx.Graph()
        else:
            G = nx.DiGraph()
        '''
        from_nodes: cx.row
        to_nodes: cx.col
        link weights: cx.data
        '''
        cx = mat_matrix.tocoo()
        if unWeighted:
            edge_list = np.array([cx.row, cx.col]).T
            G.add_edges_from(edge_list)
        else:
            edge_list = np.array([cx.row, cx.col, cx.data]).T
            G.add_weighted_edges_from(edge_list)
    return G