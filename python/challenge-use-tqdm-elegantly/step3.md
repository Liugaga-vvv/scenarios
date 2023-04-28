# Exception Handling and Graceful Exit

In this sub-challenge, you will add exception handling and graceful exit capabilities to your custom tqdm progress bar. This will allow the progress bar to handle errors and interruptions without causing the entire program to crash.

## Example

```python
tasks = [1, 2, 3, 2, 1]
custom_progress_bar_with_exceptions(tasks, desc="process 3")
```

## TODO

- Complete `custom_progress_bar_with_exceptions.py`

## Requirements

- Add exception handling to your custom tqdm progress bar from Sub-Challenge 1.
- Implement a graceful exit strategy, allowing the progress bar to close properly when an error or interruption occurs.
- Test your progress bar with various types of errors and interruptions, ensuring that it handles them correctly and exits gracefully.
