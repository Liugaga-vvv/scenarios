# User-Defined Types

You can also use custom types and classes as type hints.

> Tips： This experiment is implemented in WebIDE.

1. Define a class Person with typed attributes `name (str)` and `age (int)` and a method get_summary that returns a string summarizing the person's name and age.

Create a Project called `str_and_int_to_str.py` in the WebIDE and enter the following content.

```python
class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
    def get_summary(self) -> str:
        return f"{self.name} is {self.age} years old."

person1 = Person("Alice", 25)
print(person1.get_summary()) # Output: Alice is 25 years old.
```

Use the following command to run the script.

```bash
python str_and_int_to_str.py
```

2. Define a class Point with typed attributes `x` and `y`, both of type `float` and a method `distance` that takes another point as an argument and returns the distance between the two points.

Create a Project called `other_to_float.py` in the WebIDE and enter the following content.

```python
import math

class Point:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y
    def distance(self, other: "Point") -> float:
        return math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2)

point1 = Point(0, 0)
point2 = Point(3, 4)
print(point1.distance(point2)) # Output: 5.0

```

Use the following command to run the script.

```bash
python other_to_float.py
```
