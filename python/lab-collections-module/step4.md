# DefaultDict

## Defaultdict(int)

`DefaultDict` is a subclass of dict that provides a default value for a nonexistent key. Let's create a `DefaultDict` with default values `0` in `default_dict1.py` and count the occurrences of words in a sentence:

```python
from collections import defaultdict

sentence = "the quick brown fox jumps over the lazy dog"
word_count1 = defaultdict(int)

for word in sentence.split():
    # Count the occurrences of words
    word_count1[word] += 1

print(dict(word_count1))
```

Then, please run the script in the terminal:

```bash
python default_dict1.py
```

Output:

```python
{'the': 2, 'quick': 1, 'brown': 1, 'fox': 1, 'jumps': 1, 'over': 1, 'lazy': 1, 'dog': 1}
```

If we didn't use `DefaultDict`, the appeal code would look like this:

```python
sentence = "the quick brown fox jumps over the lazy dog"
result = {}

for word in sentence.split():
    if word in result:
        result[word] += 1
    else:
        result[word] = 1

print(result)
```

## Defaultdict(list)

Next, Let's create a `DefaultDict` with default values `[]` in `default_dict2.py` and store the number in each letter:

```python
from collections import defaultdict

data = [('a', 1), ('a', 1), ('a', 3), ('b', 1), ('b', 2), ('b', 3)]
word_count2 = defaultdict(list)

for (key,value) in data:
    # Store the number in each letter
    word_count2[key].append(value)

print(dict(word_count2))
```

Then, please run the script in the terminal:

```bash
python default_dict2.py
```

Output:

```python
{'a': [1, 1, 3], 'b': [1, 2, 3]}
```

If we didn't use `DefaultDict`, the appeal code would look like this:

```python
data = [('a', 1), ('a', 1), ('a', 3), ('b', 1), ('b', 2), ('b', 3)]
result = {}

for (key, value) in data:
    if key in result:
        result[key].append(value)
    else:
        result[key] = [value]

print(result)
```

## Defaultdict(set)

Finally, Let's create a `DefaultDict` with default values `set()` in `default_dict3.py` and stores the number that is not repeated in each letter:

```python
from collections import defaultdict

data = [('a', 1), ('a', 1), ('a', 3), ('b', 1), ('b', 2), ('b', 3)]
word_count3 = defaultdict(set)

for (key,value) in data:
    # Stores the number that is not repeated in each letter
    word_count3[key].add(value)

print(dict(word_count3))
```

Then, please run the script in the terminal:

```bash
python default_dict3.py
```

Output:

```python
{'a': {1, 3}, 'b': {1, 2, 3}}
```

If we didn't use `DefaultDict`, the appeal code would look like this:

```python
data = [('a', 1), ('a', 1), ('a', 3), ('b', 1), ('b', 2), ('b', 3)]
result = {}

for (key, value) in data:
    if key in result:
        result[key].add(value)
    else:
        result[key] = {value}

print(result)
```
