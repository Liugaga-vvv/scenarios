# Object Initialization and Representation

In this section, we will explore object initialization and representation magic methods in Python. These methods allow you to define custom behavior for creating objects and representing them as human-readable and unambiguous strings.

## \_\_init\_\_

The `__init__` method is called when an object is created. It is used to initialize the object's attributes.

Let's start with a simple object. In `person.py`, create a class named `Person` that have two attributes.

```python
class Person:
    def __init__(self, name: str, age: int):
        """
        Initialize the Person object with a name and age.

        :param name: The name of the person.
        :param age: The age of the person.
        """
        self.name = name
        self.age = age

```

## \_\_str\_\_

The `__str__` method is called by the `str()` built-in function and the `print()` function to get a human-readable string representation of the object.

```python
    # ... (previous code in person.py)

    def __str__(self) -> str:
        """
        Return a human-readable string representation of the Person object.

        :return: A string describing the person.
        """
        return f"{self.name} is {self.age} years old."
```

## \_\_repr\_\_

The `__repr__` method is called by the `repr()` built-in function and used in the interactive interpreter to get a string representation that, if possible, can be used to recreate the object.

```python
    # ... (previous code in person.py)

    def __repr__(self) -> str:
        """
        Return a string representation of the Person object that can be used to recreate the object.

        :return: A string in the format 'Person(name, age)'.
        """
        return f"Person('{self.name}', {self.age})"
```

## Example: Using the Basic Magic Methods

Now that we have defined the basic magic methods for our `Person` class, let's see how they work in `init_repr_example.py`:

```python
from person import Person

# Create a new Person object
p = Person("Alice", 30)

# Use the __str__ method with the print function
print(p)  # Output: Alice is 30 years old.

# Use the __repr__ method in the interactive interpreter
print(repr(p))  # Output: Person('Alice', 30)
```

Then typing the following command in the terminal to execute the script.

```bash
python init_repr_example.py
```
