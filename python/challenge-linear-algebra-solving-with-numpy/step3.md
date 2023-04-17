# Determinant Calculation

## TODO

Write a Python function `determinant_matrix(matrix)` in `determinant_matrix.py` that takes a NumPy matrix as input and calculates its determinant. The function should return the determinant value as a float.

- The `numpy.linalg.det(matrix)` function is used to calculate the determinant of a NumPy `matrix` and it returns the determinant value as a float.

## Example Input

```python
import numpy as np

A = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])

B = np.array([[1, 2],
              [3, 4]])

print("determinant_A:\n", determinant_matrix(A))

print("determinant_B:\n", determinant_matrix(B))
```

## Example Output

```lua
determinant_A:
-0.0
determinant_B:
-2.0
```
