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
    Decorator that retries a function with an exponential fallback method when
    an OperationFailedError exception is raised, and writes a warning log.

    The contents of the logging module log output:
    f"Operation failed. Retrying in {wait_time} seconds. Error: {str(e)}"

    Args:
        func: The function to retry on failure.
        max_retries: The maximum number of retries allowed.
        backoff_factor: The backoff factor for exponential delay calculation.

    Returns:
        The wrapped function.
    """

    def wrapper(*args, **kwargs):
        retries = 0
        while retries < max_retries:
            try:
                return func(*args, **kwargs)
            except OperationFailedError as e:
                wait_time = backoff_factor**retries
                logging.warning(
                    f"Operation failed. Retrying in {wait_time} seconds. Error: {str(e)}"
                )
                time.sleep(wait_time)
                retries += 1
        logging.error(f"Operation failed after {max_retries} retries.")
        return None  # Return a fallback value or perform a fallback operation

    return wrapper


@retry_on_failure
def perform_critical_operation(data: str) -> None:
    """
    Perform a critical operation on the data and writes a error log.

    The contents of the raise exception:
    "Data is empty."

    The contents of the logging module log output:
    str(e)

    Args:
        data: The data to process.
    """
    try:
        if not data:
            raise OperationFailedError("Data is empty.")
        # Perform critical operation here
    except OperationFailedError as e:
        logging.error(str(e))
        raise


def main() -> None:
    """
    Main function to run the program.

    The contents of the logging module log output:
    "A critical error occurred: " + str(e)
    """
    try:
        data = read_data_from_file("/home/labex/project/example.txt")
        perform_critical_operation(data)
    except (FileNotFoundError, InvalidDataError) as e:
        logging.critical("A critical error occurred: " + str(e))


if __name__ == "__main__":
    main()
