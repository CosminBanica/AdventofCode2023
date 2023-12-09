"""
Solver for day 6: Wait For It
"""
import math
from src.day_management.day_solver import DaySolver


def return_possible_solutions(a, b, c):
    """
    Solves the equation ax^2 + bx + c = 0, limited to the range [1, b - 1],
    and returns the number of solutions
    """
    discriminant = b**2 - 4 * a * c
    solution1 = int(math.ceil((-b + math.sqrt(discriminant)) / (2 * a)))
    solution2 = int(math.floor((-b - math.sqrt(discriminant)) / (2 * a)))

    smallest_solution = min(solution1, solution2)
    largest_solution = max(solution1, solution2)
    if smallest_solution <= 0:
        smallest_solution = 1
    if largest_solution >= b:
        largest_solution = b - 1
    ways_to_win = largest_solution - smallest_solution + 1
    return ways_to_win


class Day6Solver(DaySolver):
    """
    Solver for day 6: Wait For It
    """

    def __init__(self, input_data):
        super().__init__(input_data)
        self.races = []
        times, record_distances = list(
            map(lambda x: x.split(":")[1].strip().split(" "), input_data)
        )
        times = list(filter(lambda x: x != "", times))
        record_distances = list(filter(lambda x: x != "", record_distances))
        self.races = list(
            map(lambda x: (int(x[0]), int(x[1])), zip(times, record_distances))
        )
        self.times_united = int("".join(times))
        self.record_distances_united = int("".join(record_distances))

    def solve_part_one(self):
        """
        Solves part one
        """
        ways_to_win_product = 1
        for race_time, race_record_distance in self.races:
            ways_to_win = return_possible_solutions(
                -1, race_time, -1 * (race_record_distance + 1)
            )
            ways_to_win_product *= ways_to_win

        return ways_to_win_product

    def solve_part_two(self):
        """
        Solves part two
        """
        ways_to_win = return_possible_solutions(
            -1, self.times_united, -1 * (self.record_distances_united + 1)
        )
        return ways_to_win
