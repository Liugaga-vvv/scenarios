# F-String Tips and Tricks

Here are some tips and tricks to help you get the most out of f-strings:

## Escaping Curly Braces

To include literal curly braces in an f-string, double the curly braces `{{` and `}}`:

```python
print(f"{{Hello}}")
```

Output:

```
{Hello}
```

## Multiline F-strings

F-strings can span multiple lines using triple quotes `"""` or `'''`:

```python
name = "Alice"
age = 30
print(f"""\
Name: {name}
Age: {age}
""")
```

Output:

```
Name: Alice
Age: 30
```
