# Counter

`Counter` is a subclass of `dict` that counts the occurrences of elements in a collection. Let's create a `Counter` object in `counter.py` to count the occurrences of characters in a string:

```python
from collections import Counter

text = "hello, world!"
# Gets the number of occurrences of the elements in the collection and returns them as a dictionary
char_count = Counter(text)

print(char_count)
```

Then, please run the script in the terminal:

```bash
python counter.py
```

Output:

```python
Counter({'l': 3, 'o': 2, 'h': 1, 'e': 1, ',': 1, ' ': 1, 'w': 1, 'r': 1, 'd': 1, '!': 1})
```
