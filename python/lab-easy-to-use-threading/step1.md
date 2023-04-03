# Creating Threads

To create a new thread in Python, we need to create a new instance of the `Thread` class and pass it a function to execute.

Create a Project called `create_thread.py` in the WebIDE and enter the following content.

```python
import threading

# Define a function to run in the thread
def my_function():
    print("Hello from thread")

# Create a new thread
thread = threading.Thread(target=my_function)

# Start the thread
thread.start()

# Wait for the thread to finish
thread.join()

# Print "Done" to indicate that the program has finished
print("Done")
```

This example defines a function `my_function` that prints a message. We then create a new instance of the `Thread` class, passing it `my_function` as the target function. Finally, we start the thread using the `start` method and wait for it to finish using the `join` method.

Use the following command to run the script.

```bash
python create_thread.py
```
