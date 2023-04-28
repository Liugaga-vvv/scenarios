from time import sleep
from tqdm import tqdm
from typing import Any, List


def custom_progress_bar(iterable: List[any], desc: str = "processing") -> None:
    """
    A custom progress bar that calculates the average time per iteration and estimates the remaining time for completion.

    Args:
        iterable: A list of elements that the progress bar should iterate through.
        desc: A description to display in the progress bar. Default is "Processing".
    """
    # TODO: Write your code here
