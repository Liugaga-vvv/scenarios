## Step 4 Solution

```python
def sum_two_lists(list1: list, list2: list) -> list:
    """
    Element-wise sum of two input lists.
    Args:
        list1 (list): The first list of numbers to be summed.
        list2 (list): The second list of numbers to be summed, of equal length to `list1`.

    Returns:
        list: A new list containing the element-wise sum of `list1` and `list2`.

    """
    sum_list = [x + y for x, y in zip(list1, list2)]
    return sum_list
```
