from typing import Any, List, Dict, Union


def serialize_json(obj: Any) -> str:
    """
    Convert a Python object to a JSON string.

    Args:
        obj: The Python object to convert.

    Returns:
        A JSON string representing the input object.

    Raises:
        TypeError: If the input object is not JSON serializable.
    """
    if obj is None:
        return "null"
    elif isinstance(obj, bool):
        return "true" if obj else "false"
    elif isinstance(obj, (int, float)):
        return str(obj)
    elif isinstance(obj, str):
        return '"' + obj.replace('"', '\\"') + '"'
    elif isinstance(obj, list):
        elems = ",".join(serialize_json(elem) for elem in obj)
        return "[" + elems + "]"
    elif isinstance(obj, dict):
        pairs = []
        for key, val in obj.items():
            key_str = '"' + str(key).replace('"', '\\"') + '"'
            val_str = serialize_json(val)
            pairs.append(key_str + ":" + val_str)
        pairs_str = ",".join(pairs)
        return "{" + pairs_str + "}"
    else:
        raise TypeError(f"Object of type {type(obj).__name__} is not JSON serializable")
