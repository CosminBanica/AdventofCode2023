"""
Solver for day 14: Parabolic Reflector Dish
"""
from copy import deepcopy
from src.day_management.day_solver import DaySolver


class Day14Solver(DaySolver):
    """
    Solver for day 14: Parabolic Reflector Dish
    """

    def __init__(self, input_data):
        super().__init__(input_data)
        self.initial_grid = self.get_grid_from_input()
        self.grid = deepcopy(self.initial_grid)

    def get_grid_from_input(self):
        """
        Returns a grid from the input data
        """
        grid = []
        for line in self.input_data:
            grid.append(list(line))
        return grid

    def roll_rocks_north(self):
        """
        Rolls all 'O' rocks as far north as possible
        """
        for i, row in enumerate(self.grid):
            for j in range(len(self.grid[i])):
                if row[j] == "O":
                    k = i - 1
                    while k >= 0 and self.grid[k][j] == ".":
                        self.grid[k][j] = "O"
                        self.grid[k + 1][j] = "."
                        k -= 1

    def roll_rocks_south(self):
        """
        Rolls all 'O' rocks as far south as possible
        """
        for i in range(len(self.grid) - 1, -1, -1):
            for j in range(len(self.grid[i])):
                if self.grid[i][j] == "O":
                    k = i + 1
                    while k < len(self.grid) and self.grid[k][j] == ".":
                        self.grid[k][j] = "O"
                        self.grid[k - 1][j] = "."
                        k += 1

    def roll_rocks_east(self):
        """
        Rolls all 'O' rocks as far east as possible
        """
        for j in range(len(self.grid[0]) - 1, -1, -1):
            for i, row in enumerate(self.grid):
                if row[j] == "O":
                    k = j + 1
                    while k < len(self.grid[0]) and row[k] == ".":
                        self.grid[i][k] = "O"
                        self.grid[i][k - 1] = "."
                        k += 1

    def roll_rocks_west(self):
        """
        Rolls all 'O' rocks as far west as possible
        """
        for j in range(len(self.grid[0])):
            for i, row in enumerate(self.grid):
                if row[j] == "O":
                    k = j - 1
                    while k >= 0 and row[k] == ".":
                        self.grid[i][k] = "O"
                        self.grid[i][k + 1] = "."
                        k -= 1

    def roll_rocks(self):
        """
        Rolls all 'O' once in all directions
        """
        self.roll_rocks_north()
        self.roll_rocks_west()
        self.roll_rocks_south()
        self.roll_rocks_east()

    def solve_part_one(self):
        """
        Solves part one
        """
        # The load of a rock is determined by its vertical distance to the bottom of the grid
        rock_load_sum = 0

        # First roll all 'O' rocks as far north as possible;
        # they can pass through empty tiles '.', but not through walls '#' or other 'O' rocks
        self.roll_rocks_north()

        # Then, for each rock, calculate its load and add it to the sum
        for i, row in enumerate(self.grid):
            for _, tile in enumerate(row):
                if tile == "O":
                    rock_load_sum += len(self.grid) - i

        self.grid = deepcopy(self.initial_grid)
        return rock_load_sum

    def solve_part_two(self):
        """
        Solves part two
        """
        rock_load_sum = 0
        nr_iterations = 1000000000

        # Since we're doing this for so many iterations, perform cycle detection
        # If we detect a cycle, we can skip the remaining iterations
        cycle_detected = False
        cycle_length = 0
        cycle_grids = [deepcopy(self.grid)]

        i = 0
        while i < nr_iterations:
            self.roll_rocks()
            i += 1
            if self.grid in cycle_grids:
                cycle_detected = True
                cycle_length = i - cycle_grids.index(self.grid)
                break
            cycle_grids.append(deepcopy(self.grid))

        if cycle_detected:
            # We can skip the remaining iterations
            nr_iterations = (nr_iterations - i) % cycle_length

        for i in range(nr_iterations):
            self.roll_rocks()

        for i, row in enumerate(self.grid):
            for _, tile in enumerate(row):
                if tile == "O":
                    rock_load_sum += len(self.grid) - i

        return rock_load_sum
