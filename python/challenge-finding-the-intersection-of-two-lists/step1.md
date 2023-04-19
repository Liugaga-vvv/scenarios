# Finding the Intersection of Two Lists

Given two lists of integers, list1 and list2, write a Python function `find_intersection(list1, list2)` that returns a new list containing only the elements that are common to both list1 and list2.

## Example Usage

```python
>>> find_intersection([1, 2, 3], [2, 3, 4]) == [2, 3]
>>> find_intersection([2, 2, 3, 4], [1, 2, 2, 4]) == [2, 4]
>>> find_intersection([], [1, 2, 3]) == []
>>> find_intersection([1, 2, 3], []) == []
>>> find_intersection([], []) == []
```

## TODO

- Complete `find_intersection.py`

## Requirements

- The input lists may contain duplicates, but the output list should not.
- The order of the output list does not matter.
- If there are no common elements, return an empty list `[]`.
- Your implementation should have a time complexity of $O(n)$, where $n$ is the length of the longer input list.
