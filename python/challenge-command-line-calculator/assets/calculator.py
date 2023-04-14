import argparse

def add(a: int, b: int) -> int:
    """Return the sum of two numbers."""
    return a + b

def subtract(a: int, b: int) -> int:
    """Return the difference of two numbers."""
    return a - b

def multiply(a: int, b: int) -> int:
    """Return the product of two numbers."""
    return a * b

def divide(a: int, b: int) -> float:
    """Return the quotient of two numbers."""
    return a / b

if __name__ == '__main__':
    # TODO: Creat a parser and a group.
    parser = None
    group = None

    # TODO: Add and parse the arguments.
    # The add arugument is already implemented for you as an example.You will need to add the other three arguments.
    group.add_argument('-a', '--add', nargs=2, type=int, metavar=('NUM1', 'NUM2'), help='add NUM1 and NUM2')

    # TODO: Output management.