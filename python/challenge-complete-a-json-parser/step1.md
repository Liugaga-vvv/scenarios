# Parse JSON

In this challenge, you need to complete a function that can convert a `json` string into a Python object.

## Requirements

Please complete the `parse_json` function in the file `/home/labex/project/parse_json.py`.

You are given a string that represents a JSON object, write a Python function that can parse the string and return the corresponding Python object. In addition, you are not allowed to use the `json` library.

Your function should be able to handle the following types:

- Object (`dict`)
- Array (`list`)
- String(`str`)
- Number (`int`, `float`)
- Boolean (`True`, `False`)
- Null(`None`)

You can assume that the input string is a valid JSON object.

## Example

### Input:

```python
json_str =
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

### Output:

```python
{
    "name": "John",
    "age": 30,
    "city": "New York",
    "isEmployed": True,
    "car": None,
    "grades": [
        90,
        85,
        95
    ]
}
```
