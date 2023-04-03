# Inter-Process Communication

In some cases, you may need to communicate between processes when using multiprocessing in Python. In this example, we will use the `multiprocessing.Queue()` function to create a shared queue between processes.

Please complete `multiprocessing_queue.py`.

```python
import multiprocessing

def producer(queue):
    for i in range(10):
        queue.put(i)

def consumer(queue):
    while True:
        item = queue.get()
        if item is None:
            break
        print(item)

if __name__ == '__main__':
    queue = multiprocessing.Queue()
    process_producer = multiprocessing.Process(target=producer, args=(queue,))
    process_consumer = multiprocessing.Process(target=consumer, args=(queue,))
    process_producer.start()
    process_consumer.start()
    process_producer.join()
    queue.put(None)
    process_consumer.join()
```

This code creates a shared queue `queue` using the `multiprocessing.Queue()` function. We then create two processes that each call a function `producer()` and `consumer()`. The `producer()` function puts the numbers 0 to 9 into the queue, while the `consumer()` function gets each item from the queue and prints it to the console.
