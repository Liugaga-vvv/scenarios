# @ operator

The `@` operator performs matrix multiplication, just like `numpy.dot` and `numpy.matmul`. It was introduced in Python 3.5 as a shorthand for `numpy.matmul`.

```python
C = A @ B

print(C)
# Output:
# array([[19, 22],
#       [43, 50]])
```

In this example, we use the `@` operator to perform matrix multiplication between arrays `A` and `B`. The resulting array `C` has two rows and two columns, just like with `numpy.dot` and `numpy.matmul`.
