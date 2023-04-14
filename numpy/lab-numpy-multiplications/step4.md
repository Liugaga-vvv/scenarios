# numpy.matmul

The `numpy.matmul` function also performs matrix multiplication between two arrays, but it has slightly different rules for handling multidimensional arrays. The two arrays must have the same shape, except for the last two dimensions, which must conform. If either array is 1-D, it is promoted to a matrix by appending a 1 to its shape.

```python
C = np.matmul(A, B)

print(C)
# Output:
# array([[19, 22],
#        [43, 50]])
```

In this example, we get the same result as with `numpy.dot`. This is because our arrays `A` and `B` have the same shape, so `numpy.matmul` behaves the same way as `numpy.dot`.

And there is another different example:

```python
# define two 3-D arrays
a = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
b = np.array([[[9, 10], [11, 12]], [[13, 14], [15, 16]]])

c = np.matmul(a, b)
d = np.dot(a, b)

print(c)
# Output:
# array([[[ 31,  34],
#        [ 71,  78]],
#        [[155, 166],
#        [211, 226]]])

print(d)
# Output:
# array([[[[ 31,  34],
#         [ 43,  46]],
#        [[ 71,  78],
#         [ 99, 106]]],
#       [[[111, 122],
#         [155, 166]],
#        [[151, 166],
#         [211, 226]]]])
```

In this example, `numpy.matmul` performs the batch matrix multiplication operation.

Since both `a` and `b` are 3-D arrays, the output of `numpy.dot` will have dimensionality $(2,2,2,2)$. The first two dimensions correspond to the two batches of $2\times2$ matrices in `a` and `b`. The next two dimensions correspond to the dot product of each pair of $2\times2$ matrices in the batches:

```python
# the first 2 × 2 result
dot(a[0], b[0]) =
dot([[1, 2],
 [3, 4]],
 [[9, 10],
 [11, 12]]
= [[1*9 + 2*11, 1*10 + 2*12],
   [3*9 + 4*11, 3*10 + 4*12]]
= [[31, 34],
   [43, 46]]
```
