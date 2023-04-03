# Object Destruction

In this section, we will explore the object destruction magic method in Python. The method allows you to define custom behavior when an object is about to be destroyed.

## \_\_del\_\_

The `__del__` method is called when an object is about to be destroyed. It allows you to perform clean-up tasks, such as closing file handles or releasing resources, before the object is garbage collected.

```python
    # ... (previous code in person.py)

    def __del__(self):
        """
        Clean up the Person object before it is destroyed.
        """
        print(f"Person '{self.name}' is being deleted.")
```

## Example: Using the Object Destruction Magic Method

Now that we have defined the object destruction magic method for our `Person` class, let's see how it works in `del_example.py`:

```python
from person import Person

# Create a Person object and then delete it
p = Person("Alice", 30)
del p  # Output: Person 'Alice' is being deleted.
```

Then typing the following command in the terminal to execute the script.

```bash
python del_example.py
```

It's important to note that the `__del__` method is not guaranteed to be called immediately when an object is no longer needed. The actual deletion of the object depends on the Python interpreter's garbage collection mechanism. The `__del__` method is called when the garbage collector decides to remove the object from memory.
