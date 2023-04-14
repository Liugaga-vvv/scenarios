# Creating a Simple Multiprocessing Program

The first step in learning about multiprocessing in Python is to create a simple program that demonstrates how it works. In this program, we will create a function that takes a single argument and returns the square of that number. We will then use multiprocessing to run this function on multiple processes.

Please complete `square.py`.

```python
import multiprocessing

def square(x):
    return x * x

if __name__ == '__main__':
    pool = multiprocessing.Pool(processes=4)
    results = pool.map(square, range(10))
    print(results)
```

This code creates a pool of four processes and uses the `map()` function to apply the `square()` function to each of the numbers in the range from 0 to 9. The results are then printed to the console.
