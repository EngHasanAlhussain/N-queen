import random

from n_queens.board import count_conflicts
from n_queens.hill_climbing import solve_hill_climbing, solve_hill_climbing_with_restarts


def test_single_attempt_returns_a_result_even_if_stuck():
    result = solve_hill_climbing(n=8, rng=random.Random(1))
    assert result.algorithm == "hill_climbing"
    assert len(result.board) == 8
    assert result.solved == (count_conflicts(result.board) == 0)


def test_restarts_eventually_find_a_solution():
    result = solve_hill_climbing_with_restarts(n=8, max_restarts=200, rng=random.Random(1))
    assert result.solved
    assert count_conflicts(result.board) == 0
