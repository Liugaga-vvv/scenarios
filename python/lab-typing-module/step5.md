# Optional and None

The `Optional` type can be used when a value can be either of a specific type or `None`.

1. Define a function that takes an optional int argument, multiplies it by `2` if it is not `None`, and returns the result as an `int` or `None` if the input was `None`.

Create a Project called `option_and_none_1.py` in the WebIDE and enter the following content.

```python
from typing import Optional

def double_or_none(number: Optional[int]) -> Optional[int]:
    if number is not None:
        return number * 2
    else:
        return None

result1 = double_or_none(5)
result2 = double_or_none(None)
print(result1, result2) # Output: 10 None
```

Use the following command to run the script.

```bash
python option_and_none_1.py
```

2. Define a class Person with a typed attribute address, either a valid address string or None.

Create a Project called `option_and_none_2.py` in the WebIDE and enter the following content.

```python
from typing import Optional

class Person:
    def __init__(self, name: str, age: int, address: Optional[str]):
        self.name = name
        self.age = age
        self.address = address

person1 = Person("Alice", 25, "123 Main St")
person2 = Person("Bob", 30, None)
print(person1.name, person1.age, person1.address) # Output: Alice 25 123 Main St
print(person2.name, person2.age, person2.address) # Output: Bob 30 None
```

Use the following command to run the script.

```bash
python option_and_none_2.py
```
