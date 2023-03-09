import numpy as np

def tensor_contract(A: np.ndarray, B: np.ndarray) -> np.ndarray:
    """
    Perform tensor contraction between two tensors using NumPy's einsum function.

    Parameters:
    -----------
    A : numpy.ndarray
        Input tensor A of shape (M, N, K).
    B : numpy.ndarray
        Input tensor B of shape (K, L).

    Returns:
    --------
    numpy.ndarray
        Resulting tensor of shape (M, J, L), where J is the dimension not contracted.
    """
    # TODO: implement this function
    # Note: Do not change the existing code