# NumPy Array Attributes

NumPy arrays have several attributes that provide information about the array's properties, such as:

- `shape`: A tuple representing the dimensions of the array.
- `size`: The total number of elements in the array.
- `ndim`: The array's dimensions (axes).
- `dtype`: The data type of the array elements.
- `itemsize`: The size in bytes of each element in the array.

## Using Array Attributes

Now, We can use these attributes in practice:

```python
# Create a 2D array
array = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Get the shape of the array
print("Shape:", array.shape)  # Output: (3, 3)

# Get the size of the array
print("Size:", array.size)  # Output: 9

# Get the number of dimensions of the array
print("Number of dimensions:", array.ndim)  # Output: 2

# Get the data type of the array elements
print("Data type:", array.dtype)  # Output: int64 (or int32, depending on your system)

# Get the size in bytes of each element in the array
print("Item size:", array.itemsize)  # Output: 8 (or 4, depending on your system)
```
