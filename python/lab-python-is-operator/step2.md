# Immutable vs Mutable Objects

In this step, we will explore how the `is` operator behaves with immutable and mutable objects.

1. Define two variables, `c` and `d`, and assign them both an empty list `[]`.

```python
c = []
d = []
```

2. Print out the memory address of `c` and `d` using the `id()` function.

```python
print(id(c))
print(id(d))
```

3. Use the `is` operator to check if `c` and `d` refer to the same object.

```python
print(c is d)
```

The output of the above code should be `False`, since `c` and `d` are mutable objects and they are not the same object in memory.

4. Now, define two variables, `e` and `f`, and assign them both an integer value.

```python
e = 10
f = 10
```

5. Print out the memory address of `e` and `f` using the `id()` function.

```python
print(id(e))
print(id(f))
```

6. Use the `is` operator to check if `e` and `f` refer to the same object.

```python
print(e is f)
```

The output of the above code should be `True`, since `e` and `f` are immutable objects and they share the same object in memory.
