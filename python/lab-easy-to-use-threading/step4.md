# Thread Pool

In Python, you can use a thread pool to execute tasks concurrently using a predefined set of threads. The benefit of using a thread pool is that it avoids the overhead of creating and destroying threads for each task, which can improve performance.

Python's `concurrent.futures` module provides a ThreadPoolExecutor class that allows you to create a pool of threads and submit tasks. Here's an example:

Create a Project called `thread_pool_range.py` in the WebIDE and enter the following content.

```python
import concurrent.futures

# Define a function to be executed in multiple threads with two arguments
def my_func(arg1, arg2):
    # Define the tasks performed by the thread here
    print(f"Hello from my thread with args {arg1} and {arg2}")

# Create a ThreadPoolExecutor object with a maximum of 5 worker threads
with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
    # Submit each task (function call with its arguments) to the executor for processing in a separate thread
    # The submit() method returns a Future object representing the result of the asynchronous computation
    for i in range(10):
        executor.submit(my_func, i, i+1)
```

In this example, we define a function `my_func` that takes two arguments. We create a ThreadPoolExecutor with a maximum of 5 worker threads. Then, we loop through a range of numbers and submit tasks to the thread pool using the `executor.submit()` method. Each submitted task is executed on one of the available worker threads.

> Tips: The `ThreadPoolExecutor` object is used as a context manager. This ensures that all threads are properly cleaned up when the code inside the with block is completed.

Use the following command to run the script.

```bash
python thread_pool_range.py
```

The `submit()` method returns a Future object immediately, representing the submitted task's result. You can use the `result()` method of the Future object to retrieve the task's return value. If the task raises an exception, calling `result()` will raise that exception.

You can also use the `map()` method of the ThreadPoolExecutor class to apply the same function to a collection of items. For example, Create a Project called `thread_pool_map.py` in the WebIDE and enter the following content.:

```python
import concurrent.futures

# Define a function to be executed in multiple threads
def my_func(item):
    # Define the tasks performed by the thread here
    print(f"Hello from my thread with arg {item}")

# Create a list of items to be processed by the threads
items = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Create a ThreadPoolExecutor object with a maximum of 5 worker threads
with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
    # Submit each item to the executor for processing in a separate thread
    # The map() method automatically returns the results in order
    executor.map(my_func, items)
```

In this example, we define a function `my_func` that takes one argument. We create a list of items and submit them to the thread pool using the `executor.map()` method. Each item in the list is passed to my_func as an argument, and each item is executed on one of the available worker threads.

Use the following command to run the script.

```bash
python thread_pool_map2.py
```

The results obtained from `thread_pool_range.py` and `thread_pool_map.py` are the same.
