import time
from typing import Callable

from custom_exceptions_and_logging import (
    logging,
    read_data_from_file,
    FileNotFoundError,
    InvalidDataError,
    OperationFailedError,
)


def retry_on_failure(
    func: Callable, max_retries: int = 3, backoff_factor: float = 2.0
) -> Callable:
    """
    Decorator that sleeps backoff_factor**number-of-backoffs time and retries
    a function with an exponential fallback method and writes a warning log when
    an OperationFailedError exception occurs.

    When the number of retries is less than max_retries:
        log level:
            WARNING
        The contents of the logging module log output:
            f"Operation failed. Retrying in {wait_time} seconds. Error: {str(e)}"

    When the number of retries is larger than max_retries:
        log level:
            WARNING
        The contents of the logging module log output:
            f"Operation failed after {max_retries} retries."

    Args:
        func: The function to retry on failure.
        max_retries: The maximum number of retries allowed.
        backoff_factor: The backoff factor for exponential delay calculation.

    Returns:
        The wrapped function.
    """

    def wrapper(*args, **kwargs):

        # TODO: Follow the function description to complete this function

        return None  # Return a fallback value or perform a fallback operation

    return wrapper


@retry_on_failure
def perform_critical_operation(data: str) -> None:
    """
    Checks if the data is empty.
    If the data is empty, writes to the error log and raise an OperationFailedError exception.
    If the data is not empty, return the string.

    Hints when raising an exception:
    "Data is empty."

    The contents of the logging module log output:
        str(e)

    Args:
        data: The data to process.

    Raises:
        InvalidDataError: If the data variable is empty.
    """

    # TODO


def main() -> None:
    """
    Main process:
        1. Read the "/home/labex/project/example.txt" file.
        2. determine if the content read is empty

    log level:
        CRITICAL
    The contents of the logging module log output:
        "A critical error occurred: " + str(e)

    """

    # TODO: completing the code to catch the exception

    data = read_data_from_file("/home/labex/project/example.txt")
    perform_critical_operation(data)


if __name__ == "__main__":
    main()
