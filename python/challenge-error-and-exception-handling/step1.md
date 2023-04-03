# Custom Exceptions and Logging

In this sub-challenge, you will create custom exception classes for specific error conditions and use the `logging` module to log exceptions and important events in the application.

## Purpose

This sub-challenge aims to help you understand how to create custom exception classes and use the `logging` module to record error messages and events for later analysis.

There is a piece of code in `custom_exceptions_and_logging.py` that is designed to read from the `example.txt` file we provided and do some processing, now you need to add some exception handling to this code. The content of the hint when the exception is raised is in the function explanation of the corresponding function.

## Basic Syntax

### Create Custom Exception Classes

Implementing a custom exception class requires attention to the following points:

1. Use the **CamelCase** rule to name the custom exception class and end it with the word `Error`.
2. Custom exception classes must inherit from the `Exception` class.

For example:

Create an exception class named `TestError`:

```python
class TestError(Exception):
  # Do something
```

### Catching exception

Challengers can use the `try except` statement to catch exceptions.

For example:

1. Basic usage

This writing style catches all errors.

```python
try:
  # Execution of code that may cause an exception
except:
  # Execute the code that responds to the exception when it occurs
```

2. Catch exceptions of specified type

Like the following code, where `Exception` is the specific exception class to be caught, it can be a single exception class or a exception class tuple.

```python
try:
  # Execution of code that may cause an exception
except Exception as variable-name:
  # Execute the code that responds to the exception when it occurs
```

## Requirements

1. Create custom exception classes for the following error conditions:

- `FileNotFoundError`
- `InvalidDataError`
- `OperationFailedError`

2. In the `read_data_from_file` function, if the file pointed to by the parameter `filename` does not exist, a `FileNotFoundError` exception is raised.
3. In the `process_data` function, `InvalidDataError` is raised when the parameter `data` is an empty string.
4. In the `main` function, Use `try...except...` blocks, receive `FileNotFoundError` and `InvalidDataError` exceptions, and write a `CRITICAL` type log.

## TODO

- Completing `/home/labex/project/custom_exceptions_and_logging.py`
- Implement the custom exception classes mentioned above, inheriting from the `Exception` class.
- Raise and handle custom exceptions where appropriate in your code, and use the `logging` module that has been set up to log the error messages caught by the exception.
