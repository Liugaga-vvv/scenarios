# Daemon Threads

In Python, a daemon thread is a type of thread that runs in the background and does not prevent the program from exiting. When all non-daemon threads have been completed, the Python interpreter exits, regardless of whether any daemon threads are still running.

Create a Project called `daemon_thread_with_args.py` in the WebIDE and enter the following content.

```python
import threading
import time

# Define a function that runs indefinitely and prints messages at a regular interval
def my_function():
    while True:
        print("Hello from thread")
        time.sleep(1)

# Create a daemon thread that runs the target function
thread = threading.Thread(target=my_function, daemon=True)

# Start the thread
thread.start()

# The main program continues to execute and prints a message
print("Main program")

# Wait for a few seconds before exiting the program
time.sleep(5)

# The program exits, and the daemon thread is terminated automatically
print("Main thread exiting...")

```

In this example, we create a thread that runs an infinite loop and prints a message every second using `time.sleep()` function. We mark the thread as a daemon using the `daemon` parameter to exit when the main program exits automatically. The main program continues to run and prints a message. We wait a few seconds, and the program exits, terminating the daemon thread.

Then use the following command to run the script.

```bash
python daemon_thread_with_args.py
```

Of course, we can also set a thread as a daemon by calling the `setDaemon(True)` method on the thread instance. For example, Create a Project called `daemon_thread_with_func.py` in the WebIDE and enter the following content:

```python
import threading
import time

# Define a function that runs indefinitely and prints messages at a regular interval
def my_function():
    while True:
        print("Hello from thread")
        time.sleep(1)

# Create a new thread with target function
thread = threading.Thread(target=my_function)

# Set the daemon flag to True so that the thread runs in the background and terminates when the main program exits
thread.setDaemon(True)

# Start the thread
thread.start()

# The main program continues to run and prints a message
print("Main program")

# Wait for a few seconds before exiting the program
time.sleep(5)

# The program exits and the daemon thread is terminated automatically
print("Main thread exiting...")
```

Executing the script with the following command will achieve the same result as the above example.

```bash
python daemon_thread_with_func.py
```
