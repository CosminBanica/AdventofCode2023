"""
Template for a day_solver
"""
from string import Template


DAY_TEMPLATE = Template(
    '"""\n\
Solver for day ${day}: ${name}\n\
"""\n\
from src.day_management.day_solver import DaySolver\n\
\n\
\n\
class Day${day}Solver(DaySolver):\n\
    """\n\
    Solver for day ${day}: ${name}\n\
    """\n\
\n\
    def solve_part_one(self):\n\
        """\n\
        Solves part one\n\
        """\n\
        return 0\n\
\n\
    def solve_part_two(self):\n\
        """\n\
        Solves part two\n\
        """\n\
        return 0\n\
'
)
