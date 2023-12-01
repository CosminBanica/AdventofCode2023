"""
Solver for day 1: Trebuchet?!
"""
from src.day_management.day_solver import DaySolver

ACCEPTED_DIGITS = [
    "0",
    "1",
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
    "8",
    "9",
    "zero",
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine",
]

SPELLED_DIGITS = {
    "zero": 0,
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}


def get_first_real_digit(line):
    """
    Gets the first digit of a line
    """
    for i, char in enumerate(line):
        if char.isdigit():
            return int(char)
        if char.isalpha():
            if line[i : i + 3] in ACCEPTED_DIGITS:
                return SPELLED_DIGITS[line[i : i + 3]]
            if line[i : i + 4] in ACCEPTED_DIGITS:
                return SPELLED_DIGITS[line[i : i + 4]]
            if line[i : i + 5] in ACCEPTED_DIGITS:
                return SPELLED_DIGITS[line[i : i + 5]]

    return 0


def get_last_real_digit(line):
    """
    Gets the first digit of a line
    """
    for i in range(len(line)):
        backwards_index = len(line) - i - 1
        if line[backwards_index].isdigit():
            return int(line[backwards_index])
        if line[backwards_index].isalpha():
            if line[backwards_index - 2 : backwards_index + 1] in ACCEPTED_DIGITS:
                return SPELLED_DIGITS[line[backwards_index - 2 : backwards_index + 1]]
            if line[backwards_index - 3 : backwards_index + 1] in ACCEPTED_DIGITS:
                return SPELLED_DIGITS[line[backwards_index - 3 : backwards_index + 1]]
            if line[backwards_index - 4 : backwards_index + 1] in ACCEPTED_DIGITS:
                return SPELLED_DIGITS[line[backwards_index - 4 : backwards_index + 1]]

    return 0


class Day1Solver(DaySolver):
    """
    Solver for day 1: Trebuchet?!
    """

    def solve_part_one(self):
        """
        Solves part one of the day's puzzle.
        """
        numbers_found = []

        for line in self.input_data:
            number = 0
            found_first = False
            found_last = False
            i = 0

            # Find first and last digit of the line
            while i < len(line) and (not found_first or not found_last):
                if line[i].isdigit() and not found_first:
                    number = number + int(line[i]) * 10
                    found_first = True
                if line[len(line) - i - 1].isdigit() and not found_last:
                    number = number + int(line[len(line) - i - 1])
                    found_last = True
                i += 1
            numbers_found.append(number)

        return sum(numbers_found)

    def solve_part_two(self):
        """
        Solves part two of the day's puzzle.
        """
        numbers_found = []

        for line in self.input_data:
            number = get_first_real_digit(line) * 10
            number = number + get_last_real_digit(line)
            numbers_found.append(number)

        return sum(numbers_found)
