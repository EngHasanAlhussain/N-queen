"""
Board representation and conflict counting.

A board is represented as a list of length N, one entry per column, where
``board[col]`` is the row (0-indexed) of the queen placed in that column.
This matches the representation used throughout the original coursework
(one queen per column) but is 0-indexed instead of 1-indexed, and every
solver in this package works with it directly instead of re-deriving an
8x8 occupancy grid every time.

The original code counted conflicts with ~150 lines of grid-scanning that
only checked whether a row or diagonal had "more than one" or "more than
two" queens on it -- it did not count actual attacking *pairs*, so its
"fitness" values weren't proportional to how far a board was from a
solution. ``count_conflicts`` below replaces all of that with the standard,
correct pairwise-conflict count, in O(N) time.
"""

from __future__ import annotations

import random
from itertools import combinations


def random_board(n: int, rng: random.Random | None = None) -> list[int]:
    """A board with each column's queen placed on a uniformly random row."""
    rng = rng or random
    return [rng.randrange(n) for _ in range(n)]


def count_conflicts(board: list[int]) -> int:
    """Number of pairs of queens that attack each other.

    Two queens at columns c1 < c2 with rows r1, r2 attack each other if
    they share a row (r1 == r2) or a diagonal (abs(r1 - r2) == c2 - c1).
    Returns 0 for a valid N-Queens solution.
    """
    n = len(board)
    row_counts: dict[int, int] = {}
    diag1_counts: dict[int, int] = {}  # constant along "\" diagonals: row - col
    diag2_counts: dict[int, int] = {}  # constant along "/" diagonals: row + col

    for col in range(n):
        row = board[col]
        row_counts[row] = row_counts.get(row, 0) + 1
        diag1_counts[row - col] = diag1_counts.get(row - col, 0) + 1
        diag2_counts[row + col] = diag2_counts.get(row + col, 0) + 1

    conflicts = 0
    for counts in (row_counts, diag1_counts, diag2_counts):
        for group_size in counts.values():
            if group_size > 1:
                # every pair within a group of size k attacks each other
                conflicts += group_size * (group_size - 1) // 2
    return conflicts


def is_solution(board: list[int]) -> bool:
    """True if no two queens on this board attack each other."""
    return count_conflicts(board) == 0


def attacks(col_a: int, row_a: int, col_b: int, row_b: int) -> bool:
    """True if a queen at (col_a, row_a) attacks one at (col_b, row_b)."""
    if col_a == col_b:
        return row_a == row_b
    return row_a == row_b or abs(row_a - row_b) == abs(col_a - col_b)


def all_pairs_conflicting(board: list[int]) -> list[tuple[int, int]]:
    """Column-index pairs of queens that attack each other. Mainly for tests
    and debugging -- ``count_conflicts`` is what the solvers use internally.
    """
    n = len(board)
    return [
        (c1, c2)
        for c1, c2 in combinations(range(n), 2)
        if attacks(c1, board[c1], c2, board[c2])
    ]
