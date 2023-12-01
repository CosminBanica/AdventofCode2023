"""
This module contains the DayPicker class.
"""
from src.day1.day1_solver import Day1Solver


def get_input_data(input_file_path):
    """
    Returns the input data from the input file
    """
    input_data = []
    with open(input_file_path, "r", encoding="utf-8") as input_file:
        for line in input_file:
            input_data.append(line.strip())
    return input_data


def get_day_solver(day, input_file_path):
    """
    Returns the day class based on the day number
    """
    if day == 1:
        return Day1Solver(get_input_data(input_file_path))

    return None
