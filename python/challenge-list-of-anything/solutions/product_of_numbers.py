def product_of_numbers(list1: list, list2: list) -> list:
    """Given two lists of numbers, this function returns a new list containing the product of each pair of numbers from the corresponding positions in the original lists.

    Args:
        param list1(list): A list of integers, e.g. [1, 2, 3, 4]
        param list2(list): A list of integers, e.g. [10, 20, 30, 40]

    Returns:
        A list of integers representing the product of each pair of numbers, e.g. [10, 40, 90, 160]
    """
    result = [x * y for x, y in zip(list1, list2)]

    return result
