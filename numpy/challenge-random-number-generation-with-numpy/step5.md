# Sampling from a Multinomial Distribution

In this sub-challenge, you will write a Python program that generates a random sample from a multinomial distribution using NumPy. You will use NumPy to generate random numbers and manipulate NumPy arrays to sample from the distribution.

## TODOs

1. Import the NumPy library.
2. Create a NumPy array representing the probability distribution, where each element represents the probability of a specific outcome.
3. Sample from the multinomial distribution by randomly selecting $n$ elements from the array, where $n$ is the number of trials, with a probability proportional to their values.
4. Return the counts of each selected element.
5. Completing `sample_multinomial.py`

## Example Output

Suppose the probability distribution is $[0.2, 0.3, 0.5]$ and the number of trials is 10. The output of the program could be any of the following, depending on the randomly selected elements:

```csharp
[2 2 6]
[4 2 4]
[1 4 5]
```
