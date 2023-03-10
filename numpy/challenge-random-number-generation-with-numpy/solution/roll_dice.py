import numpy as np

def roll_dice() -> int:
    """Simulate the rolling of two six-sided dice and return the sum.

    Returns:
        int: The sum of the two dice rolls.
    """
    dice1 = np.random.randint(1, 7)
    dice2 = np.random.randint(1, 7)
    return dice1 + dice2