# Universal Functions

Universal functions, or ufuncs, are functions that operate on arrays in an element-wise fashion. They provide fast and efficient operations on arrays.

Let's create an array and perform some ufuncs:

```python
# Creating an array
arr = np.array([1, 2, 3, 4])

# Finding the square root of each element in the array
print("Square root of array: ", np.sqrt(arr))

# Finding the exponential of each element in the array
print("Exponential of array: ", np.exp(arr))

# Finding the sine of each element in the array
print("Sine of array: ", np.sin(arr))

# Finding the cosine of each element in the array
print("Cosine of array: ", np.cos(arr))

# Finding the natural logarithm of each element in the array
print("Natural logarithm of array: ", np.log(arr))
```

Output:

```python
Square root of array:  [1.         1.41421356 1.73205081 2.        ]
Exponential of array:  [ 2.71828183  7.3890561  20.08553692 54.59815003]
Sine of array:  [ 0.84147098  0.90929743  0.14112001 -0.7568025 ]
Cosine of array:  [ 0.54030231 -0.41614684 -0.9899925  -0.65364362]
Natural logarithm of array:  [0.         0.69314718 1.09861229 1.38629436]
```
