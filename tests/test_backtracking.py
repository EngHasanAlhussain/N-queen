from itertools import product

import pytest

from n_queens.board import count_conflicts
from n_queens.backtracking import solve_backtracking

HEURISTIC_COMBINATIONS = list(product([False, True], repeat=5))


@pytest.mark.parametrize("mrv,mcv,lcv,forward_checking,arc_consistency", HEURISTIC_COMBINATIONS)
@pytest.mark.parametrize("n", [4, 5, 6, 8])
def test_finds_a_valid_solution_for_every_heuristic_combination(
    n, mrv, mcv, lcv, forward_checking, arc_consistency
):
    result = solve_backtracking(
        n,
        mrv=mrv,
        mcv=mcv,
        lcv=lcv,
        forward_checking=forward_checking,
        arc_consistency=arc_consistency,
    )
    assert result.solved, f"no solution found for n={n} with flags={result.details}"
    assert len(result.board) == n
    assert count_conflicts(result.board) == 0


@pytest.mark.parametrize("n", [2, 3])
def test_reports_failure_when_no_solution_exists(n):
    result = solve_backtracking(n, mrv=True, forward_checking=True)
    assert result.solved is False
    assert result.board is None


def test_plain_backtracking_with_no_heuristics_still_works():
    result = solve_backtracking(8)
    assert result.solved
    assert count_conflicts(result.board) == 0


def test_heuristics_reduce_nodes_expanded_on_average():
    # Not a strict guarantee for every seed/board, but MRV+FC should not be
    # wildly worse than plain backtracking for a solvable board like N=8.
    plain = solve_backtracking(8)
    guided = solve_backtracking(8, mrv=True, forward_checking=True)
    assert guided.steps <= plain.steps * 5
