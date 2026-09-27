"""
n_queens
========
A small, dependency-free N-Queens solver package with three interchangeable
search strategies (genetic algorithm, hill climbing, and CSP backtracking
with configurable heuristics) plus a Tkinter GUI.

This is a refactor of a 2021 KFUPM "Introduction to Artificial Intelligence"
coursework project. The original single-file submission is preserved under
``legacy/Application.py`` for reference; see the top-level README for details
on what changed and why.
"""

from n_queens.board import count_conflicts, is_solution, random_board
from n_queens.results import SolveResult

__all__ = [
    "count_conflicts",
    "is_solution",
    "random_board",
    "SolveResult",
]
