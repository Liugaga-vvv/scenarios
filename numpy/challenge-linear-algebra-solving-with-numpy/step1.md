# Matrix Inversion

Write a Python function `invert_matrix(matrix)` in `invert_matrix.py` that takes a NumPy matrix as input and returns the inverse of the matrix. If the input matrix is not invertible, the function should raise a `ValueError` with an appropriate error message.

- `numpy.linalg.det(matrix)` function calculates the determinant of the input `matrix`.
- If the determinant value of the matrix is zero, the `matrix` is not invertible, the function should raise a `ValueError` with an appropriate error message, e.g."Matrix is not invertible".
- If the determinant value of the matrix is not zero, the `numpy.linalg.inv(matrix)` fuction is used to return the inverse of the matrix.

## Example Input

```python
import numpy as np

A = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])

B = np.array([[1, 0, 0],
              [0, 2, 0],
              [0, 0, 3]])

C = np.array([[1, 2],
              [3, 4]])

D = np.array([[1, 2],
              [2, 4]])

print("invert_A:\n", invert_matrix(A))
print("invert_B:\n", invert_matrix(B))
print("invert_C:\n", invert_matrix(C))
print("invert_D:\n", invert_matrix(D))
```

## Example Output

```lua
invert_A:
[[-0.5         1.         -0.5       ]
 [ 1.         -2.          1.        ]
 [-0.5         1.         -0.5       ]]
invert_B:
[[1.         0.         0.        ]
 [0.         0.5        0.        ]
 [0.         0.         0.33333333]]
invert_C:
[[-2.   1. ]
 [ 1.5  -0.5]]
invert_D:
ValueError: Matrix is not invertible
```
