import numpy as np

def generate_markov_chain(n: int) -> tuple[np.ndarray, np.ndarray]:
    """Generate a random Markov chain with n states.

    Args:
        n (int): The number of states in the Markov chain.

    Returns:
        tuple[np.ndarray, np.ndarray]: A tuple of the transition matrix and initial state vector.
    """
    transition_matrix = np.random.rand(n, n)
    transition_matrix /= np.sum(transition_matrix, axis=1, keepdims=True)
    init_state = np.random.rand(n)
    init_state /= np.sum(init_state)
    return transition_matrix, init_state
