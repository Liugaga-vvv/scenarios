# Advanced Usage

In this step, we will explore some advanced usage of the `is` operator.

1. Define a class `MyClass` with an attribute `value`.

```python
class MyClass:
    def __init__(self, value):
        self.value = value
```

2. Define two instances of the `MyClass` class, `obj1` and `obj2`, with the same `value`.

```python
obj1 = MyClass("Hello")
obj2 = MyClass("Hello")
```

3. Print out the memory address of `obj1.value` and `obj2.value` using the `id()` function.

```python
print(id(obj1.value))
print(id(obj2.value))
```

4. Use the `is` operator to check if `obj1.value` and `obj2.value` refer to the same object.

```python
print(obj1.value is obj2.value)
```

The output of the above code should be `True`, since the `value` attribute is an immutable object and both instances share the same object in memory.

5. Now, define two instances of the `MyClass` class, `obj3` and `obj4`, with a mutable object as their `value`.

```python
obj3 = MyClass([])
obj4 = MyClass([])
```

6. Print out the memory address of `obj3.value` and `obj4.value` using the `id()` function.

```python
print(id(obj3.value))
print(id(obj4.value))
```

7. Use the `is` operator to check if `obj3.value` and `obj4.value` refer to the same object.

```python
print(obj3.value is obj4.value)
```

The output of the above code should be `False`, since the `value` attribute is a mutable object and both instances do not share the same object in memory.
