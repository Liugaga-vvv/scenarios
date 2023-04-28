# Custom Progress Bar with Dynamic Time Estimation

In this sub-challenge, you will create a custom progress bar that shows the estimated time remaining for the completion of a task, based on the average time taken by previous iterations. The progress bar should update dynamically, recalculating the estimated time remaining after each iteration.

## Example

```python
tasks = [1, 2, 3, 2, 1]
custom_progress_bar(tasks, desc="process 1")
```

## TODO

- Complete `custom_progress_bar.py`

## Requirements

- Create a custom tqdm progress bar that calculates the average time per iteration and estimates the remaining time for completion.
- Implement the progress bar in a loop with varying iteration durations.
- Make sure that the progress bar updates dynamically, displaying the recalculated estimated remaining time after each iteration.
