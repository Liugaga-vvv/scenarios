# Asynchronous Tasks with Pool.apply_async()

In addition to `map()`, the `multiprocessing.Pool()` class provides another method for running processes in parallel called `apply_async()`. This method allows you to submit a function call to a pool of processes and immediately continue execution without waiting for the result. Instead, you can use a callback function to retrieve the result of the function call when it is ready.

Please complete`slow_square.py`.

```python
import multiprocessing
import time

def slow_square(x):
    time.sleep(1)
    return x * x

def callback(result):
    print(result)

if __name__ == '__main__':
    pool = multiprocessing.Pool(processes=4)
    results = [pool.apply_async(slow_square, (x,), callback=callback) for x in range(10)]
    for result in results:
        result.wait()
    print("All tasks completed.")
```

In this example, we define a function `slow_square()` that takes a number $x$, waits for one second, and then returns the square of $x$. We also define a callback function `callback()` that simply prints the result when it is available.

We then create a pool of four processes and use `apply_async()` to submit a function call to the pool for each number in the range from 0 to 9. We pass in the `slow_square()` function and the argument $x$ using the $args$ parameter, and also specify the callback function to be called when the result is ready.

We then loop through the list of results and call `result.wait()` to block the main thread until the result is ready. Finally, we print a message to indicate that all tasks are completed.
