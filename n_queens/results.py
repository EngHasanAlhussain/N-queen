"""Shared result type returned by every solver in this package."""

from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class SolveResult:
    """Outcome of a solve attempt.

    Attributes:
        board: The final board (list of rows, one per column), or ``None``
            if no board was ever produced.
        solved: Whether ``board`` has zero conflicts.
        algorithm: Short name of the algorithm that produced this result.
        steps: Algorithm-specific step count (generations, hill-climbing
            iterations, or backtracking nodes expanded) -- see ``details``
            for the exact meaning per algorithm.
        elapsed_seconds: Wall-clock time spent solving.
        details: Free-form extra info (e.g. number of restarts).
    """

    board: list[int] | None
    solved: bool
    algorithm: str
    steps: int
    elapsed_seconds: float
    details: dict = field(default_factory=dict)
