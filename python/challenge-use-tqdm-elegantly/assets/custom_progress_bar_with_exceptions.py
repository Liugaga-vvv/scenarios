from time import sleep
from tqdm import tqdm
from typing import Any, List


def custom_progress_bar_with_exceptions(iterable: List[Any], desc: str = "Processing") -> None:
    """
    A custom progress bar with exception handling and graceful exit capabilities.

    Args:
        iterable: A list of elements that the progress bar should iterate through.
        desc: A description to display in the progress bar. Default is "Processing".
    """
    # TODO: Write your code here
