# Combinatoric Itertools Functions

## product

The `product` computes the Cartesian product of input iterables. It takes any number of iterables as arguments and an optional `repeat` parameter, which specifies the number of repetitions of each input iterable.

**Example:**

Create a Project called `product.py` in WebIDE and enter the following content.

```python
import itertools

# Compute the Cartesian product of two lists
list1 = [1, 2]
list2 = ['a', 'b']
product_iterator = itertools.product(list1, list2)

# Print the elements of the product iterator
for item in product_iterator:
    print(item)
```

**Output:**

Use the following command to run the script.

```bash
python product.py
```

```txt
(1, 'a')
(1, 'b')
(2, 'a')
(2, 'b')
```

## permutations

The `permutations` generate all possible ordered permutations of elements from an input iterable. It takes an iterable and an optional integer `r` as arguments, specifying the permutations' length.

**Example:**

Create a Project called `permutations.py` in WebIDE and enter the following content.

```python
import itertools

# Generate all permutations of length 2 from a list
list1 = [1, 2, 3]
permutations_iterator = itertools.permutations(list1, 2)

# Print the elements of the permutations iterator
for item in permutations_iterator:
    print(item)
```

**Output:**

Use the following command to run the script.

```bash
python permutations.py
```

```txt
(1, 2)
(1, 3)
(2, 1)
(2, 3)
(3, 1)
(3, 2)
```

## combinations

The `combinations` generate all possible unordered combinations of elements from an input iterable. It takes an iterable and an integer `r` as arguments, specifying the combinations' length.

**Example:**

Create a Project called `combinations.py` in WebIDE and enter the following content.

```python
import itertools

# Generate all combinations of length 2 from a list
list1 = [1, 2, 3]
combinations_iterator = itertools.combinations(list1, 2)

# Print the elements of the combinations iterator
for item in combinations_iterator:
    print(item)
```

**Output:**

Use the following command to run the script.

```bash
python combinations.py
```

```txt
(1, 2)
(1, 3)
(2, 3)
```

## combinations_with_replacement

The `combinations_with_replacement` generates all possible unordered combinations of elements from an input iterable, allowing for repeated elements. It takes an iterable and an integer `r` as arguments, specifying the combinations' length.

**Example:**

Create a Project called `cr.py` in WebIDE and enter the following content.

```python
import itertools

# Generate all combinations with replacement of length 2 from a list
list1 = [1, 2, 3]
combinations_iterator = itertools.combinations_with_replacement(list1, 2)

# Print the elements of the combinations_with_replacement iterator
for item in combinations_iterator:
    print(item)
```

**Output:**

Use the following command to run the script.

```bash
python cr.py
```

```txt
(1, 1)
(1, 2)
(1, 3)
(2, 2)
(2, 3)
(3, 3)
```
