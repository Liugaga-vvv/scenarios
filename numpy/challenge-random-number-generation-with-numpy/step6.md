# Generating a Random Graph

In this sub-challenge, you will write a Python program that generates a random graph using NumPy. You will use NumPy to generate random numbers and manipulate NumPy arrays to create the graph.

## TODOs

1. Completing `generate_graph.py`
2. Import the NumPy library.
3. Generate a NumPy array representing the adjacency matrix of the graph, where each element is 1 with probability $p$ and 0 with probability $1-p$.
4. Ensure that the matrix is symmetric.
5. Return the adjacency matrix.

## Example Output

Suppose the probability of an edge between two nodes is 0.3 and the graph has 4 nodes. The output of the program could be the following adjacency matrix:

```lua
[[0. 1. 0. 1.]
 [1. 0. 0. 1.]
 [0. 0. 0. 0.]
 [1. 1. 0. 0.]]
```
