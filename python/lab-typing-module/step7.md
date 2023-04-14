# Typeddict

`TypedDict` allows you to create custom dictionaries with specific keys and value types.

> Tips: TypedDict was introduced in Python 3.8, so you need to be running Python 3.8 or later to use it.

Here's an example:

Create a Project called `typeddict.py` in the WebIDE and enter the following content.

```python
from typing import TypedDict

class PersonInfo(TypedDict):
    name: str
    age: int

def greet(person: PersonInfo) -> str:
    return f"Hello, {person['name']}! You are {person['age']} years old."

alice_info: PersonInfo = {"name": "Alice", "age": 30}
print(greet(alice_info))  # Output: Hello, Alice! You are 30 years old.
```

Use the following command to run the script.

```bash
python typeddict.py
```
