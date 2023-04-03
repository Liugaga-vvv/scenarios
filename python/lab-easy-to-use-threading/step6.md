# Event Object

In Python, you can use `threading.Event` object to allow threads to wait for a specific event to occur before proceeding. The Event object provides a way for one thread to signal that an event has occurred, and other threads can wait for that signal.

Create a Project called `event_object.py` in the WebIDE and enter the following content.

```python
import threading

# Create an event object
event = threading.Event()

# Define a function that waits for the event to be set
def my_function():
    print("Waiting for event")
    # Wait for the event to be set
    event.wait()
    print("Event received")

# Create a new thread with target function
thread = threading.Thread(target=my_function)

# Start the thread
thread.start()

# Signal the event after a few seconds
# The wait() call in the target function will now return and continue execution
event.set()

# Wait for the thread to finish executing
thread.join()

```

In this example, we create an `Event` object using the `Event` class. We define a function that waits for the event to be signaled using the `wait` method and then prints a message. We create a new thread and start it. After a few seconds, we signal the event using the `set` method. The thread receives the event and prints a message. Finally, we wait for the thread to finish using the `join` method.

Then use the following command to run the script.

```bash
python event_object.py
```
