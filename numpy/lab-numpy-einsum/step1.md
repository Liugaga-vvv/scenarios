# Einsum Introduction

`einsum` is a powerful tool for performing various array operations in NumPy. It is a concise way of expressing complex array operations using a string notation. The string notation is based on the Einstein summation convention, which uses indices to denote which dimensions of arrays are being operated on. The indices are represented by letters or characters, and the operations are denoted by the characters that appear between the indices.

## Open the Python Shell

Open the Python shell by typing the following command in the terminal.

```bash
python3
```

## First Example

For example, let's consider a simple operation of multiplying two matrices $A$ and $B$:

$$
C_{ij} = \sum_k A_{ik}B_{kj}
$$

Here, we sum over the index $k$, and the resulting matrix $C$ has dimensions $(i,j)$. Using `einsum`, we can express this operation as follows:

```python
import numpy as np

# generate two random matrixs
A = np.random.rand(3, 4)
B = np.random.rand(4, 5)

# multiplying two matrices
C = np.einsum('ik,kj->ij', A, B)
```

The first argument to `einsum` is the string notation that describes the operation. In this case, we use the string `'ik,kj->ij'`, which tells `einsum` to perform the matrix multiplication and return the resulting matrix $C$ with dimensions $(i,j)$.

## Anatomy of an Einsum String

The `einsum` string notation has the following general format:

```python
output = np.einsum('input1_label1input1_label2, input2_label1input2_label2 -> output_label1output_label2', input1, input2)
```

- `input1_label1input1_label2` and `input2_label1input2_label2`: These are the input tensor labels followed by their corresponding index labels. The index labels are separated by a comma. For example, `ij` would represent the indices `i` and `j` of the first input tensor.
- `output_label1output_label2`: This is the label and index specification for the output tensor. For example, `ik` would represent the indices `i` and `k` of the output tensor.
- `input1` and `input2`: These are the input tensors.

The notation allows for very flexible and concise specification of tensor operations, making it a powerful tool for scientific computing.
