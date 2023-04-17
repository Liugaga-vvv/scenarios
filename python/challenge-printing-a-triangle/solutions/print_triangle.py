# This function takes a height as a parameter and prints a triangle made of asterisks with that height.
def print_triangle(height):
    # Iterate through the range 1 to the given height (inclusive).
    for i in range(1, height+1):
        # Print i asterisks.
        print('*' * i)
