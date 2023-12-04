"""
Solver for day 3: Gear Ratios
"""
from src.day_management.day_solver import DaySolver


class Day3Solver(DaySolver):
    """
    Solver for day 3: Gear Ratios
    """

    def __init__(self, input_data):
        super().__init__(input_data)
        self.map = []
        self.gears = {}
        self.parse_input()

    def get_map_width(self):
        """
        Gets the width of the map
        """
        return len(self.map[0])

    def get_map_height(self):
        """
        Gets the height of the map
        """
        return len(self.map)

    def parse_input(self):
        """
        Parses the input data
        """
        for i, line in enumerate(self.input_data):
            symbols = []
            for j, symbol in enumerate(line):
                symbols.append(symbol)
                if symbol == "*":
                    self.gears[(i, j)] = []

            self.map.append(symbols)

    def is_symbol_around_position(self, i, j, number):
        """
        Checks if there is a symbol around the given position
        """
        nearby_positions = [
            (i - 1, j),
            (i - 1, j - 1),
            (i - 1, j + 1),
            (i, j - 1),
            (i, j + 1),
            (i + 1, j),
            (i + 1, j - 1),
            (i + 1, j + 1),
        ]

        for nearby_position in nearby_positions:
            if (
                0 <= nearby_position[0] < self.get_map_height()
                and 0 <= nearby_position[1] < self.get_map_width()
                and self.map[nearby_position[0]][nearby_position[1]] != "."
                and (not self.map[nearby_position[0]][nearby_position[1]].isdigit())
            ):
                if self.map[nearby_position[0]][nearby_position[1]] == "*":
                    self.gears[nearby_position].append(number)
                return True

        return False

    def is_symbol_around_number(self, i, number_start, number_end, number):
        """
        Checks if there is a symbol around the given position
        """
        for j in range(number_start, number_end + 1):
            if self.is_symbol_around_position(i, j, number):
                return True

        return False

    def solve_part_one(self):
        """
        Solves part one
        """
        numbers_sum = 0
        for i, line in enumerate(self.map):
            j = 0
            while j < self.get_map_width():
                if line[j].isdigit():
                    last_digit_position = j
                    number = 0

                    while (
                        last_digit_position < self.get_map_width()
                        and line[last_digit_position].isdigit()
                    ):
                        number *= 10
                        number += int(line[last_digit_position])
                        last_digit_position += 1

                    last_digit_position -= 1

                    if self.is_symbol_around_number(i, j, last_digit_position, number):
                        numbers_sum += number

                    j = last_digit_position

                j += 1

        return numbers_sum

    def solve_part_two(self):
        """
        Solves part two
        """
        gear_ratio_sum = 0

        for gear in self.gears.items():
            if len(gear[1]) == 2:
                gear_ratio_sum += gear[1][0] * gear[1][1]

        return gear_ratio_sum
