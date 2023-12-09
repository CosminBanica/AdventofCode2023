"""
Entry point for Advent of Code 2023
"""
import time
import argparse
import sys
from config import constants
from src.day_management.day_picker import get_day_solver
from src.day_management.day_files_generator import generate_day


def get_args():
    """
    Gets the command line arguments
    """
    parser = argparse.ArgumentParser(description="Advent of Code 2023")
    parser.add_argument(
        "day", type=int, help="the day to solve [1-25]", choices=range(1, 26)
    )
    parser.add_argument(
        "-t",
        "--test",
        help="run the solver in test mode",
        action="store_true",
        default=False,
    )
    parser.add_argument(
        "-g",
        "--generate",
        help="generate the files for the day",
        action="store_true",
        default=False,
    )
    parser.add_argument(
        "-n",
        "--name",
        help="the name of the day's problem",
        type=str,
        default="",
    )

    args = parser.parse_args()
    return args


if __name__ == "__main__":
    ARGS = get_args()

    if ARGS.generate:
        generate_day(ARGS.day, ARGS.name)
        sys.exit(0)

    INPUT_PATH = ""
    if ARGS.test:
        INPUT_PATH = f"src/day{ARGS.day}/{constants.SMALL_IN}"
    else:
        INPUT_PATH = f"src/day{ARGS.day}/{constants.BIG_IN}"

    day_solver = get_day_solver(ARGS.day, INPUT_PATH)

    if day_solver is None:
        print("No solver found for day " + str(ARGS.day))
        sys.exit(1)

    print("Starting task 1")
    start = time.time()
    RESULT = day_solver.solve_part_one()
    print("Task 1 result: " + str(RESULT))
    end = time.time()
    print("Exec time" + str(end - start))

    print("\nStarting task 2")
    start = time.time()
    RESULT = day_solver.solve_part_two()
    print("Task 2 result: " + str(RESULT))
    end = time.time()
    print("Exec time" + str(end - start))
