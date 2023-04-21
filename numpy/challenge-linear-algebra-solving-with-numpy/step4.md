# Linear Equation Solver

## TODO

Write a Python function `solve_linear_equation(A, b)` in `solve_linear_equation.py` that takes two NumPy matrices A and b as input and solves the linear equation Ax = b using matrix inversion. The function should return the solution x as a NumPy array. If the matrix A is not invertible or the dimensions of A and b do not match, the function should raise a `ValueError` with an appropriate error message.

- If `A.shape[0]` is not equal to `A.shape[1]` or `A.shape[0]` is not equal to `b.shape[0]`, the dimensions of matrix A and matrix b do not match, the function should raise a `ValueError` with an appropriate error message.
- The `invert_matrix(matrix)` function in step1 returns the inverse of the `matrix`, here the `matrix` should be `matrix A`.
- The `numpy.matmul(matrix1,matrix2)` funtion returns the product of two matrices A and b, which is the solution to the linear equation Ax = b. Here matrix1 should be `inv_A` and matrix2 should be `b`.

## Example Input

```python
import numpy as np

A = np.array([[1, 2],
              [3, 4]])

b = np.array([5, 6])

print("x:\n", solve_linear_equation(A, b))
```

## Example Output

```lua
x:
[-4. 4.5]
```
