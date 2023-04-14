# Deque

A `deque` (double-ended queue) is a generalization of stacks and queues that supports fast O(1) appends and pops from both ends. Let's create a `deque` in `deque.py` and perform some operations:

```python
from collections import deque

d = deque([1, 2, 3, 4, 5])

# Append to the right
d.append(6)
print("Append to the right:", d)

# Append to the left
d.appendleft(0)
print("Append to the left:", d)

# Pop from the right
right_element = d.pop()
print("The right element:", right_element)
print("Pop from the right:", d)

# Pop from the left
left_element = d.popleft()
print("The left element:", left_element)
print("Pop from the left:", d)

# Rotate the deque
d.rotate(2)
print("Rotate clockwise the deque:", d)

d.rotate(-2)
print("Rotate counterclockwise the deque:", d)
```

Then, please run the script in the terminal:

```bash
python deque.py
```

Output:

```python
Append to the right: deque([1, 2, 3, 4, 5, 6])
Append to the left: deque([0, 1, 2, 3, 4, 5, 6])
The right element: 6
Pop from the right: deque([0, 1, 2, 3, 4, 5])
The left element: 0
Pop from the left: deque([1, 2, 3, 4, 5])
Rotate clockwise the deque: deque([4, 5, 1, 2, 3])
Rotate counterclockwise the deque: deque([1, 2, 3, 4, 5])
```
