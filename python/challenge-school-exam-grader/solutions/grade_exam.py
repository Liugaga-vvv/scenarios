# This script imports the time module and defines a function that takes in a list of exam scores.
import time


def grade_exam(exam_scores):
    # Create a dictionary to store the grade counts.
    grade_dict = {"A": 0, "B": 0, "C": 0, "D": 0, "F": 0}

    # Iterate over each exam score in the input list and update the grade counts accordingly.
    for score in exam_scores:
        if score >= 90:
            grade_dict["A"] += 1
        elif score >= 80:
            grade_dict["B"] += 1
        elif score >= 70:
            grade_dict["C"] += 1
        elif score >= 60:
            grade_dict["D"] += 1
        else:
            grade_dict["F"] += 1

    # Add the current date to the grade dictionary.
    grade_dict["date"] = time.strftime("%m/%d/%Y")

    # Return the grade dictionary.
    return grade_dict
