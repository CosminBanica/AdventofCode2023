"""
Solver for day 9: Mirage Maintenance
"""
from src.day_management.day_solver import DaySolver


def are_all_new_differences_zero(current_differences):
    """
    Checks if all new differences are zero, and also returns them
    """
    new_differences = []
    all_zeroes = True

    for i in range(len(current_differences) - 1):
        first, second = current_differences[i], current_differences[i + 1]
        difference = second - first
        if difference != 0:
            all_zeroes = False
        new_differences.append(difference)

    return all_zeroes, new_differences


class Day9Solver(DaySolver):
    """
    Solver for day 9: Mirage Maintenance
    """

    def __init__(self, input_data):
        super().__init__(input_data)
        self.histories = []
        for line in input_data:
            numbers = line.strip().split(" ")
            numbers = [int(number) for number in numbers]
            self.histories.append(numbers)

    def solve_part_one(self):
        """
        Solves part one
        """
        extrapolated_numbers_sum = 0

        for history in self.histories:
            current_differences = history
            last_difference_sum = 0
            all_zeroes = False

            while not all_zeroes:
                last_difference_sum += current_differences[-1]

                all_zeroes, new_differences = are_all_new_differences_zero(
                    current_differences
                )

                current_differences = new_differences

            extrapolated_numbers_sum += last_difference_sum

        return extrapolated_numbers_sum

    def solve_part_two(self):
        """
        Solves part two
        """
        extrapolated_numbers_sum = 0

        for history in self.histories:
            current_differences = history
            first_differences = []
            all_zeroes = False

            while not all_zeroes:
                first_differences.append(current_differences[0])

                all_zeroes, new_differences = are_all_new_differences_zero(
                    current_differences
                )

                current_differences = new_differences

            extrapolated_first_number = 0
            for i in range(len(first_differences) - 1, -1, -1):
                extrapolated_first_number = (
                    first_differences[i] - extrapolated_first_number
                )

            extrapolated_numbers_sum += extrapolated_first_number

        return extrapolated_numbers_sum
