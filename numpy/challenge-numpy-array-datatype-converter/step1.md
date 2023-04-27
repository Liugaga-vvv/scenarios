# NumPy Array Datatype Conversion

## Problem Statement:

You are given a list of integers. Write a Python function that converts the list into a numpy array and changes the datatype of the array to a specified datatype. The function should return the modified numpy array.

### Function Signature:

```python
def convert_to_dtype(lst: list[int], dtype: str) -> numpy.ndarray:
    """
    Converts a list of integers to numpy array and changes its datatype.

    Args:
    lst (list[int]): List of integers to be converted to numpy array.
    dtype (str): The datatype to which the numpy array should be converted.

    Returns:
    numpy.ndarray: The modified numpy array.
    """
```

### Input

- A list of integers `lst` where (0 <= len(lst) <= 10^6)
- A string `dtype` representing the datatype to which the numpy array should be converted. The allowed values for `dtype` are:
  - 'int8'
  - 'int16'
  - 'int32'
  - 'int64'
  - 'uint8'
  - 'uint16'
  - 'uint32'
  - 'uint64'
  - 'float16'
  - 'float32'
  - 'float64'
  - 'float128'

### Output

- A numpy array of the same shape as the input list but with the specified datatype.

### Example

```python
>>> lst = [1, 2, 3, 4, 5]
>>> convert_to_dtype(lst, 'float64')
array([1., 2., 3., 4., 5.])
```
