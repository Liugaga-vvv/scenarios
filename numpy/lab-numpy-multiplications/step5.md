# \* operator

The `*` operator also performs element-wise multiplication between two arrays, but it behaves slightly differently than `numpy.multiply`. If the two arrays have the same shape, the `*` operator will perform element-wise multiplication, just like `numpy.multiply`. However, if one of the arrays is a scalar value, the `*` operator will perform scalar multiplication on every element of the other array.

```python
C = A * B
D = A * 2

print(C)
# Output:
#array([[ 5, 12],
#       [21, 32]])

print(D)
# Output:
# array([[2, 4],
#       [6, 8]])
```

In the first example, we get the same result as with `numpy.multiply`. In the second example, we perform scalar multiplication on every element of array `A`.
