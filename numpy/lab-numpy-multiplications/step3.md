# numpy.dot

The `numpy.dot` function performs matrix multiplication between two arrays. The first array must have the same number of columns as the second array has rows. The resulting array will have the same number of rows as the first array and the same number of columns as the second array.

```python
C = np.dot(A, B)

print(C)
# Output:
# array([[19, 22],
#        [43, 50]])
```

In this example, we have performed matrix multiplication between arrays `A` and `B`. The resulting array `C` has two rows and two columns, as expected.
