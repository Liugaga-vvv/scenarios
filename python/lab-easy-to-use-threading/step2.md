# Synchronization

If multiple threads access the same shared resource (e.g., a variable or file), we must synchronize access to that resource to avoid race conditions. Python's threading module provides a `Lock` class for this purpose.

Here's an example of using a `Lock` to create a Project called `sync.py` in the WebIDE and enter the following content.

```python
import threading

# Create a lock to protect access to shared resource
lock = threading.Lock()

# Shared resource that will be modified by multiple threads
counter = 0

# Define a function that each thread will run
def my_function():
    global counter

    # Acquire the lock before accessing the shared resource
    lock.acquire()
    try:
        # Access the shared resource
        counter += 1
    finally:
        # Release the lock after modifying the shared resource
        lock.release()

# Create multiple threads to access the shared resource
threads = []

# Create and start 10 threads that execute the same function
for i in range(10):
    thread = threading.Thread(target=my_function)
    threads.append(thread)
    thread.start()

# Wait for all threads to complete their execution
for thread in threads:
    thread.join()

# Print the final value of the counter
print(counter) # Output: 10
```

We create a `Lock` object and a shared resource `counter` in this example. The `my_function` function accesses the shared resource by acquiring the lock using the `acquire` method and releasing the lock using the `release` method. We create multiple threads and start them, then wait for them to finish using the `join` method. Finally, we print the final value of the counter.

Use the following command to run the script.

```bash
python sync.py
```
