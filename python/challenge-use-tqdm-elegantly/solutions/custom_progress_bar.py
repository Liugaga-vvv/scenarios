from time import sleep
from tqdm import tqdm
from typing import Any, List

def custom_progress_bar(iterable: List[any], desc: str = "processing") -> None:
    # obtain the total number of iterations and set initial variables
    total_iterations = len(iterable)
    avg_time_per_iteration = 0

    # initializing tqdm with settings for the progress bar and entering a for loop over the "iterable"
    with tqdm(total=total_iterations, desc=desc, dynamic_ncols=True, 
              bar_format="{l_bar}{bar}{n}/{total} [{elapsed}<{remaining}]") as pbar:
        for i, item in enumerate(iterable):
            start_time = pbar.format_dict["elapsed"] # starting/obtaining the elapsed time since the instance was created
            sleep(item)  # sleep for `item` seconds simulating processing item
            pbar.update(1) # update one iteration progress on progressbar
            elapsed_time = pbar.format_dict["elapsed"] - start_time # calculate elapsed time
 
            # average time per iteration calculation:
            # old_time_calculated_using_previous_iteration_times * no_of_iterations + this_elapsedtime / (no_of_iterations + 1)
            avg_time_per_iteration = ((avg_time_per_iteration * i) + elapsed_time) / (i + 1)
            pbar.set_postfix_str(  # postfix string shows eta (estimated time of arrival)
                f"eta: {avg_time_per_iteration * (total_iterations - (i + 1)):.2f}s", refresh=True) 

tasks = [1, 2, 3, 2, 1] # a list of tasks, used to call the custom progress bar function
custom_progress_bar(tasks, desc="sub-challenge 1") # calling the function and passing its parameters.
