# Singular Value Decomposition

Write a Python function `svd_matrix(matrix)` in `svd_matrix.py` that takes a NumPy matrix as input and performs Singular Value Decomposition (SVD) on the matrix. The function should return three matrices: $U$, $S$, and $V$.

- The`numpy.linalg.svd(matrix)` funtion is used to perform Singular Value Decomposition (SVD) on the `matrix`, which returns three matrices: $U$, $S$, and $V$.

## Example Input

```python
import numpy as np

A = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])

U, S, V = svd_matrix(A)

print("U:\n", U)
print("S:\n", S)
print("V:\n", V)
```

## Example Output

```lua
U:
 [[-0.21483724 -0.88723069  0.40824829]
 [-0.52058739 -0.24964395 -0.81649658]
 [-0.82633754  0.38794278  0.40824829]]
S:
 [1.68481034e+01 1.06836951e+00 3.33475287e-16]
V:
 [[-0.47967117 -0.57236779 -0.66506441]
 [-0.77669099 -0.07568653  0.62531793]
 [-0.40824829  0.81649658 -0.40824829]]
```
