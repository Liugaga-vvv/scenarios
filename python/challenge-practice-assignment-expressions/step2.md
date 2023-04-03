# Assignment Expression in List Comprehension

In this step, let's use the walrus operator within a list comprehension.

## Syntax format

Assignment expressions can also be used in list comprehensions.

Example:

```python
"""
Compute the square root of the elements in the nums array and keep the values whose square root is greater than 5
"""

nums = [16, 36, 49, 64]

# General Style
[i ** 0.5 for i in nums if i ** 0.5 > 5]

# Assignment Expression Style
[n for i in nums if (n := i ** 0.5) > 5]
```

## Requirements

- Completing `/home/labex/project/list_comprehension.py`.
- Implements the `list_comprehension` function, use the walrus expression to Generate a list of squares of even numbers between `1` and `10`, and return the list.
