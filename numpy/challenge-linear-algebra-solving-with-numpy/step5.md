# Eigenvector and Eigenvalue Calculation

## TODO

Write a Python function `eigenvector_eigenvalue(matrix)` in `eigenvector_eigenvalue.py` that takes a NumPy matrix as input and calculates its eigenvectors and eigenvalues. The function should return two NumPy arrays: one containing the eigenvectors and another containing the corresponding eigenvalues.

- The `numpy.linalg.eig(matrix)` is used to calculates the eigenvectors and eigenvalues of matrix.

## Example Input

```python
import numpy as np

A = np.array([[1, 2],
              [2, 1]])

print("eigenvectors and eigenvalues:\n", eigenvector_eigenvalue(A))
```

## Example Output

```lua
eigenvectors and eigenvalues:
(array([[ 0.70710678, -0.70710678],
        [ 0.70710678,  0.70710678]]), array([ 3., -1.]))
```
