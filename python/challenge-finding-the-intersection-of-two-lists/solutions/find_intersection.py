# This function takes two lists as parameters and returns a list containing their intersection.
def find_intersection(list1, list2):
    # Initialize an empty list to store the intersection.
    intersection = []

    # Iterate through each element in the first list.
    for element in list1:
        # Check if the element is in the second list and not already in the intersection.
        if element in list2 and element not in intersection:
            # Add the element to the intersection list.
            intersection.append(element)

    # Return the intersection list.
    return intersection
