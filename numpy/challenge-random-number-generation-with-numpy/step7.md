# Generating a Random Markov Chain

In this sub-challenge, you will write a Python program that generates a random Markov chain using NumPy. You will use NumPy to generate random numbers and manipulate NumPy arrays to create the chain.

## TODOs

1. Import the NumPy library.
2. Generate a NumPy array representing the transition matrix of the Markov chain, where each element is a probability between 0 and 1.
3. Normalize each row of the matrix by dividing each element by the sum of its row.
4. Generate a random initial state vector, where each element is a probability between 0 and 1 and the sum of all elements is 1.
5. Return the transition matrix and initial state vector.
6. Completing `generate_markov_chain.py`

## Example Output

Suppose the transition matrix of the Markov chain is:

```lua
[[0.4 0.6 0.0]
 [0.2 0.5 0.3]
 [0.0 0.7 0.3]]
```

and the initial state vector is $[0.1, 0.2, 0.7]$. The output of the program could be:

```lua
(array([[0.4, 0.6, 0. ],
        [0.2, 0.5, 0.3],
        [0. , 0.7, 0.3]]),
 array([0.1, 0.2, 0.7]))
```
