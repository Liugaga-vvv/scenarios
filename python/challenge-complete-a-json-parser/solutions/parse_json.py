from typing import Any, Dict, List, Union


def parse_json(json_str: str) -> Any:
    """
    Parse a JSON string and return the corresponding Python object.

    Args:
        json_str: The JSON string to parse.

    Returns:
        A Python object representing the input JSON.

    Raises:
        ValueError: If the input string is not valid JSON.
    """
    pos = 0

    # Skip whitespace characters
    def skip_whitespace() -> None:
        nonlocal pos
        while pos < len(json_str) and json_str[pos].isspace():
            pos += 1

    # Parse a JSON value
    def parse_value() -> Any:
        nonlocal pos
        skip_whitespace()
        if json_str[pos] == "{":
            return (
                parse_object()
            )  # Call parse_object function if the current character is an opening brace
        elif json_str[pos] == "[":
            return (
                parse_array()
            )  # Call parse_array function if the current character is an opening bracket
        elif json_str[pos] == '"':
            return (
                parse_string()
            )  # Call parse_string function if the current character is a double-quote
        elif json_str[pos].isdigit() or json_str[pos] == "-":
            return (
                parse_number()
            )  # Call parse_number function if the current character is a digit or minus sign
        elif json_str[pos] == "t" or json_str[pos] == "f":
            return (
                parse_boolean()
            )  # Call parse_boolean function if the current character is 't' or 'f'
        elif json_str[pos] == "n":
            return (
                parse_null()
            )  # Call parse_null function if the current character is 'n'
        else:
            raise ValueError("Invalid JSON value")

    # Parse a JSON object
    def parse_object() -> Dict[str, Any]:
        nonlocal pos
        obj = {}
        pos += 1  # Increment position past opening brace
        while True:
            skip_whitespace()
            if (
                json_str[pos] == "}"
            ):  # If the current character is a closing brace, return the object
                pos += 1
                return obj
            key = parse_string()  # Parse the key as a string
            skip_whitespace()
            if json_str[pos] != ":":
                raise ValueError("Expected colon")
            pos += 1
            val = parse_value()  # Parse the value recursively
            obj[key] = val  # Add the key-value pair to the object
            skip_whitespace()
            if json_str[pos] == ",":
                pos += 1  # Increment position past comma
            elif json_str[pos] == "}":
                pos += 1  # Increment position past closing brace and return the object
                return obj
            else:
                raise ValueError("Expected comma or closing brace")

    # Parse a JSON array
    def parse_array() -> List[Any]:
        nonlocal pos
        arr = []
        pos += 1  # Increment position past opening bracket
        while True:
            skip_whitespace()
            if (
                json_str[pos] == "]"
            ):  # If the current character is a closing bracket, return the array
                pos += 1
                return arr
            val = parse_value()  # Parse the value recursively
            arr.append(val)  # Add the value to the array
            skip_whitespace()
            if json_str[pos] == ",":
                pos += 1  # Increment position past comma
            elif json_str[pos] == "]":
                pos += 1  # Increment position past closing bracket and return the array
                return arr
            else:
                raise ValueError("Expected comma or closing bracket")

    # Parse a JSON string
    def parse_string() -> str:
        nonlocal pos
        start = pos + 1
        pos = json_str.find(
            '"', start
        )  # Find the next double-quote character starting from the current position
        if pos == -1:
            raise ValueError("Expected closing double-quote")
        val = json_str[start:pos]  # Extract the string value
        pos += 1  # Increment position past closing double-quote
        return val

    # Parse a JSON number
    def parse_number() -> Union[int, float]:
        nonlocal pos
        start = pos
        while pos < len(json_str) and (
            json_str[pos].isdigit() or json_str[pos] in [".", "e", "E", "+", "-"]
        ):
            pos += 1
        num_str = json_str[start:pos]  # Extract the number string
        try:
            return int(num_str)  # Return an integer if the number is an integer
        except ValueError:
            return float(num_str)  # Otherwise, return a float

    # Parse a JSON boolean
    def parse_boolean() -> bool:
        nonlocal pos
        if json_str[pos] == "t":
            pos += 4  # Increment position past the characters 'true'
            return True
        else:
            pos += 5  # Increment position past the characters 'false'
            return False

    # Parse a JSON null
    def parse_null() -> None:
        nonlocal pos
        pos += 4  # Increment position past the characters 'null'
        return None

    return parse_value()  # Call parse_value to start parsing the JSON string
