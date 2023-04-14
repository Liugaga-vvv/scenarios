# Solution

```python
def second_smallest(numbers: list[int]) -> int:
    """
    This function takes a list of integers as an input and returns the second smallest integer in the list.
    If the list contains less than two elements, it returns None.
    """
    if len(numbers) < 2:
        return None

    (min1 := float('inf'))
    (min2 := float('inf'))
    for num in numbers:
        if num <= min1:
            min2 = min1
            min1 = num
        elif num < min2:
            min2 = num
    return min2
```
