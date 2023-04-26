from time import sleep
from tqdm import tqdm
from typing import Any, List


def custom_progress_bar(iterable: List[Any], desc: str = "Processing") -> None:
    """
    A custom progress bar that calculates the average time per iteration and estimates the remaining time for completion.

    Args:
        iterable: A list of elements that the progress bar should iterate through.
        desc: A description to display in the progress bar. Default is "Processing".
    """
    total_iterations = len(iterable)
    avg_time_per_iteration = 0

    with tqdm(total=total_iterations, desc=desc, dynamic_ncols=True, bar_format="{l_bar}{bar}{n}/{total} [{elapsed}<{remaining}]") as pbar:
        for i, item in enumerate(iterable):
            start_time = pbar.format_dict["elapsed"]
            sleep(item)  # Simulating the processing of the item
            pbar.update(1)
            elapsed_time = pbar.format_dict["elapsed"] - start_time

            # Update average time per iteration
            avg_time_per_iteration = (
                (avg_time_per_iteration * i) + elapsed_time) / (i + 1)
            pbar.set_postfix_str(
                f"ETA: {avg_time_per_iteration * (total_iterations - (i + 1)):.2f}s", refresh=True)
