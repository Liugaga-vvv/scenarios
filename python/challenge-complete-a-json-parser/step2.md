# Serialize to JSON

In this challenge, you need to complete a function that can convert a Python object into a `json` string.

## Requirements

Please complete the `serialize_json` function in the file `/home/labex/project/serialize_json.py`.

Write a Python function that can serialize a Python object to a JSON string. And you are not allowed to use the `json` library.

Your function should be able to handle the following types:

- Object (`dict`)
- Array (`list`)
- String(`str`)
- Number (`int`, `float`)
- Boolean (`True`, `False`)
- Null(`None`)

You can assume that the input object is a valid Python object.

## Example

### Input:

```python
obj = {
    "name": "John",
    "age": 30,
    "city": "New York",
    "isEmployed": True,
    "car": None,
    "grades": [90, 85, 95]
}
```

### Output:

```python
'{
    "name": "John",
    "age": 30,
    "city": "New York",
    "isEmployed": true,
    "car": null,
    "grades": [
        90,
        85,
        95
    ]
}'
```
