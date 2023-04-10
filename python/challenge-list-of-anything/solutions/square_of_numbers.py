def square_of_numbers(numbers: list) -> list:
    """Given a list of numbers, this function returns a new list containing the square of each number in the original list.

    Args:
        numbers(list): A list of integers, e.g. [1,2,3,4]

    Return:
        result(list): A list of integers representing the square of each number, e.g. [1,4,9,16]
    """
    result = [x**2 for x in numbers]
    return result
