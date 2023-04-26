# Nested Progress Bars with Dynamic Labels

In this sub-challenge, you will create nested progress bars to track the progress of a task with multiple sub-tasks. The progress bars should display dynamic labels, indicating the current sub-task being executed.

## Example usage

```python
tasks = [[1, 2], [2, 1, 3], [1, 1]]
nested_progress_bars(tasks)
```

## TODO

- Complete `nested_progress_bars.py`

## Requirements

- Create two nested tqdm progress bars, with the outer progress bar tracking the main task and the inner progress bar tracking the sub-tasks.
- Implement dynamic labels for both progress bars, indicating the current iteration and sub-task.
- Ensure that the progress bars update correctly, displaying the progress of both the main task and the sub-tasks.
