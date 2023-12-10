"""
Solver for day 10: Pipe Maze
"""
from enum import Enum
from src.day_management.day_solver import DaySolver


class Direction(Enum):
    """
    Enum for directions
    """

    UP = 0
    DOWN = 1
    LEFT = 2
    RIGHT = 3


class Day10Solver(DaySolver):
    """
    Solver for day 10: Pipe Maze
    """

    def __init__(self, input_data):
        super().__init__(input_data)
        self.map = list(map(lambda x: x, input_data))
        self.starting_position = self.get_starting_position()
        self.added_pipes = []
        self.zoomed_map = self.get_zoomed_map()
        self.zoomed_starting_position = self.get_zoomed_starting_position()

    def get_zoomed_starting_position(self):
        """
        Gets the starting position of the zoomed map
        """
        for i, row in enumerate(self.zoomed_map):
            for j, char in enumerate(row):
                if char == "S":
                    return i, j
        return None

    def get_zoomed_map(self):
        """
        Create a 2x sized map, where between each original 2 neighboring
        rows and columns there is a row/column of 'N'
        """
        zoomed_map = [["N" for _ in range(2 * len(self.map[0]) + 1)]]
        for i, row in enumerate(self.map):
            new_row = ["N"]
            for j, char in enumerate(row):
                new_row.append(char)
                if self.left_and_right_connected(i, j):
                    new_row.append("-")
                    self.added_pipes.append((i * 2 + 1, j * 2 + 1))
                else:
                    new_row.append("N")
            zoomed_map.append(new_row)

            new_row = ["N"]
            for j in range(len(row)):
                if self.up_and_down_connected(i, j):
                    new_row.append("|")
                    self.added_pipes.append((i * 2 + 2, j * 2 + 1))
                else:
                    new_row.append("N")
                new_row.append("N")
            zoomed_map.append(new_row)

        return zoomed_map

    def left_and_right_connected(self, i, j):
        """
        Checks if the right position of the given position is connected
        """
        if j + 1 < len(self.map[i]):
            left_char = self.map[i][j]
            right_char = self.map[i][j + 1]
            if right_char in ["-", "J", "7", "S"] and left_char in ["-", "L", "F", "S"]:
                return True
        return False

    def up_and_down_connected(self, i, j):
        """
        Checks if the down position of the given position is connected
        """
        if i + 1 < len(self.map):
            up_char = self.map[i][j]
            down_char = self.map[i + 1][j]
            if up_char in ["|", "7", "F", "S"] and down_char in ["|", "J", "L", "S"]:
                return True
        return False

    def get_starting_position(self):
        """
        Gets the starting position of the map
        """
        for i, row in enumerate(self.map):
            for j, char in enumerate(row):
                if char == "S":
                    return i, j
        return None, None

    def is_connected_to_direction(self, direction, position):
        """
        Checks if two positions are connected
        """
        i, j = position
        if direction == Direction.UP:
            return self.map[i][j] in ["|", "J", "L"]
        if direction == Direction.DOWN:
            return self.map[i][j] in ["|", "7", "F"]
        if direction == Direction.LEFT:
            return self.map[i][j] in ["-", "J", "7"]
        if direction == Direction.RIGHT:
            return self.map[i][j] in ["-", "L", "F"]
        return False

    def get_connected_positions_and_directions(self, position):
        """
        Gets the two connected positions to the given position
        and their directions to the given position
        """
        i, j = position
        connected_positions = []
        directions = []

        if i - 1 >= 0 and self.map[i - 1][j] != "." and self.map[i - 1][j] != "N":
            if self.is_connected_to_direction(Direction.DOWN, (i - 1, j)):
                connected_positions.append((i - 1, j))
                directions.append(Direction.DOWN)
        if (
            i + 1 < len(self.map)
            and self.map[i + 1][j] != "."
            and self.map[i + 1][j] != "N"
        ):
            if self.is_connected_to_direction(Direction.UP, (i + 1, j)):
                connected_positions.append((i + 1, j))
                directions.append(Direction.UP)
        if j - 1 >= 0 and self.map[i][j - 1] != "." and self.map[i][j - 1] != "N":
            if self.is_connected_to_direction(Direction.RIGHT, (i, j - 1)):
                connected_positions.append((i, j - 1))
                directions.append(Direction.RIGHT)
        if (
            j + 1 < len(self.map[i])
            and self.map[i][j + 1] != "."
            and self.map[i][j + 1] != "N"
        ):
            if self.is_connected_to_direction(Direction.LEFT, (i, j + 1)):
                connected_positions.append((i, j + 1))
                directions.append(Direction.LEFT)

        return connected_positions, directions

    def get_next_position_and_direction(self, position, direction):
        """
        Gets the next position and direction from the given position and direction
        """
        i, j = position
        next_position = None
        next_direction = None

        if direction == Direction.UP and self.map[i][j] == "|":
            next_position = (i + 1, j)
            next_direction = Direction.UP
        elif direction == Direction.UP and self.map[i][j] == "J":
            next_position = (i, j - 1)
            next_direction = Direction.RIGHT
        elif direction == Direction.UP and self.map[i][j] == "L":
            next_position = (i, j + 1)
            next_direction = Direction.LEFT

        if direction == Direction.DOWN and self.map[i][j] == "|":
            next_position = (i - 1, j)
            next_direction = Direction.DOWN
        elif direction == Direction.DOWN and self.map[i][j] == "7":
            next_position = (i, j - 1)
            next_direction = Direction.RIGHT
        elif direction == Direction.DOWN and self.map[i][j] == "F":
            next_position = (i, j + 1)
            next_direction = Direction.LEFT

        if direction == Direction.LEFT and self.map[i][j] == "-":
            next_position = (i, j + 1)
            next_direction = Direction.LEFT
        elif direction == Direction.LEFT and self.map[i][j] == "J":
            next_position = (i - 1, j)
            next_direction = Direction.DOWN
        elif direction == Direction.LEFT and self.map[i][j] == "7":
            next_position = (i + 1, j)
            next_direction = Direction.UP

        if direction == Direction.RIGHT and self.map[i][j] == "-":
            next_position = (i, j - 1)
            next_direction = Direction.RIGHT
        elif direction == Direction.RIGHT and self.map[i][j] == "L":
            next_position = (i - 1, j)
            next_direction = Direction.DOWN
        elif direction == Direction.RIGHT and self.map[i][j] == "F":
            next_position = (i + 1, j)
            next_direction = Direction.UP

        return next_position, next_direction

    def mark_loop(self):
        """
        Marks the loop in the zoomed map
        """
        current_position = self.zoomed_starting_position
        save_map = self.map
        self.map = self.zoomed_map

        positions, directions = self.get_connected_positions_and_directions(
            current_position
        )
        current_position1, current_position2 = positions
        direction1, direction2 = directions

        while current_position1 != current_position2:
            (
                new_current_position1,
                new_direction1,
            ) = self.get_next_position_and_direction(current_position1, direction1)
            (
                new_current_position2,
                new_direction2,
            ) = self.get_next_position_and_direction(current_position2, direction2)
            self.map[current_position1[0]][current_position1[1]] = "X"
            self.map[current_position2[0]][current_position2[1]] = "X"
            current_position1, direction1 = new_current_position1, new_direction1
            current_position2, direction2 = new_current_position2, new_direction2

        self.map[current_position1[0]][current_position1[1]] = "X"
        self.map[current_position2[0]][current_position2[1]] = "X"

        self.zoomed_map = self.map
        self.map = save_map

    def flood_map(self, position):
        """
        Go to all neighboring positions and flood them, if they are not flooded yet
        Flood a tile by changing it to 'O'
        'X' and 'S' are walls
        """
        i, j = position
        if self.zoomed_map[i][j] in ["X", "S", "O"]:
            return

        self.zoomed_map[i][j] = "O"

        if i - 1 >= 0:
            self.flood_map((i - 1, j))
        if i + 1 < len(self.zoomed_map):
            self.flood_map((i + 1, j))
        if j - 1 >= 0:
            self.flood_map((i, j - 1))
        if j + 1 < len(self.zoomed_map[i]):
            self.flood_map((i, j + 1))

    def flood_map_non_recursive(self):
        """
        Go to all reachable positions and flood them, if they are not flooded yet
        Flood a tile by changing it to 'O'
        'X' and 'S' are walls
        """
        i, j = 0, 0
        stack = [(i, j)]
        while len(stack) > 0:
            i, j = stack.pop()
            if self.zoomed_map[i][j] in ["X", "S", "O"]:
                continue
            self.zoomed_map[i][j] = "O"
            if i - 1 >= 0:
                stack.append((i - 1, j))
            if i + 1 < len(self.zoomed_map):
                stack.append((i + 1, j))
            if j - 1 >= 0:
                stack.append((i, j - 1))
            if j + 1 < len(self.zoomed_map[i]):
                stack.append((i, j + 1))

    def get_number_of_tiles_enclosed(self):
        """
        Gets the number of tiles enclosed by the loop
        """
        nr_tiles_enclosed = 0
        for i, row in enumerate(self.zoomed_map):
            for j, char in enumerate(row):
                if char not in ["X", "S", "O", "N"] and (i, j) not in self.added_pipes:
                    nr_tiles_enclosed += 1
        return nr_tiles_enclosed

    def solve_part_one(self):
        """
        Solves part one
        """
        distance1, distance2 = 0, 0
        positions, directions = self.get_connected_positions_and_directions(
            self.starting_position
        )
        current_position1, current_position2 = positions
        direction1, direction2 = directions

        while current_position1 != current_position2:
            distance1 += 1
            distance2 += 1

            current_position1, direction1 = self.get_next_position_and_direction(
                current_position1, direction1
            )
            current_position2, direction2 = self.get_next_position_and_direction(
                current_position2, direction2
            )

        return max(distance1, distance2) + 1

    def solve_part_two(self):
        """
        Solves part two
        """
        self.mark_loop()

        self.flood_map_non_recursive()

        nr_tiles_enclosed = self.get_number_of_tiles_enclosed()

        return nr_tiles_enclosed
