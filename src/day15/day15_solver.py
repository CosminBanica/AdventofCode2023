"""
Solver for day 15: Lens Library
"""
from src.day_management.day_solver import DaySolver


def get_hash(string):
    """
    Gets the hash of a string
    """

    current_value = 0
    for char in string:
        current_value = ((current_value + ord(char)) * 17) % 256

    return current_value


class Day15Solver(DaySolver):
    """
    Solver for day 15: Lens Library
    """

    def __init__(self, input_data):
        super().__init__(input_data)
        self.steps = input_data[0].strip().split(",")
        self.hash_table = {}
        for i in range(256):
            self.hash_table[i] = []

    def solve_part_one(self):
        """
        Solves part one
        """
        hash_sum = 0

        for step in self.steps:
            hashed_step = get_hash(step)
            hash_sum += hashed_step

        return hash_sum

    def solve_part_two(self):
        """
        Solves part two
        """
        focusing_power = 0

        for step in self.steps:
            if step[len(step) - 1] != "-":
                string, focal_length = step.split("=")
                focal_length = int(focal_length)
                hashed_string = get_hash(string)

                for i, item in enumerate(self.hash_table[hashed_string]):
                    if item[0] == string:
                        self.hash_table[hashed_string][i] = (string, focal_length)
                        break
                else:
                    self.hash_table[hashed_string].append((string, focal_length))
            else:
                string = step[: len(step) - 1]
                hashed_string = get_hash(string)

                focal_length = -1
                for item in self.hash_table[hashed_string]:
                    if item[0] == string:
                        focal_length = item[1]
                if focal_length != -1:
                    self.hash_table[hashed_string].remove((string, focal_length))

        for key, value in self.hash_table.items():
            for i, item in enumerate(value):
                focusing_power += (1 + key) * (1 + i) * item[1]

        return focusing_power
