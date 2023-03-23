# Creating Arrays

Open up a new Python interpreter in Ternimal.

```bash
python3
```

Before we can start working with arrays, we need to create them. NumPy offers several methods for creating arrays, such as:

## 1. np.array()

This function creates an array from a Python list or tuple.

```python
import numpy as np

# Creating an array from a Python list
my_list = [1, 2, 3, 4, 5]
my_array = np.array(my_list)
print(my_array)  # Output: [1 2 3 4 5]

# Creating an array from a Python tuple
my_tuple = (6, 7, 8, 9, 10)
my_array = np.array(my_tuple)
print(my_array)  # Output: [ 6  7  8  9 10]
```

## 2. np.zeros()

This function creates an array of zeros with a given shape.

```python
# Creating an array of zeros
my_array = np.zeros((3, 4))
print(my_array)
# Output:
# [[0. 0. 0. 0.]
#  [0. 0. 0. 0.]
#  [0. 0. 0. 0.]]
```

## 3. np.ones()

This function creates an array of ones with a given shape.

```python
# Creating an array of ones
my_array = np.ones((2, 3))
print(my_array)
# Output:
# [[1. 1. 1.]
#  [1. 1. 1.]]
```

## 4. np.arange()

This function creates an array with evenly spaced values within a given range.

```python
# Creating an array with evenly spaced values
my_array = np.arange(0, 10, 2)
print(my_array)  # Output: [0 2 4 6 8]
```

## 5. np.linspace()

This function creates an array with evenly spaced values between two endpoints.

```python
# Creating an array with evenly spaced values between two endpoints
my_array = np.linspace(0, 1, 5)
print(my_array)  # Output: [0.   0.25 0.5  0.75 1.  ]
```
