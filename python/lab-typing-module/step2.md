# Containers and Generics

Type hints for container types (like lists, dictionaries, and sets) can be more specific using generics.

> Tips: The experiments with serial numbers 1-3 can be implemented in python shell, and the experiments with serial number 4 are implemented in WebIDE.

1. Define a variable of type `List[int]`, assign some values, and print it.

```python
from typing import List
numbers: List[int] = [1, 2, 3, 4, 5]
print(numbers) # Output: [1, 2, 3, 4, 5]

```

2. Define a variable of type `Dict[str, int]`, assign it some key-value pairs, and print it.

```python
from typing import Dict
ages: Dict[str, int] = {"Alice": 25, "Bob": 30, "Charlie": 35}
print(ages) # Output: {'Alice': 25, 'Bob': 30, 'Charlie': 35}

```

3. Define a variable of type `Tuple[str, int, float]`, assign it some values, and print it.

```python
from typing import Tuple
person: Tuple[str, int, float] = ("Alice", 25, 5.7)
print(person) # Output: ('Alice', 25, 5.7)

```

4. Define a function that takes a list of integers as an argument and returns the result as a new set of integers.

Create a Project called `list_to_set.py` in the WebIDE and enter the following content.

```python
from typing import List, Set

def get_unique_elements(elements: List[int]) -> Set[int]:
    return set(elements)

numbers = [1, 2, 2, 3, 4, 4, 4, 5]
unique_numbers = get_unique_elements(numbers)
print(unique_numbers)  # Output: {1, 2, 3, 4, 5}
```

Use the following command to run the script.

```bash
python list_to_set.py
```
