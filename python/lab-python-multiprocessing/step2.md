# Using Multiprocessing to Speed Up Processing

Now that you understand how multiprocessing works in Python, we can move on to a more complex example. In this example, we will use multiprocessing to speed up the processing of a large list of numbers.

Please complete `complex_square.py`.

```python
import multiprocessing

def square(x):
    return x * x

if __name__ == '__main__':
    with multiprocessing.Pool(processes=4) as pool:
        results = pool.map(square, range(1000000))
    print(results[:10])
```

This code creates a pool of four processes and uses the `map()` function to apply the `square()` function to each of the numbers in the range from 0 to 999999. The `with` statement is used to ensure that the pool of processes is properly closed when the processing is complete. The first ten results are then printed to the console.
