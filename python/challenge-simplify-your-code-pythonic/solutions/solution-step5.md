## Step 5 Solution

```python
def flatten_list(nested_list: list) -> list:
    """
    Flatten a nested list and convert it to a one-dimensional list.

    Args:
        nested_list (list): A nested list containing elements of any type.

    Return:
        list: A one-dimensional list containing all the elements from the nested list.
    """
    return [item for sublist in nested_list for item in (flatten_list(sublist) if isinstance(sublist, list) else [sublist])]
```
