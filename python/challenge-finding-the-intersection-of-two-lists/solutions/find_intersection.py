def find_intersection(list1, list2):
    intersection = []

    for element in list1:
        if element in list2 and element not in intersection:
            intersection.append(element)

    return intersection
