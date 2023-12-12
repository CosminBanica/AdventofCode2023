"""
Solver for day 12: Hot Springs
"""
from src.day_management.day_solver import DaySolver


class Day12Solver(DaySolver):
    """
    Solver for day 12: Hot Springs
    """

    def __init__(self, input_data):
        super().__init__(input_data)
        self.rows = []
        self.unfolded_rows = []
        self.cache = {}
        for line in self.input_data:
            row, contiguous_damaged = line.split(" ")
            row = list(row)
            contiguous_damaged = contiguous_damaged.split(",")
            contiguous_damaged = [int(x) for x in contiguous_damaged]
            self.rows.append((row, contiguous_damaged))

            # Unfolded row is the row repeated 5 times, with a '?' between each repetition
            unfolded_row = []
            for i in range(5):
                unfolded_row += row
                if i < 4:
                    unfolded_row.append("?")

            # Unfolded contiguous_damaged is the contiguous_damaged list repeated 5 times
            unfolded_contiguous_damaged = []
            for i in range(5):
                unfolded_contiguous_damaged += contiguous_damaged

            self.unfolded_rows.append((unfolded_row, unfolded_contiguous_damaged))

    def get_possible_arrangements_optimized(self, row, contiguous_damaged, cache_key):
        """
        Returns the number of possible arrangements of damaged tiles in the row.
        """
        row_i, contiguous_i, current_contiguous_length = cache_key
        if cache_key in self.cache:
            return self.cache[cache_key]

        if row_i == len(row):
            if (
                contiguous_i == len(contiguous_damaged)
                and current_contiguous_length == 0
            ):
                return 1
            if (
                contiguous_i == len(contiguous_damaged) - 1
                and contiguous_damaged[contiguous_i] == current_contiguous_length
            ):
                return 1
            return 0

        possible_arrangements_no = 0
        for wildcard in [".", "#"]:
            if row[row_i] == wildcard or row[row_i] == "?":
                if wildcard == "." and current_contiguous_length == 0:
                    possible_arrangements_no += (
                        self.get_possible_arrangements_optimized(
                            row, contiguous_damaged, (row_i + 1, contiguous_i, 0)
                        )
                    )
                elif (
                    wildcard == "."
                    and current_contiguous_length > 0
                    and contiguous_i < len(contiguous_damaged)
                    and contiguous_damaged[contiguous_i] == current_contiguous_length
                ):
                    possible_arrangements_no += (
                        self.get_possible_arrangements_optimized(
                            row, contiguous_damaged, (row_i + 1, contiguous_i + 1, 0)
                        )
                    )
                elif wildcard == "#":
                    possible_arrangements_no += (
                        self.get_possible_arrangements_optimized(
                            row,
                            contiguous_damaged,
                            (
                                row_i + 1,
                                contiguous_i,
                                current_contiguous_length + 1,
                            ),
                        )
                    )

        self.cache[cache_key] = possible_arrangements_no
        return possible_arrangements_no

    def solve_part_one(self):
        """
        Solves part one
        """
        possible_arrangements_sum = 0
        for row, contiguous_damaged in self.rows:
            self.cache = {}
            possible_arrangements_no = self.get_possible_arrangements_optimized(
                row, contiguous_damaged, (0, 0, 0)
            )
            possible_arrangements_sum += possible_arrangements_no

        return possible_arrangements_sum

    def solve_part_two(self):
        """
        Solves part two
        """
        possible_arrangements_sum = 0
        for row, contiguous_damaged in self.unfolded_rows:
            self.cache = {}
            possible_arrangements_no = self.get_possible_arrangements_optimized(
                row, contiguous_damaged, (0, 0, 0)
            )
            possible_arrangements_sum += possible_arrangements_no
        return possible_arrangements_sum
