# Basic Einsum Examples

Let's look at some basic examples to get a better understanding of how `einsum` works.

## Dot product

Suppose we have two vectors $u$ and $v$, and we want to compute their dot product:

$$
a = \sum_i u_i v_i
$$

We can use `einsum` to perform this operation as follows:

```python
# generate two random matrixs
u = np.random.rand(3)
v = np.random.rand(3)

# compute dot product
np.einsum('i,i->', u, v)
```

Here, the string `'i,i->'` tells einsum to perform the dot product and return a scalar value.

This is equivalent to use `np.dot` function:

```python
np.dot(u, v)
```

## Transpose

Suppose we have a matrix $A$, and we want to compute its transpose:

$$
B_{ij} = A_{ji}
$$

We can use einsum to perform this operation as follows:

```python
# generate a random matrix
A = np.random.rand(3, 4)

# transpose the matrix
np.einsum('ji->ij', A)
```

Here, the string `'ji->ij'` tells `einsum` to transpose the matrix $A$ and return the resulting matrix.

This is equivalent to use `np.transpose` function:

```python
np.transpose(A)
```

## Matrix Multiplication

Suppose we have two matrices $A$ and $B$, and we want to compute their product:

$$
C_{ij} = \sum_k A_{ik}B_{kj}
$$

We can use einsum to perform this operation as follows:

```python
# generate two random matrixs
A = np.random.rand(3, 4)
B = np.random.rand(4, 5)

# compute product
np.einsum('ik,kj->ij', A, B)
```

Here, the string `'ik,kj->ij'` tells einsum to perform the matrix multiplication and return the resulting matrix with dimensions $(i,j)$.

This is equivalent to use `np.matmul` function:

```python
np.matmul(A, B)
```

## Broadcasting

Suppose we have a matrix $A$ and a vector $u$, and we want to compute the product:

$$
B_{ij} = A_{ij}u_j
$$

We can use `einsum` to perform this operation as follows:

```python
# generate two random matrixs
A = np.random.rand(3, 4)
u = np.random.rand(4)

np.einsum('ij,j->ij', A, u)
```

Here, the string `'ij,j->ij'` tells `einsum` to perform the element-wise multiplication between $A$ and $u$, and return the resulting matrix.

This is equivalent to use `np.multiply` function:

```python
np.multiply(A, u)
```
