## Step 3 Solution

```python
def get_grade(score: int) -> str:
    """
    Calculates the grade of a student based on their score.

    Args:
    score (int): The score of the student.

    Returns:
    str: The grade of the student ('A', 'B', 'C', 'D', or 'E').
    """
    grades = {90: 'A', 80: 'B', 70: 'C', 60: 'D', 0: 'E'}
    return grades.get(next(key for key in grades if score >= key), 'E')
```
