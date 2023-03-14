# Broadcasting

Broadcasting is a feature of NumPy that allows for element-wise operations between arrays with different shapes. Broadcasting is especially useful when working with arrays of different dimensions.

Let's create an array and perform some broadcasting operations:

```python
# Creating two arrays of different shapes
array1 = np.array([1, 2, 3])
array2 = np.array([[4, 5, 6], [7, 8, 9]])

# Broadcasting the smaller array to the larger array
print("Adding two arrays using broadcasting: ", array1 + array2)

print("Subtracting two arrays using broadcasting: ", array1 - array2)

print("Multiplying two arrays using broadcasting: ", array1 * array2)

print("Dividing two arrays using broadcasting: ", array1 / array2)
```

Output:

```python
Adding two arrays using broadcasting:  [[ 5  7  9]
                                         [ 8 10 12]]

Subtracting two arrays using broadcasting:  [[-3 -3 -3]
                                              [-6 -6 -6]]

Multiplying two arrays using broadcasting:  [[ 4 10 18]
                                              [7 16 27]]

Dividing two arrays using broadcasting:  [[0.25       0.4        0.5       ]
                                           [0.14285714 0.25       0.33333333]]
```

In the above code, we create two arrays, `array1` with the shape (3,) and `array2` with the shape (2,3). We perform element-wise operations between `array1` and `array2`, thanks to the broadcasting feature in NumPy. The smaller array, `array1`, is broadcasted to the larger array, `array2`, to perform element-wise operations. Broadcasting makes it possible to perform operations on arrays with different shapes.
