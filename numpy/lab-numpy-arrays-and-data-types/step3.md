# Modifying Elements

We can modify the value of an element in an array by assigning a new value to it.

```python
my_array = np.array([1, 2, 3])
my_array[2] = 4
print(my_array)  # Output: [1 2 4]
```

We can also modify a slice of an array.

```python
my_array = np.array([1, 2, 3, 4, 5])
my_array[1:4] = [6, 7, 8]
print(my_array)  # Output: [1 6 7 8 5]
```
