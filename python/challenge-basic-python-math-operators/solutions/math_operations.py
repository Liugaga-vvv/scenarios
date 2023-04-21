def basic_math_operations(x: int, y: int) -> str:
    # Addition
    sum = x + y
    # Subtraction
    diff = x - y
    # Multiplication
    prod = x * y
    # Division
    div = x / y
    # Modulus
    mod = x % y

    return (
        f"The sum of {x} and {y} is {sum}.\n"
        f"The difference between {x} and {y} is {diff}.\n"
        f"The product of {x} and {y} is {prod}.\n"
        f"The quotient of {x} and {y} is {div}.\n"
        f"The remainder when {x} is divided by {y} is {mod}."
    )
