# Item Access

Item access methods are special methods in Python that allow objects to define their behavior when accessed using square bracket notation `[]`.

## \_\_getitem\_\_

The `__getitem__` magic method is used to define the behavior of the square bracket notation for accessing items in instances of your class.

```python
    # ... (previous code in sequence.py)

    def __getitem__(self, index: int) -> object:
        """Return the item at the given index."""
        return self.data[index]
```

## \_\_setitem\_\_

The `__setitem__` magic method is used to define the behavior of the square bracket notation for setting items in instances of your class.

```python
    # ... (previous code in sequence.py)

    def __setitem__(self, index: int, value: object) -> None:
        """Set the item at the given index to the given value."""
        self.data[index] = value
```

## \_\_delitem\_\_

The `__delitem__` magic method is used to define the behavior of the `del` keyword when applied to instances of your class.

```python
    # ... (previous code in sequence.py)

    def __delitem__(self, index: int) -> None:
        """Remove the item at the given index."""
        del self.data[index]
```

## Example: Using the Item Access Methods

Now that we have defined the item access methods for our `MySequence` class, let's see how they work in `item_access_example.py`:

```python
from sequence import MySequence

# Create a MySequence object
my_seq = MySequence([1, 2, 3, 4, 5])

# Test the __getitem__ magic method
print(my_seq[2])  # Output: 3

# Test the __setitem__ magic method
my_seq[2] = 9
print(my_seq[2])  # Output: 9

# Test the __delitem__ magic method
del my_seq[2]
print(len(my_seq))  # Output: 4
print(my_seq.data)  # Output: [1, 2, 4, 5]
```

Then typing the following command in the terminal to execute the script.

```bash
python item_access_example.py
```
