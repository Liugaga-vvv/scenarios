# This function takes a string as a parameter and returns the number of duplicate characters in it.
def count_duplicates(s: str) -> int:
    # Create a dictionary to store the character counts.
    counts = {}
    # Iterate through each character in the string.
    for char in s:
        # If the character is not already in the counts dictionary, add it with a count of 0.
        if char not in counts:
            counts[char] = 0
        # Increment the count for the current character.
        counts[char] += 1
    # Initialize a count variable to 0.
    count = 0
    # Iterate through each character in the counts dictionary.
    for char in counts:
        # If the count for the current character is greater than 1, increment the count variable.
        if counts[char] > 1:
            count += 1
    # Return the final count of duplicate characters.
    return count
