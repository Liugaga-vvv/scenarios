# Inter-Process Communication

In this programming challenge, you will be using Python multiprocessing to create a shared queue between processes.

Your solution should include:

Your program should use the `multiprocessing.Queue()` function to create a shared queue and the `multiprocessing.Process()` class to run two processes that each call the `producer()` and `consumer()` functions.

## Examples

Your program should output the numbers 0 to 9 in the order that they were added to the queue.

## TODO

- Completing `multiprocessing_queue.py`

## Requirements

- The two processes are started using the `start()` function, and then we use the `join()` function to wait for the `producer()` process to finish.
- You need to create two processes. Each process calls the functions `product()` and `consumer()`.
