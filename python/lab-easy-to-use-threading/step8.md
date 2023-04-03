# Barrier Object

In Python, you can use `threading.Barrier` object to synchronize multiple threads at predefined synchronization points. The Barrier object provides a way for a set of threads to wait for each other to reach a certain point in their execution before continuing.

Create a Project called `barrier_object.py` in the WebIDE and enter the following content.

```python
import threading

# Create a Barrier object for 3 threads
barrier = threading.Barrier(3)

# Define a function that waits at the barrier
def my_function():
    print("Before barrier")
    # Wait for all three threads to reach the barrier
    barrier.wait()
    print("After barrier")

# Create 3 threads using a loop and start them
threads = []
for i in range(3):
    thread = threading.Thread(target=my_function)
    threads.append(thread)
    thread.start()

# Wait for all threads to finish executing
for thread in threads:
    thread.join()

```

In this example, we create a `Barrier` object using the `Barrier` class and pass it the number of threads to wait for. Using the wait method, we define a function that waits for the barrier and prints a message. We create three threads and start them. Each thread waits for the barrier, so all threads will wait until all of them have reached the barrier. Finally, we wait for all threads to finish using the `join` method.

Then use the following command to run the script.

```bash
python barrier_object.py
```
