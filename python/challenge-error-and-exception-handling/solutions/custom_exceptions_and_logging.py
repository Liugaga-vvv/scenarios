import logging, os
from typing import Any

# Custom exception classes

# Implement the FileNotFoundError exception class
class FileNotFoundError(Exception):
    """Exception raised when a file is not found."""


# Implement the InvalidDataError exception class
class InvalidDataError(Exception):
    """Exception raised when the data is invalid."""


# Implement the OperationFailedError exception class
class OperationFailedError(Exception):
    """Exception raised when an operation fails."""


# Set up logging
logging.basicConfig(
    filename="/home/labex/project/error_handling_challenge.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)


def read_data_from_file(filename: str) -> Any:
    """
    Read data from a file and return its content.

    Args:
        filename: The name of the file to read.

    Returns:
        The content of the file.

    Raises:
        FileNotFoundError: If the file pointed to by the filename variable does not exist.
    """

    if not os.path.exists(filename):
        raise FileNotFoundError(f"File {filename} not found.")

    with open(filename, "r") as file:
        data = file.read()

    return data


def process_data(data: str) -> None:
    """
    Check if the data is empty.

    Args:
        data: The data to process.

    Raises:
        InvalidDataError: If the data variable is empty.
    """

    if not data:
        raise InvalidDataError("Data is empty.")


def main() -> None:
    """
    Main process:
        1. Read the "example.txt" file.
        2. determine if the content read is empty
    """
    try:
        data = read_data_from_file("/home/labex/project/example.txt")
        process_data(data)
    except (FileNotFoundError, InvalidDataError) as e:
        logging.critical("A critical error occurred: " + str(e))


if __name__ == "__main__":
    main()
