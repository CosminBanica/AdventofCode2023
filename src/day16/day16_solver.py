"""
Solver for day 16: The Floor Will Be Lava
"""
from dataclasses import dataclass
from src.day_management.day_solver import DaySolver
from src.utils.enums import Direction


NEXT_DIRECTION = {
    "UP/": [Direction.RIGHT],
    "UP\\": [Direction.LEFT],
    "DOWN/": [Direction.LEFT],
    "DOWN\\": [Direction.RIGHT],
    "LEFT/": [Direction.DOWN],
    "LEFT\\": [Direction.UP],
    "RIGHT/": [Direction.UP],
    "RIGHT\\": [Direction.DOWN],
    "UP|": [Direction.UP],
    "DOWN|": [Direction.DOWN],
    "LEFT-": [Direction.LEFT],
    "RIGHT-": [Direction.RIGHT],
    "UP-": [Direction.LEFT, Direction.RIGHT],
    "DOWN-": [Direction.LEFT, Direction.RIGHT],
    "LEFT|": [Direction.UP, Direction.DOWN],
    "RIGHT|": [Direction.UP, Direction.DOWN],
}


@dataclass
class Tile:
    """
    Represents the state of a tile
    """

    energized: bool
    beam_directions: list[Direction]


@dataclass
class Beam:
    """
    Represents the state of the tip of a beam
    """

    pos: tuple[int, int]
    direction: Direction


class Day16Solver(DaySolver):
    """
    Solver for day 16: The Floor Will Be Lava
    """

    def __init__(self, input_data):
        super().__init__(input_data)
        self.map = []
        self.visited = []
        for line in input_data:
            self.map.append(list(line))
            self.visited.append([Tile(False, []) for _ in range(len(line))])

    def clear_visited(self):
        """
        Clears the visited tiles
        """
        for line in self.visited:
            for tile in line:
                tile.energized = False
                tile.beam_directions = []

    def visit_and_return_if_direction_duplicate(self, beam: Beam, x: int, y: int):
        """
        Visits a tile, and returns if a beam with the same direction has already visited it
        """
        self.visited[x][y].energized = True
        if beam.direction in self.visited[x][y].beam_directions:
            return True

        self.visited[x][y].beam_directions.append(beam.direction)
        return False

    def get_beams_from_reflection(self, beam: Beam, x: int, y: int):
        """
        Gets the next beams from a reflection
        """
        next_directions = NEXT_DIRECTION[beam.direction.name + self.map[x][y]]

        next_beams = []
        for next_direction in next_directions:
            next_beams.append(Beam((x, y), next_direction))

        return next_beams

    def get_next_beams(self, beam: Beam):
        """
        Gets the next beams from a given beam
        """
        next_beams = []
        x, y = beam.pos
        next_x, next_y = None, None
        if beam.direction == Direction.UP:
            next_x, next_y = x - 1, y
        elif beam.direction == Direction.DOWN:
            next_x, next_y = x + 1, y
        elif beam.direction == Direction.LEFT:
            next_x, next_y = x, y - 1
        elif beam.direction == Direction.RIGHT:
            next_x, next_y = x, y + 1

        if 0 <= next_x < len(self.map) and 0 <= next_y < len(self.map[next_x]):
            if self.map[next_x][next_y] == ".":
                next_beams.append(Beam((next_x, next_y), beam.direction))
            else:
                next_beams += self.get_beams_from_reflection(beam, next_x, next_y)
        else:
            return []

        next_beams_unique = []
        for next_beam in next_beams:
            is_duplicate = self.visit_and_return_if_direction_duplicate(
                next_beam, next_x, next_y
            )
            if not is_duplicate:
                next_beams_unique.append(next_beam)

        return next_beams_unique

    def solve_part_one(self):
        """
        Solves part one
        """
        beams = [Beam((0, 0), Direction.RIGHT)]
        self.visit_and_return_if_direction_duplicate(beams[0], 0, 0)

        while len(beams) > 0:
            next_beams = []

            for beam in beams:
                next_beams += self.get_next_beams(beam)

            beams = next_beams

        total_energized = 0
        for line in self.visited:
            for tile in line:
                if tile.energized:
                    total_energized += 1

        return total_energized

    def solve_part_two(self):
        """
        Solves part two
        """
        max_total_energized = 0

        # Start a beam from every edge tile, with direction opposite to the edge
        for x, line in enumerate(self.map):
            for y, _ in enumerate(line):
                beams = []
                if x == 0:
                    beams = [Beam((x, y), Direction.DOWN)]
                elif x == len(self.map) - 1:
                    beams = [Beam((x, y), Direction.UP)]
                elif y == 0:
                    beams = [Beam((x, y), Direction.RIGHT)]
                elif y == len(self.map[x]) - 1:
                    beams = [Beam((x, y), Direction.LEFT)]
                else:
                    continue

                self.clear_visited()
                self.visited[x][y].energized = True

                while len(beams) > 0:
                    next_beams = []

                    for beam in beams:
                        next_beams += self.get_next_beams(beam)

                    beams = next_beams

                total_energized = 0
                for line in self.visited:
                    for tile in line:
                        if tile.energized:
                            total_energized += 1

                max_total_energized = max(max_total_energized, total_energized)

        return max_total_energized
