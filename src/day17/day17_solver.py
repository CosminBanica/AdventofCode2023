"""
Solver for day 17: Clumsy Crucible
"""
from heapq import heappop, heappush
from src.day_management.day_solver import DaySolver


DIRECTION_TO_VECTOR = {
    0: (0, 1),
    1: (1, 0),
    2: (0, -1),
    3: (-1, 0),
}


class Day17Solver(DaySolver):
    """
    Solver for day 17: Clumsy Crucible
    """

    def __init__(self, input_data):
        super().__init__(input_data)
        self.map = []
        for line in input_data:
            line_list = list(line.strip())
            line_list = [int(char) for char in line_list]
            self.map.append(line_list)
        self.min_straight_moves = 0
        self.max_straight_moves = 0

    def djikstra_with_cost(self):
        """
        Returns the minimal heat loss path
        """
        visited = set()
        end_pos = (len(self.map) - 1, len(self.map[0]) - 1)
        start_pos = (0, 0)
        queue = [(0, start_pos, -1)]
        costs = {}

        while queue:
            cost, pos, direction = heappop(queue)
            if pos == end_pos:
                return cost
            if (pos, direction) in visited:
                continue
            visited.add((pos, direction))
            for new_direction in range(4):
                added_cost = 0

                # Can't go back the way we came
                if direction in [new_direction, (new_direction + 2) % 4]:
                    continue

                for dist in range(1, self.max_straight_moves + 1):
                    new_pos = (
                        pos[0] + DIRECTION_TO_VECTOR[new_direction][0] * dist,
                        pos[1] + DIRECTION_TO_VECTOR[new_direction][1] * dist,
                    )

                    if 0 <= new_pos[0] < len(self.map) and 0 <= new_pos[1] < len(
                        self.map[0]
                    ):
                        added_cost += self.map[new_pos[1]][new_pos[0]]
                        if dist < self.min_straight_moves:
                            continue
                        new_cost = cost + added_cost
                        if costs.get((new_pos, new_direction), 1e100) <= new_cost:
                            continue
                        costs[(new_pos, new_direction)] = new_cost
                        heappush(queue, (new_cost, new_pos, new_direction))

        return 0

    def solve_part_one(self):
        """
        Solves part one
        """
        self.min_straight_moves = 1
        self.max_straight_moves = 3
        minimal_heat_loss = self.djikstra_with_cost()

        return minimal_heat_loss

    def solve_part_two(self):
        """
        Solves part two
        """
        self.min_straight_moves = 4
        self.max_straight_moves = 10
        minimal_heat_loss = self.djikstra_with_cost()

        return minimal_heat_loss
