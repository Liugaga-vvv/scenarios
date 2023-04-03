# Data Types

NumPy arrays can store elements of different data types, such as integers, floats, and booleans. NumPy offers a range of data types, including:

| Data Type  | Description                                     |
| ---------- | ----------------------------------------------- |
| int\_      | Integer                                         |
| int8       | 8-bit integer                                   |
| int16      | 16-bit integer                                  |
| int32      | 32-bit integer                                  |
| int64      | 64-bit integer                                  |
| uint8      | Unsigned 8-bit integer                          |
| uint16     | Unsigned 16-bit integer                         |
| uint32     | Unsigned 32-bit integer                         |
| uint64     | Unsigned 64-bit integer                         |
| float\_    | Floating point number                           |
| float16    | Half precision floating point number            |
| float32    | Single precision floating point number          |
| float64    | Double precision floating point number          |
| complex\_  | Complex number                                  |
| complex64  | Complex number represented by two 32-bit floats |
| complex128 | Complex number represented by two 64-bit floats |
| bool\_     | Boolean                                         |
| object\_   | Object (can hold any Python object)             |

To specify a data type for an array, we can use the dtype parameter.

```python
# Creating an array with a specific data type
my_array = np.array([1, 2, 3], dtype=np.float64)
print(my_array)  # Output: [1. 2. 3.]
```

We can also convert an array to a different data type using the `astype()` method.

```python
# Converting an array to a different data type
my_array = np.array([1, 2, 3], dtype=np.int32)
my_array = my_array.astype(np.float64)
print(my_array)  # Output: [1. 2. 3.]
```
