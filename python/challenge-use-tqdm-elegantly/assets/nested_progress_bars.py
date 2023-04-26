from time import sleep
from tqdm import tqdm
from typing import Any, List


def nested_progress_bars(iterable: List[List[Any]]) -> None:
    """
    A function that creates nested progress bars to track the progress of a task with multiple sub-tasks.

    Args:
        iterable: A list of lists, where each sublist represents a sub-task.
    """
    # TODO: Write your code here
