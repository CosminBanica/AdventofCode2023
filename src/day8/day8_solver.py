"""
Solver for day 8: Haunted Wasteland
"""
import math
from itertools import cycle
from src.day_management.day_solver import DaySolver


class Node:
    """
    Node class
    """

    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def set_right(self, right):
        """
        Sets right node
        """
        self.right = right

    def set_left(self, left):
        """
        Sets left node
        """
        self.left = left

    def __str__(self):
        return f"Node: {self.value} -> ({self.left.value} | {self.right.value})"


class Day8Solver(DaySolver):
    """
    Solver for day 8: Haunted Wasteland
    """

    def __init__(self, input_data):
        super().__init__(input_data)
        self.instructions = list(input_data[0])
        self.nodes = {}
        for i in range(2, len(self.input_data)):
            node_data = self.input_data[i]
            node_value = node_data[0:3]
            node_left_value = node_data[7:10]
            node_right_value = node_data[12:15]

            if node_value not in self.nodes:
                node_left = self.nodes.get(node_left_value, Node(node_left_value))
                self.nodes[node_left_value] = node_left

                node_right = self.nodes.get(node_right_value, Node(node_right_value))
                self.nodes[node_right_value] = node_right

                self.nodes[node_value] = Node(node_value, node_left, node_right)
            else:
                node_left = self.nodes.get(node_left_value, Node(node_left_value))
                self.nodes[node_left_value] = node_left

                node_right = self.nodes.get(node_right_value, Node(node_right_value))
                self.nodes[node_right_value] = node_right

                self.nodes[node_value].set_left(node_left)
                self.nodes[node_value].set_right(node_right)

    def solve_part_one(self):
        """
        Solves part one
        """
        instructions = cycle(self.instructions)
        current_node = self.nodes.get("AAA", None)
        step = 0

        if current_node is None:
            return -1

        for instruction in instructions:
            if current_node.value == "ZZZ":
                return step

            if instruction == "L":
                current_node = current_node.left
            elif instruction == "R":
                current_node = current_node.right

            step += 1

        return -1

    def solve_part_two(self):
        """
        Solves part two
        """
        loop_lengths = []
        starting_nodes = [node for node in self.nodes.values() if node.value[2] == "A"]

        # For each of the starting nodes, iterate until we find a node that ends in Z,
        # to find the length of the loop
        for starting_node in starting_nodes:
            current_node = starting_node
            step = 0
            instructions = cycle(self.instructions)

            for instruction in instructions:
                if current_node.value[2] == "Z":
                    loop_lengths.append(step)
                    break

                if instruction == "L":
                    current_node = current_node.left
                elif instruction == "R":
                    current_node = current_node.right

                step += 1

        # Find the lowest common multiple of all the loop lengths
        lcm = math.lcm(*loop_lengths)

        return lcm
