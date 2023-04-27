from time import sleep
from tqdm import tqdm
from typing import Any, List


def nested_progress_bars(iterable: List[List[Any]]) -> None:
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


tasks = [[1, 2], [2, 1, 3], [1, 1]]
nested_progress_bars(tasks)
