# Generating a Random Graph

In this sub-challenge, you will write a Python program that generates a random graph using NumPy. You will use NumPy to generate random numbers and manipulate NumPy arrays to create the graph.

## TODOs

1. Import the NumPy library.
2. Generate a NumPy array representing the adjacency matrix of the graph, where each element is 1 with probability $p$ and 0 with probability $1-p$.
3. Ensure that the matrix is symmetric.
4. Return the adjacency matrix.
5. Completing `generate_graph.py`

## Example Output

Suppose the probability of an edge between two nodes is 0.3 and the graph has 4 nodes. The output of the program could be the following adjacency matrix:

```lua
[[0. 1. 0. 1.]
 [1. 0. 0. 1.]
 [0. 0. 0. 0.]
 [1. 1. 0. 0.]]
```
