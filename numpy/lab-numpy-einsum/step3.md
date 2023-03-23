# Advanced Einsum Examples

Now that we have covered the basics of `einsum`, let's look at some more advanced examples.

## Tensor Contraction

Suppose we have a 4th-order tensor $T$ with dimensions $(i,j,k,l)$, and we want to contract it along the last two dimensions to obtain a 2nd-order tensor $S$ with dimensions $(i,j)$:

$$
S_{ij} = \sum_{k,l} T_{ijkl}
$$

We can use `einsum` to perform this operation as follows:

```python
# generate a 4th-order tensor
T = np.random.rand(3, 4, 5, 6)

# contract
np.einsum('ijkl->ij', T)
```

Here, the string `'ijkl->ij'` tells `einsum` to contract the tensor $T$ along the last two dimensions and return the resulting matrix.

This is equivalent to use `np.sum` function:

```python
np.sum(T, axis=(2, 3))
```

## Batch Matrix Multiplications

Suppose we have a batch of $n$ matrices $A_1, ..., A_n$ with dimensions $(m, p)$ and a batch of $n$ matrices $B_1, ..., B_n$ with dimensions $(p, q)$, and we want to compute their batch product $C_1, ..., C_n$ with dimensions $(m, q)$:

$$
C_i = A_iB_i
$$

We can use `einsum` to perform this operation as follows:

```python
n = 5
m = 3
p = 4
q = 5

# generate two matrixs
A = np.random.rand(n, m, p)
B = np.random.rand(n, p, q)

# compute batch matrix multiplication
np.einsum('nmp,npq->nmq', A, B)
```

Here, the string `'nmp,npq->nmq'` tells `einsum` to perform the batch matrix multiplication and return the resulting batch of matrices.

This is equivalent to use `np.matmul` function:

```python
np.matmul(A, B)
```
