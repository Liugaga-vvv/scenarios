# Using Assignment Expressions in a List Comprehension

Finally, let's explore using assignment expressions in a list comprehension.

```python
# Using assignment expressions in a list comprehension
from math import sqrt

numbers = [1, 4, 9, 16, 25]
roots = [int(root) for n in numbers if (root := sqrt(n)) == int(root)]
print(roots)
```

Output:

```python
[1, 2, 3, 4, 5]
```

In this example, we use the walrus operator within a list comprehension to calculate the square root of each number in `numbers` and check if it is an integer. If it is, we add the integer square root to the `roots` list.
