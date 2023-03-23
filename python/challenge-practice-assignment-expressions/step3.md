# Assignment Expression in a While Loop

In this step, we will use the walrus operator to simplify a while loop.

## Syntax format

Assignment expressions can also simplify the steps of a loop.

Example:

```python
"""
Enter a data and determine if it is equal to "123".
"""

# General Style
while True:
    i = input()
    if i == "123":
        break

# Assignment Expression Style
while (i := input()) != "123":
    continue
```

## Requirements

- Completing `/home/labex/project/while_loop.py`.
- Implements the `while_loop` function, read integers from the user until they enter `0`. Calculate and return the sum of all entered numbers using the walrus operator.
