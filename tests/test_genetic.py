import random

from n_queens.board import count_conflicts
from n_queens.genetic import solve_genetic


def test_solves_eight_queens():
    result = solve_genetic(n=8, rng=random.Random(1))
    assert result.solved
    assert count_conflicts(result.board) == 0
    assert len(result.board) == 8


def test_solves_a_smaller_board():
    result = solve_genetic(n=5, rng=random.Random(2))
    assert result.solved
    assert count_conflicts(result.board) == 0


def test_gives_up_gracefully_when_no_solution_exists():
    # N-Queens has no solution for N == 2 or N == 3
    result = solve_genetic(n=3, max_generations=50, max_restarts=3, rng=random.Random(3))
    assert result.solved is False
    assert result.board is not None  # still returns its best attempt
