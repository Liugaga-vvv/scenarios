# Object Comparison

In this section, we will explore the magic methods used for object comparison in Python. These methods allow you to define custom comparison logic for objects of your class.

## \_\_eq\_\_

The `__eq__` method is used to determine if two objects are equal. It is called by the `==` operator.

```python
    # ... (previous code in person.py)

    def __eq__(self, other: "Person") -> bool:
        """
        Compare two Person objects for equality.

        :param other: The other Person object to compare with.
        :return: True if both objects have the same name and age, False otherwise.
        """
        if isinstance(other, Person):
            return self.name == other.name and self.age == other.age
        return False
```

## \_\_ne\_\_

The `__ne__` method is used to determine if two objects are not equal. It is called by the `!=` operator.

```python
    # ... (previous code in person.py)

    def __ne__(self, other: "Person") -> bool:
        """
        Compare two Person objects for inequality.

        :param other: The other Person object to compare with.
        :return: True if the objects have different names or ages, False otherwise.
        """
        return not self.__eq__(other)
```

## \_\_lt\_\_

The `__lt__` method is used to determine if one object is less than another. It is called by the `<` operator.

```python
    # ... (previous code in person.py)

    def __lt__(self, other: "Person") -> bool:
        """
        Compare two Person objects to see if one is less than the other based on age.

        :param other: The other Person object to compare with.
        :return: True if the current object's age is less than the other object's age, False otherwise.
        """
        if isinstance(other, Person):
            return self.age < other.age
        return NotImplemented
```

## \_\_le\_\_

The `__le__` method is used to determine if one object is less than or equal to another. It is called by the `<=` operator.

```python
    # ... (previous code in person.py)

    def __le__(self, other: "Person") -> bool:
        """
        Compare two Person objects to see if one is less than or equal to the other based on age.

        :param other: The other Person object to compare with.
        :return: True if the current object's age is less than or equal to the other object's age, False otherwise.
        """
        if isinstance(other, Person):
            return self.age <= other.age
        return NotImplemented
```

## \_\_gt\_\_

The `__gt__` method is used to determine if one object is greater than another. It is called by the `>` operator.

```python
    # ... (previous code in person.py)

    def __gt__(self, other: "Person") -> bool:
        """
        Compare two Person objects to see if one is greater than the other based on age.

        :param other: The other Person object to compare with.
        :return: True if the current object's age is greater than the other object's age, False otherwise.
        """
        if isinstance(other, Person):
            return self.age > other.age
        return NotImplemented
```

## \_\_ge\_\_

The `__ge__` method is used to determine if one object is greater than or equal to another. It is called by the `>=` operator.

```python
    # ... (previous code in person.py)

    def __ge__(self, other: "Person") -> bool:
        """
        Compare two Person objects to see if one is greater than or equal to the other based on age.

        :param other: The other Person object to compare with.
        :return: True if the current object's age is greater than or equal to the other object's age, False otherwise.
        """
        if isinstance(other, Person):
            return self.age >= other.age
        return NotImplemented
```

## Example: Using the Object Comparison Magic Methods

Now that we have defined the object comparison magic methods for our `Person` class, let's see how they work in `compare_example.py`:

```python
from person import Person

# Create two Person objects
p1 = Person("Alice", 30)
p2 = Person("Bob", 35)

# Use the __eq__ and __ne__ methods
print(p1 == p2)  # Output: False
print(p1 != p2)  # Output: True

# Use the __lt__, __le__, __gt__, and __ge__ methods
print(p1 < p2)  # Output: True
print(p1 <= p2)  # Output: True
print(p1 > p2)  # Output: False
print(p1 >= p2)  # Output: False
```

Then typing the following command in the terminal to execute the script.

```bash
python compare_example.py
```
