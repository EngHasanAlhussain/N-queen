"""
Hill climbing solver.

This generalizes the original ``A_loop`` (hardcoded to 8 queens, and defined
in the original source but never actually wired to a GUI button) to any
board size, and replaces its "build 8 copies of the board by hand and call
Fitness_Function 8 times" pattern with a loop over candidate rows.

Algorithm, unchanged in spirit from the original: for each column, in
order, try every possible row and keep whichever reduces total conflicts
the most (steepest-descent, one column at a time). Repeat for
``max_iterations`` full passes over all columns, or until a solution is
found.

Plain hill climbing gets stuck on local optima fairly often (this is a
known property of the algorithm, not a bug) -- ``solve_hill_climbing``
reports whether it actually found a solution, and
``solve_hill_climbing_with_restarts`` just reruns it from a fresh random
board when it doesn't, which in practice finds a solution quickly for
typical board sizes.
"""

from __future__ import annotations

import random
import time

from n_queens.board import count_conflicts, random_board
from n_queens.results import SolveResult


def solve_hill_climbing(
    n: int = 8,
    max_iterations: int = 25,
    rng: random.Random | None = None,
) -> SolveResult:
    """Run steepest-descent hill climbing from a single random start.

    ``solved`` in the returned result reflects whether a zero-conflict
    board was actually reached -- it is common for this to be False, since
    hill climbing can settle into a local optimum with no legal move that
    improves it further.
    """
    rng = rng or random
    start = time.perf_counter()
    board = random_board(n, rng)

    for iteration in range(max_iterations):
        if count_conflicts(board) == 0:
            return SolveResult(
                board=board,
                solved=True,
                algorithm="hill_climbing",
                steps=iteration,
                elapsed_seconds=time.perf_counter() - start,
            )
        for col in range(n):
            best_row = board[col]
            best_conflicts = count_conflicts(board)
            for row in range(n):
                if row == board[col]:
                    continue
                candidate = board[:]
                candidate[col] = row
                conflicts = count_conflicts(candidate)
                if conflicts < best_conflicts:
                    best_conflicts = conflicts
                    best_row = row
            board[col] = best_row

    return SolveResult(
        board=board,
        solved=count_conflicts(board) == 0,
        algorithm="hill_climbing",
        steps=max_iterations,
        elapsed_seconds=time.perf_counter() - start,
    )


def solve_hill_climbing_with_restarts(
    n: int = 8,
    max_iterations: int = 25,
    max_restarts: int = 100,
    rng: random.Random | None = None,
) -> SolveResult:
    """Random-restart hill climbing: keep trying fresh random boards until
    one run finds a solution, or ``max_restarts`` attempts are exhausted.
    """
    rng = rng or random
    start = time.perf_counter()
    total_steps = 0

    for restart in range(max_restarts):
        result = solve_hill_climbing(n, max_iterations, rng)
        total_steps += result.steps
        if result.solved:
            return SolveResult(
                board=result.board,
                solved=True,
                algorithm="hill_climbing_with_restarts",
                steps=total_steps,
                elapsed_seconds=time.perf_counter() - start,
                details={"restarts": restart},
            )

    return SolveResult(
        board=result.board,
        solved=False,
        algorithm="hill_climbing_with_restarts",
        steps=total_steps,
        elapsed_seconds=time.perf_counter() - start,
        details={"restarts": max_restarts},
    )
