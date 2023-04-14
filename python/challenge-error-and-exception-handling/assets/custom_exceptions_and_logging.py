import logging

# Custom exception classes

# Implement the FileNotFoundError exception class

# TODO

# Implement the InvalidDataError exception class

# TODO

# Implement the OperationFailedError exception class

# TODO

# Set up logging
logging.basicConfig(
    filename="/home/labex/project/error_handling_challenge.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)


def read_data_from_file(filename: str) -> str:
    """
    Read data from a file and return its content.

    Hints when raising an exception:
        f"File {filename} not found."

    Args:
        filename: The name of the file to read.

    Returns:
        The content of the file.

    Raises:
        FileNotFoundError: If the file pointed to by the filename variable does not exist.
    """

    # TODO: completing the code to catch the exception

    with open(filename, "r") as file:
        data = file.read()

    return data


def process_data(data: str) -> None:
    """
    Check if the data is empty.

    Hints when raising an exception:
        'Data is empty.'
    Args:
        data: The data to process.

    Raises:
        InvalidDataError: If the data variable is empty.
    """

    # TODO: Check if the data is empty, if it is empty then pop up
    #   InvalidDataError exception, if it is not empty then do not do any processing


def main() -> None:
    """
    Main process:
        1. Read the "/home/labex/project/example.txt" file.
        2. determine if the content read is empty
    """

    # TODO: Use try except to catch FileNotFoundError and InvalidDataError exceptions
    #   and logging of generated exceptions to the logging system

    data = read_data_from_file("/home/labex/project/example.txt")
    process_data(data)


if __name__ == "__main__":
    main()
