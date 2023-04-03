import numpy as np

def shuffle_deck() -> np.ndarray:
    """Simulate shuffling a deck of cards and return the shuffled deck.

    Returns:
        np.ndarray: A NumPy array representing the shuffled deck of cards.
    """
    deck = np.arange(1, 53)
    shuffled_deck = np.random.permutation(deck)
    return shuffled_deck