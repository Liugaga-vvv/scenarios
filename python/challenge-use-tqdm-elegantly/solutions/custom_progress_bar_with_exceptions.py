from time import sleep
from tqdm import tqdm
from typing import Any, List

def custom_progress_bar_with_exceptions(iterable: List[Any], desc: str = "Processing") -> None:
    total_iterations = len(iterable)
    avg_time_per_iteration = 0

    # Initializes a progress bar with appropriate settings and formats.
    with tqdm(total=total_iterations, desc=desc, dynamic_ncols=True, bar_format="{l_bar}{bar}{n}/{total} [{elapsed}<{remaining}]") as pbar:

        # Loops through each item in iterable.
        for i, item in enumerate(iterable):
            start_time = pbar.format_dict["elapsed"]

            try:
                sleep(item)  # Simulating the processing of the item
            except KeyboardInterrupt:
                print("\nInterrupted by user. Exiting...")
                pbar.close()
                break
            
            # catches other exceptions
            except Exception as e:
                print(f"\nAn error occurred: {e}. Skipping this iteration.")
                
                # Writes an additional message to the progress bar. 
                pbar.write("Skipping the current iteration.")
                
                pbar.update(1)
                continue

            # Completes each iteration, updating the progress bar along each loop.
            pbar.update(1)
            
            elapsed_time = pbar.format_dict["elapsed"] - start_time

            avg_time_per_iteration = (
                (avg_time_per_iteration * i) + elapsed_time) / (i + 1)
            # Adjusts the final output of progress by adding an ETA.
            pbar.set_postfix_str(
                f"ETA: {avg_time_per_iteration * (total_iterations - (i + 1)):.2f}s", refresh=True)

# Example usage
tasks = [1, 2, 3, 2, 1]
custom_progress_bar_with_exceptions(tasks, desc="Sub-Challenge 3")