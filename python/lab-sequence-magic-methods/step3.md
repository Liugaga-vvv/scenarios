# Iteration

Iteration methods are special methods in Python that allow objects to define their behavior when used with iteration protocols.

## \_\_iter\_\_

The `__iter__` magic method is used to define the behavior of the `iter()` function and the `for ... in ...` loop when applied to instances of your class.

```python
    # ... (previous code in sequence.py)

    def __iter__(self):
        """Return an iterator for the sequence."""
        for item in self.data:
            yield item
```

## \_\_reversed\_\_

The `__reversed__` magic method is used to define the behavior of the `reversed()` function when applied to instances of your class.

```python
    # ... (previous code in sequence.py)

    def __reversed__(self):
        """Return a reversed iterator for the sequence."""
        return reversed(self.data)
```

## Example: Using the Iteration Methods

Now that we have defined the iteration methods for our `MySequence` class, let's see how they work in `iteration_example.py`:

```python
from sequence import MySequence

# Create a MySequence object
my_seq = MySequence([1, 2, 3, 4, 5])

# Test the __iter__ magic method
for item in my_seq:
    print(item, end=" ")  # Output: 1 2 4 5

# Test the __reversed__ magic method
for item in reversed(my_seq):
    print(item, end=" ")  # Output: 5 4 2 1
```

Then typing the following command in the terminal to execute the script.

```bash
python iteration_example.py
```
