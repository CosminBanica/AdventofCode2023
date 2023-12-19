"""
Solver for day 18: Lavaduct Lagoon
"""
from src.day_management.day_solver import DaySolver


DIRECTION_TO_VECTOR = {
    "R": (0, 1),
    "D": (1, 0),
    "L": (0, -1),
    "U": (-1, 0),
}

DIGIT_TO_DIRECTION = {
    "0": "R",
    "1": "D",
    "2": "L",
    "3": "U",
}


class Day18Solver(DaySolver):
    """
    Solver for day 18: Lavaduct Lagoon
    """

    def __init__(self, input_data):
        super().__init__(input_data)
        self.steps = []
        self.true_steps = []
        for line in input_data:
            direction, nr, color = line.strip().split()
            nr = int(nr)
            self.steps.append((direction, nr))

            true_nr = color[2:7]
            true_dir = color[7]
            true_nr = int(true_nr, 16)
            true_dir = DIGIT_TO_DIRECTION[true_dir]
            self.true_steps.append((true_dir, true_nr))

    def solve_part_one(self):
        """
        Solves part one
        """
        curr_pos = (0, 0)
        area = 0
        perimeter = 0

        for step in self.steps:
            direction, nr = step
            vector = DIRECTION_TO_VECTOR[direction]
            vector = (vector[0] * nr, vector[1] * nr)
            curr_pos = (curr_pos[0] + vector[0], curr_pos[1] + vector[1])
            perimeter += nr
            area += curr_pos[1] * vector[0]

        return area + perimeter // 2 + 1

    def solve_part_two(self):
        """
        Solves part two
        """
        curr_pos = (0, 0)
        area = 0
        perimeter = 0

        for step in self.true_steps:
            direction, nr = step
            vector = DIRECTION_TO_VECTOR[direction]
            vector = (vector[0] * nr, vector[1] * nr)
            curr_pos = (curr_pos[0] + vector[0], curr_pos[1] + vector[1])
            perimeter += nr
            area += curr_pos[1] * vector[0]

        return area + perimeter // 2 + 1
