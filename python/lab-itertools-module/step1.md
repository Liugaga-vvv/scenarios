# Basic Itertools Functions

## chain

The `chain` is used to combine multiple iterables into a single iterable. It takes any number of iterables as arguments and returns a single iterator that produces elements from the input iterables in sequence.

**Example:**

Create a Project called `chain.py` in WebIDE and enter the following content.

```python
import itertools

list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']

# Chain the two lists together
result = itertools.chain(list1, list2)

# Print the elements of the chained iterator
for item in result:
    print(item)
```

**Output:**

Input `python chain.py` in Terminal. Then check the output.

```txt
1
2
3
a
b
c
```

## cycle

The `cycle` is used to create an iterator that cycles through the elements of an input iterable indefinitely.

**Example:**

Create a Project called `cycle.py` in WebIDE and enter the following the content.

```python
import itertools

# Create a cycle iterator from a list
cycle_iterator = itertools.cycle([1, 2, 3])

# Print the first 10 elements of the cycle iterator
for i, item in enumerate(cycle_iterator):
    if i >= 10:
        break
    print(item)
```

**Output:**

Use the following command to run the script.

```bash
python cycle.py
```

```txt
1
2
3
1
2
3
1
2
3
1
```

## count

The `count` creates an iterator that generates consecutive integers indefinitely, starting from an optional specified number.

**Example:**

Create a Project called `count.py` in WebIDE and enter the following content.

```python
import itertools

# Create a count iterator starting from 5
count_iterator = itertools.count(5)

# Print the first 10 elements of the count iterator
for i, item in enumerate(count_iterator):
    if i >= 10:
        break
    print(item)
```

**Output:**

Use the following command to run the script.

```bash
python count.py
```

```txt
5
6
7
8
9
10
11
12
13
14
```
