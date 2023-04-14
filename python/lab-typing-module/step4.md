# Type Aliases

Type aliases can create more readable type hints, especially for complex types.

Create a Project called `type_aliases.py` in the WebIDE and enter the following content.

```python
from typing import List, Tuple

Coordinate = Tuple[float, float]
Path = List[Coordinate]

def get_distance(coord1: Coordinate, coord2: Coordinate) -> float:
    return ((coord1[0] - coord2[0])**2 + (coord1[1] - coord2[1])**2)**0.5

start = (0, 0)
end = (3, 4)
print(get_distance(start, end))  # Output: 5.0
```

Use the following command to run the script.

```bash
python type_aliases.py
```
