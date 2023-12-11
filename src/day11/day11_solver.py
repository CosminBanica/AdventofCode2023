"""
Solver for day 11: Cosmic Expansion
"""
from src.day_management.day_solver import DaySolver


class Day11Solver(DaySolver):
    """
    Solver for day 11: Cosmic Expansion
    """

    def __init__(self, input_data):
        super().__init__(input_data)
        self.original_map = [list(line) for line in self.input_data]
        self.expanded_map = self.get_expanded_map()
        self.galaxies = []
        self.original_galaxies = []

        for i, line in enumerate(self.original_map):
            for j, _ in enumerate(line):
                if self.original_map[i][j] == "#":
                    self.original_galaxies.append((i, j))
        for i, line in enumerate(self.expanded_map):
            for j, _ in enumerate(line):
                if self.expanded_map[i][j] == "#":
                    self.galaxies.append((i, j))
        self.empty_rows = set(
            row
            for row in range(len(self.original_map))
            if "#" not in self.original_map[row]
        )
        self.empty_columns = set(
            column
            for column in range(len(self.original_map[0]))
            if all(
                self.original_map[row][column] != "#"
                for row in range(len(self.original_map))
            )
        )

    def get_expanded_map(self):
        """
        Expands the map to 1000x1000
        """
        expanded_map = []

        # For each line which has no # in it, add it twice
        for line in self.original_map:
            expanded_map.append(line.copy())
            if "#" not in line:
                expanded_map.append(line.copy())
                continue

        # For each column which has no # in it, insert and identical column, right next to it
        i = 0
        while i < len(expanded_map[0]):
            if all(line[i] != "#" for line in expanded_map):
                for line in expanded_map:
                    line.insert(i, ".")
                i += 1
            i += 1

        return expanded_map

    def solve_part_one(self):
        """
        Solves part one
        """
        distances_between_galaxies_sum = 0

        for i, galaxy in enumerate(self.galaxies):
            for j in range(i + 1, len(self.galaxies)):
                distance = abs(galaxy[0] - self.galaxies[j][0]) + abs(
                    galaxy[1] - self.galaxies[j][1]
                )
                distances_between_galaxies_sum += distance

        return distances_between_galaxies_sum

    def solve_part_two(self):
        """
        Solves part two
        """
        distances_between_galaxies_sum = 0

        for i, galaxy in enumerate(self.original_galaxies):
            for j in range(i + 1, len(self.original_galaxies)):
                x1, y1 = galaxy
                x2, y2 = self.original_galaxies[j]

                distances_between_galaxies_sum += abs(x1 - x2) + abs(y1 - y2)

                rows_between = (
                    set(range(x1, x2 + 1)) if x1 < x2 else set(range(x2, x1 + 1))
                )
                columns_between = (
                    set(range(y1, y2 + 1)) if y1 < y2 else set(range(y2, y1 + 1))
                )

                distances_between_galaxies_sum += len(
                    self.empty_rows & rows_between
                ) * (1000000 - 1)
                distances_between_galaxies_sum += len(
                    self.empty_columns & columns_between
                ) * (1000000 - 1)

        return distances_between_galaxies_sum
