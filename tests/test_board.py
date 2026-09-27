from n_queens.board import all_pairs_conflicting, count_conflicts, is_solution, random_board


def test_known_solution_has_zero_conflicts():
    # a well-known 8-queens solution (0-indexed rows, one per column)
    solution = [0, 4, 7, 5, 2, 6, 1, 3]
    assert count_conflicts(solution) == 0
    assert is_solution(solution)


def test_all_queens_same_row_is_maximally_conflicted():
    board = [0, 0, 0, 0]
    # every pair of the 4 columns shares a row: C(4,2) = 6 conflicting pairs
    assert count_conflicts(board) == 6
    assert not is_solution(board)


def test_diagonal_conflict_detected():
    # queens on the main diagonal all attack each other
    board = [0, 1, 2, 3]
    assert count_conflicts(board) == 6
    assert all_pairs_conflicting(board) == [(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)]


def test_no_conflict_for_single_queen():
    assert count_conflicts([0]) == 0


def test_random_board_has_correct_length_and_range():
    board = random_board(10)
    assert len(board) == 10
    assert all(0 <= row < 10 for row in board)
