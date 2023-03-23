# Mathematical Operations

NumPy provides a variety of mathematical operations for arrays. These operations can be performed on one or more arrays.

## Open the Python Shell

Open the Python shell by typing the following command in the terminal.

```bash
python3
```

## Import NumPy

NumPy is already installed，you can import it in your Python code:

```python
import numpy as np
```

## Element-wise Operations

Element-wise operations are operations performed on each element in the array.

Let's create two arrays and perform some element-wise operations:

```python
# Creating two arrays
arr1 = np.array([1, 2, 3, 4])
arr2 = np.array([5, 6, 7, 8])

# Adding two arrays
print("Adding two arrays: ", arr1 + arr2)

# Subtracting two arrays
print("Subtracting two arrays: ", arr1 - arr2)

# Multiplying two arrays
print("Multiplying two arrays: ", arr1 * arr2)

# Dividing two arrays
print("Dividing two arrays: ", arr1 / arr2)

# Finding the remainder after division of two arrays
print("Modulo of two arrays: ", arr1 % arr2)

# Raising elements of an array to a power
print("Raising an array to a power: ", arr1 ** 2)
```

Output:

```python
Adding two arrays:  [ 6  8 10 12]
Subtracting two arrays:  [-4 -4 -4 -4]
Multiplying two arrays:  [ 5 12 21 32]
Dividing two arrays:  [0.2        0.33333333 0.42857143 0.5       ]
Modulo of two arrays:  [1 2 3 4]
Raising an array to a power:  [ 1  4  9 16]
```

## Array-wise Operations

Array-wise operations are operations performed on the entire array.

Let's create an array and perform some array-wise operations:

```python
# Creating an array
arr = np.array([1, 2, 3, 4])

# Finding the sum of all elements in the array
print("Sum of array: ", np.sum(arr))

# Finding the product of all elements in the array
print("Product of array: ", np.prod(arr))

# Finding the minimum element in the array
print("Minimum element in array: ", np.min(arr))

# Finding the maximum element in the array
print("Maximum element in array: ", np.max(arr))

# Finding the average of all elements in the array
print("Average of array: ", np.mean(arr))

# Finding the standard deviation of all elements in the array
print("Standard deviation of array: ", np.std(arr))
```

Output:

```python
Sum of array:  10
Product of array:  24
Minimum element in array:  1
Maximum element in array:  4
Average of array:  2.5
Standard deviation of array:  1.118033988749895
```
