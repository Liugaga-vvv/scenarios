# Square Multiprocessing

You are given a list of integers. Your task is to calculate the square of each integer using multiprocessing in Python and return the result as a list.

Your solution should include:

1. A function called `square_multiprocessing` that takes a list of integers as input and uses multiprocessing to calculate the square of each integer.
2. The function should return a list of the squared integers.

## Example

```python
>>> from square_multiprocessing import square_multiprocessing
>>> integers = [1, 2, 3, 4, 5]
>>> square_multiprocessing(integers)
[1, 4, 9, 16, 25]
```

## TODO

- Completing `square_multiprocessing.py`

## Requirements

- The input list of integers can have at most 10^5 elements.
- The integers in the input list are non-negative and at most 10^3.
