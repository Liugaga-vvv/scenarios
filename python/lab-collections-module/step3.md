# OrderedDict

`OrderedDict` is a subclass of dict that maintains the order of elements as they were inserted. Let's create an `OrderedDict` in `ordered_dict.py` and add some key-value pairs:

```python
from collections import OrderedDict

# Initialdefining OrderedDict
od = OrderedDict()

# Insert in key-value pairs
od['a'] = 1
od['b'] = 2
od['c'] = 3

# Iterate over the key-value pairs and print out the contents
for key, value in od.items():
    print(key, value)
```

Then, please run the script in the terminal:

```bash
python ordered_dict.py
```

Output:

```python
a 1
b 2
c 3
```
