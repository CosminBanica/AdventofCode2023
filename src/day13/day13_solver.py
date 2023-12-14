"""
Solver for day 13: Point of Incidence
"""
from src.day_management.day_solver import DaySolver


def is_vertical_line_of_reflection(pattern, i):
    """
    Checks if the column at index i is a vertical line of reflection
    """
    start = i
    symmetrical = i + 1

    # Keep checking if the columns are identical, until the end of pattern
    while symmetrical < len(pattern[0]) and start > -1:
        for _, row in enumerate(pattern):
            if row[start] != row[symmetrical]:
                return False
        start -= 1
        symmetrical += 1

    return True


def is_horizontal_line_of_reflection(pattern, i):
    """
    Checks if the line at index i is a horizontal line of reflection
    """
    start = i
    symmetrical = i + 1

    # Keep checking if the lines are identical, until the end of pattern
    while symmetrical < len(pattern) and start > -1:
        if pattern[start] != pattern[symmetrical]:
            return False
        start -= 1
        symmetrical += 1

    return True


def is_vertical_line_of_reflection_with_smudge(pattern, i):
    """
    Checks if the column at index i is a vertical line of reflection
    """
    start = i
    symmetrical = i + 1
    number_of_smudges = 0

    # Keep checking if the columns are identical, until the end of pattern
    while symmetrical < len(pattern[0]) and start > -1:
        for _, row in enumerate(pattern):
            if row[start] != row[symmetrical]:
                number_of_smudges += 1
                if number_of_smudges > 1:
                    return False
        start -= 1
        symmetrical += 1

    if number_of_smudges == 1:
        return True

    return False


def is_horizontal_line_of_reflection_with_smudge(pattern, i):
    """
    Checks if the line at index i is a horizontal line of reflection with one smudge
    """
    start = i
    symmetrical = i + 1
    number_of_smudges = 0

    # Keep checking if the lines are identical, until the end of pattern
    while symmetrical < len(pattern) and start > -1:
        for j in range(len(pattern[0])):
            if pattern[start][j] != pattern[symmetrical][j]:
                number_of_smudges += 1
                if number_of_smudges > 1:
                    return False

        start -= 1
        symmetrical += 1

    if number_of_smudges == 1:
        return True

    return False


class Day13Solver(DaySolver):
    """
    Solver for day 13: Point of Incidence
    """

    def __init__(self, input_data):
        super().__init__(input_data)
        self.patterns = []
        pattern = []
        for line in self.input_data:
            if line.strip() == "":
                self.patterns.append(pattern)
                pattern = []
            else:
                pattern.append(line)
        self.patterns.append(pattern)

    def solve_part_one(self):
        """
        Solves part one
        """
        horizontal_lines_of_reflection_indices = []
        vertical_lines_of_reflection_indices = []

        for pattern in self.patterns:
            # First check if there is a horizontal line of reflection,
            # by seeing if two consecutive lines are the same
            for i in range(len(pattern) - 1):
                if pattern[i] == pattern[i + 1]:
                    if is_horizontal_line_of_reflection(pattern, i):
                        horizontal_lines_of_reflection_indices.append(i + 1)
                        break
            else:
                # If there is no horizontal line of reflection,
                # check if there is a vertical line of reflection
                for i in range(len(pattern[0]) - 1):
                    for _, row in enumerate(pattern):
                        if row[i] != row[i + 1]:
                            break
                    else:
                        if is_vertical_line_of_reflection(pattern, i):
                            vertical_lines_of_reflection_indices.append(i + 1)
                            break

        mirrors_sum = sum(vertical_lines_of_reflection_indices)

        horizontal_lines_of_reflection_indices = [
            x * 100 for x in horizontal_lines_of_reflection_indices
        ]
        mirrors_sum += sum(horizontal_lines_of_reflection_indices)

        return mirrors_sum

    def solve_part_two(self):
        """
        Solves part two
        """
        horizontal_lines_of_reflection_indices = []
        vertical_lines_of_reflection_indices = []

        for _, pattern in enumerate(self.patterns):
            # First check if there is a horizontal line of reflection,
            # by seeing if two consecutive lines are the same,
            # or if they are the same with one smudge
            found_horizontal_line_of_reflection = False
            for i in range(len(pattern) - 1):
                smudges = 0
                for j in range(len(pattern[0])):
                    if pattern[i][j] != pattern[i + 1][j]:
                        smudges += 1
                    if smudges > 1:
                        break
                if smudges <= 1 and is_horizontal_line_of_reflection_with_smudge(pattern, i):
                    horizontal_lines_of_reflection_indices.append(i + 1)
                    found_horizontal_line_of_reflection = True
                    break

            if not found_horizontal_line_of_reflection:
                # If there is no horizontal line of reflection,
                # check if there is a vertical line of reflection
                for i in range(len(pattern[0]) - 1):
                    smudges = 0
                    for _, row in enumerate(pattern):
                        if row[i] != row[i + 1]:
                            smudges += 1
                        if smudges > 1:
                            break
                    if smudges <= 1 and is_vertical_line_of_reflection_with_smudge(pattern, i):
                        vertical_lines_of_reflection_indices.append(i + 1)
                        break

        mirrors_sum = sum(vertical_lines_of_reflection_indices)

        horizontal_lines_of_reflection_indices = [
            x * 100 for x in horizontal_lines_of_reflection_indices
        ]
        mirrors_sum += sum(horizontal_lines_of_reflection_indices)

        return mirrors_sum
