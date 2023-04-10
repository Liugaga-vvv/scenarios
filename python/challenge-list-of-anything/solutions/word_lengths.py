def word_lengths(words: list) -> list:
    """Given a list of words, this function returns a new list containing the length of each word in the original list.

    Args:
        words(list): A list of strings,e.g.["apple", "banana", "cherry", "date"]

    Returns:
        resulst(list): A list of integers representing the length of each word,e.g. [5, 6, 6, 4]
    """
    result = [len(word) for word in words]

    return result
