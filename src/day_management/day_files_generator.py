"""
Auto-generate the files for a new day, and add them to the day picker
"""
import os
from config.day_template import DAY_TEMPLATE

CURRENT_DIR = os.path.dirname(os.path.realpath(__file__))
DAY_PICKER_PATH = CURRENT_DIR + "/day_picker.py"


def generate_day_solver(day, name):
    """
    Generates the day solver
    """
    day_solver_path = CURRENT_DIR + f"/../day{day}/day{day}_solver.py"
    if os.path.exists(day_solver_path):
        print(f"Day {day} solver already exists")
        return

    with open(day_solver_path, "w", encoding="utf-8") as day_solver_file:
        day_solver_file.write(DAY_TEMPLATE.substitute(day=day, name=name))

    print(f"Day {day} solver created")


def create_input_files(day):
    """
    Creates the input files for the day
    """
    small_in_path = CURRENT_DIR + f"/../day{day}/small_input.txt"
    big_in_path = CURRENT_DIR + f"/../day{day}/input.txt"
    if os.path.exists(small_in_path):
        print(f"Small input file for day {day} already exists")
    else:
        with open(small_in_path, "w", encoding="utf-8") as small_in_file:
            small_in_file.write("")
        print(f"Small input file for day {day} created")

    if os.path.exists(big_in_path):
        print(f"Big input file for day {day} already exists")
    else:
        with open(big_in_path, "w", encoding="utf-8") as big_in_file:
            big_in_file.write("")
        print(f"Big input file for day {day} created")


def add_day_to_picker(day):
    """
    Adds the day to the day picker
    """
    with open(DAY_PICKER_PATH, "r", encoding="utf-8") as day_picker_file:
        lines = day_picker_file.readlines()

    if f"from src.day{day}.day{day}_solver import Day{day}Solver\n" in lines:
        print(f"Day {day} solver already imported")
    else:
        for i, line in enumerate(lines):
            if line.startswith("from"):
                lines.insert(
                    i, f"from src.day{day}.day{day}_solver import Day{day}Solver\n"
                )
                break
        print(f"Day {day} solver imported")

    if f"    {day}: Day{day}Solver,\n" in lines:
        print(f"Day {day} already in day solver map")
    else:
        for i, line in enumerate(lines):
            if line.startswith("day_solver_map = {"):
                lines.insert(i + 1, f"    {day}: Day{day}Solver,\n")
                break
        print(f"Day {day} added to day solver map")

    with open(DAY_PICKER_PATH, "w", encoding="utf-8") as day_picker_file:
        day_picker_file.writelines(lines)


def generate_day(day, name):
    """
    Generates the files for a new day
    """
    if not os.path.exists(CURRENT_DIR + f"/../day{day}"):
        os.mkdir(CURRENT_DIR + f"/../day{day}")

    generate_day_solver(day, name)
    create_input_files(day)
    add_day_to_picker(day)
