import numpy as np

def generate_graph(n: int, p: float) -> np.ndarray:
    """Generate a random graph with n nodes and probability p of an edge between any two nodes.

    Args:
        n (int): The number of nodes in the graph.
        p (float): The probability of an edge between any two nodes.

    Returns:
        np.ndarray: A NumPy array representing the adjacency matrix of the graph.
    """
    adj_matrix = np.random.choice([0, 1], size=(n, n), p=[1-p, p])
    adj_matrix = adj_matrix + adj_matrix.T - np.diag(adj_matrix.diagonal())
    return adj_matrix