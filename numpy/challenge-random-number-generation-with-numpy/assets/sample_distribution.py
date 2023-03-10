import numpy as np

def sample_distribution(probs: np.ndarray) -> int:
    """Sample from a probability distribution and return the index of the selected element.

    Args:
        probs (np.ndarray): A NumPy array representing the probability distribution.

    Returns:
        int: The index of the selected element.
    """
    cum_probs = np.cumsum(probs)
    r = np.random.rand()
    idx = np.where(cum_probs >= r)[0][0]
    return idx
