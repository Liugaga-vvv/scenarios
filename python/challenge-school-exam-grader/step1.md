# School Exam Grader

Write a Python function called `grade_exam` that takes a list of student exam scores as input and returns a dictionary with the current date and the grade distribution. The input list will contain integers between 0 and 100, representing the exam scores of students.

The grade distribution should be as follows:

- A: 90-100
- B: 80-89
- C: 70-79
- D: 60-69
- F: 0-59

## Example Usage

```python
exam_scores = [85, 92, 78, 65, 90, 100, 70, 75, 82, 95]

grade_dict = grade_exam(exam_scores)

print(grade_dict) # Output: {'A': 4, 'B': 2, 'C': 3, 'D': 1, 'F': 0, 'date': '04/18/2023'}
```

## TODO

- Complete `grade_exam.py`

## Requirements

- The `grade_exam` function should take a single argument (the list of exam scores).
- The `grade_exam` function should return a dictionary with keys `"date"`, `"A"`, `"B"`, `"C"`, `"D"`, and `"F"`, and values representing the number of students who received each grade.
- If no students received a particular grade, the corresponding value in the output dictionary should be 0.
