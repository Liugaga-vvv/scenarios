# Length and Containment

Length and containment methods are special methods in Python that allow objects to define their behavior when used with built-in functions or operators such as `len()`, `in`, and `not in`.

Let's start with a simple object. In `sequence.py`, create a class named `MySequence` that have an attribute `data`.

```python
class MySequence:
    def __init__(self, data: list):
        """Initialize a new MySequence object with the given data."""
        self.data = data
```

## \_\_len\_\_

The `__len__` magic method is used to define the behavior of the `len()` function when applied to instances of your class.

```python
    # ... (previous code in sequence.py)

    def __len__(self) -> int:
        """Return the length of the sequence."""
        return len(self.data)
```

## \_\_contains\_\_

The `__contains__` magic method is used to define the behavior of the `in` and `not in` operators when applied to instances of your class.

```python
    # ... (previous code in sequence.py)

    def __contains__(self, item: object) -> bool:
        """Check if the sequence contains the given item."""
        return item in self.data
```

## Example: Using the Length and Containment Methods

Now that we have defined the length and containment methods for our `MySequence` class, let's see how they work in `length_containment_example.py`:

```python
from sequence import MySequence

# Create a MySequence object
my_seq = MySequence([1, 2, 3, 4, 5])

# Test the __len__ magic method
print(len(my_seq))  # Output: 5

# Test the __contains__ magic method
print(3 in my_seq)  # Output: True
print(3 not in my_seq)  # Output: False
print(10 in my_seq)  # Output: False
```

Then typing the following command in the terminal to execute the script.

```bash
python length_containment_example.py
```
