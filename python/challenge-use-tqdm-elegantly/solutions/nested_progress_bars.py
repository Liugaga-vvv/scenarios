from time import sleep
from tqdm import tqdm
from typing import Any, List


# define a function that takes a nested list of tasks as input and displays the progress of completing those tasks in nested progress bars.
def nested_progress_bars(iterable: List[List[any]]) -> None:
    # find the total number of main tasks (as the length of the iterable's list).
    total_main_tasks = len(iterable)

    # initialize a tqdm progress bar, with options to show the progress in real time, display information about the "main" task being completed, and format the appearance of the progress bar.
    with tqdm(total=total_main_tasks, desc="main task", dynamic_ncols=True, bar_format="{l_bar}{bar}{n}/{total} [{elapsed}<{remaining}, {rate_fmt}]") as main_pbar:
        # loop through each "main" task within the iterable, while keeping track of its index (i).
        for i, main_task in enumerate(iterable):
            # find the total number of sub-tasks within the current main task.
            total_sub_tasks = len(main_task)
            # update the description shown on the main progress bar to reflect which main task is currently being processed.
            main_pbar.set_description(f"main task {i+1}")

            # initialize another tqdm progress bar, this time for the sub-tasks within the current main task.
            with tqdm(total=total_sub_tasks, desc=f"sub-task {i+1}", leave=False, dynamic_ncols=True, bar_format="{l_bar}{bar}{n}/{total} [{elapsed}<{remaining}, {rate_fmt}]") as sub_pbar:
                # loop through each sub-task within the current main task, while pausing temporarily to simulate processing of the sub-task.
                for sub_task in main_task:
                    sleep(sub_task)  
                    # update the progress bar for the sub-tasks to reflect that one additional sub-task has been completed.
                    sub_pbar.update(1)

            # update the progress bar for the main tasks to reflect that one additional main task has been completed.
            main_pbar.update(1)

# define a nested list of tasks, where each "main" task is represented by a list containing multiple "sub-tasks," and call the nested_progress_bars function with this input.
tasks = [[1, 2], [2, 1, 3], [1, 1]]
nested_progress_bars(tasks)
