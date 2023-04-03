import numpy as np

def estimate_pi(n: int) -> float:
    """Estimate the value of pi using a Monte Carlo simulation.

    Args:
        n (int): The number of points to generate.

    Returns:
        float: An estimate of the value of pi.
    """
    x = np.random.rand(n)
    y = np.random.rand(n)
    distance = np.sqrt(x**2 + y**2)
    inside_circle = np.sum(distance < 1)
    pi_estimate = 4 * inside_circle / n
    return pi_estimate