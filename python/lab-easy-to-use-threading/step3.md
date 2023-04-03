# Thread with Arguments

In Python, you can pass arguments to threads by either using the `args` parameter when creating a new thread or by subclassing the Thread class and defining your constructor that accepts arguments. Here are examples of both approaches:

1; We create a subclass of the `Thread` class and override the `run` method to define the thread's behavior. Create a Project called `thread_subclass.py` in the WebIDE and enter the following content.

```python
import threading

# Define a custom Thread class that extends the Thread class
class MyThread(threading.Thread):
    # Override the run() method to implement thread's behavior
    def run(self):
        print("Hello from thread")

# Create an instance of the custom thread class
thread = MyThread()

# Start the thread
thread.start()

# Wait for the thread to finish execution
thread.join()
```

Use the following command to run the script.

```bash
python thread_subclass.py
```

2; We create a thread and pass arguments to the target function using the `args` parameter. Create a Project called `thread_with_args.py` in the WebIDE and enter the following content

```python
import threading

# Define a function that takes a parameter
def my_function(name):
    print("Hello from", name)

# Create a new thread with target function and arguments
thread = threading.Thread(target=my_function, args=("Thread 1",))

# Start the thread
thread.start()

# Wait for the thread to finish execution
thread.join()
```

Use the following command to run the script.

```bash
python thread_with_args.py
```
