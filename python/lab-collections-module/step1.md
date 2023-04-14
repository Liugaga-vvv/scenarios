# NamedTuple

A `namedtuple` is a subclass of a tuple, providing named fields for more readability and self-documenting code. Let's create a `namedtuple` in `named_tuple.py` to represent a point in a 2D space:

```python
# Import collections
from collections import namedtuple

# Define a namedtuple type Point with x and y properties
Point = namedtuple('Point', ['x', 'y'])

# Create a Poinit object
p = Point(1, 2)

# Retrieve the properties of point
print(p.x)
print(p.y)
```

Then, please run the script in the terminal:

```bash
python named_tuple.py
```

Output:

```python
1
2
```
