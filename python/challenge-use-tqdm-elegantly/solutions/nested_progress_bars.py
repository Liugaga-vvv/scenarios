from time import sleep
from tqdm import tqdm
from typing import Any, List


def nested_progress_bars(iterable: List[List[Any]]) -> None:
    """
    A function that creates nested progress bars to track the progress of a task with multiple sub-tasks.

    Args:
        iterable: A list of lists, where each sublist represents a sub-task.
    """
    total_main_tasks = len(iterable)

    with tqdm(total=total_main_tasks, desc="Main Task", dynamic_ncols=True, bar_format="{l_bar}{bar}{n}/{total} [{elapsed}<{remaining}, {rate_fmt}]") as main_pbar:
        for i, main_task in enumerate(iterable):
            total_sub_tasks = len(main_task)
            main_pbar.set_description(f"Main Task {i+1}")

            with tqdm(total=total_sub_tasks, desc=f"Sub-Task {i+1}", leave=False, dynamic_ncols=True, bar_format="{l_bar}{bar}{n}/{total} [{elapsed}<{remaining}, {rate_fmt}]") as sub_pbar:
                for sub_task in main_task:
                    sleep(sub_task)  # Simulating the processing of the sub-task
                    sub_pbar.update(1)

            main_pbar.update(1)
