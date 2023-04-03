# Timer Object

In Python, you can use `threading.Timer` object to schedule a function to run after a specific time has passed. The Timer object creates a new thread that waits for the specified time interval before executing the function.

Create a Project called `timer_object.py` in the WebIDE and enter the following content.

```python
import threading

# Define a function to be executed by the Timer after 5 seconds
def my_function():
    print("Hello from timer")

# Create a timer that runs the target function after 5 seconds
timer = threading.Timer(5, my_function)

# Start the timer
timer.start()

# Wait for the timer to finish
timer.join()

```

In this example, we create a `Timer` object using the `Timer` class and pass it a time delay in seconds and a function to execute. We start the timer using the `start` method and wait for it to finish using the `join` method. After 5 seconds, the function is executed and prints a message.

Then use the following command to run the script.

```bash
python timer_object.py
```

> Tips: The timer thread runs separately, so it may not be synchronized with the main thread. If your function relies on some shared state or resources, you will need to synchronize access to them appropriately. Also, remember that the timer thread will not stop the program from exiting if it is still running when all other non-daemon threads have been completed.
