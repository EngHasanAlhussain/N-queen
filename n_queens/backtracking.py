"""
CSP backtracking solver with optional heuristics.

The original ``MRV_MCV_LCV`` function was not actually backtracking search:
it was a hand-rolled repair loop, capped at 40 iterations, that assigned
a queen, patched up conflicts with more ad-hoc loops, and gave up (silently,
printing whatever partial board it had) if that cap was hit. Its
"arc consistency" check compared a board value against the Tkinter
``IntVar`` object ``N`` instead of ``N.get()``, so it could never actually
trigger, and its "least constraining value" branch computed a candidate row
into a local variable and then never assigned it anywhere.

This is a real recursive backtracking search over one column at a time,
with the same five options the original GUI exposed:

  * ``mrv``  -- Minimum Remaining Values: assign the unassigned column with
    the fewest legal rows left first.
  * ``mcv``  -- Most Constraining Variable: among the candidates MRV leaves
    (or all unassigned columns, if MRV is off), break ties by choosing the
    column whose current domain rules out the most values in *other*
    unassigned columns' domains. (For N-Queens every pair of columns
    constrains each other, so the classic graph-degree version of this
    heuristic is a no-op here -- this domain-aware version is what actually
    produces a meaningful ordering.)
  * ``lcv``  -- Least Constraining Value: try the row that rules out the
    fewest values in other columns' domains first.
  * ``forward_checking`` -- after each assignment, immediately remove the
    newly-attacked row from every other unassigned column's domain, and
    backtrack right away if that empties one.
  * ``arc_consistency`` -- a simplified AC-3 pass: after each assignment
    (and any forward checking), repeatedly drop any remaining value that
    no longer has a supporting value in some other unassigned column's
    domain, until nothing changes or a domain is emptied.

With every option off, this is plain chronological backtracking -- still
complete, just unguided.
"""

from __future__ import annotations

import time

from n_queens.results import SolveResult

Domains = dict[int, set[int]]
Assignment = dict[int, int]


def _conflicts(col_a: int, row_a: int, col_b: int, row_b: int) -> bool:
    return row_a == row_b or abs(row_a - row_b) == abs(col_a - col_b)


def _is_consistent(col: int, row: int, assignment: Assignment) -> bool:
    return all(
        not _conflicts(col, row, c2, r2) for c2, r2 in assignment.items()
    )


def _constraint_impact(col: int, domains: Domains, assignment: Assignment) -> int:
    """How many (column, row) options in *other* unassigned columns would
    become invalid if some value gets picked for ``col`` -- used to compare
    candidate columns (MCV) and candidate values (LCV).
    """
    total = 0
    for row in domains[col]:
        for c2, d2 in domains.items():
            if c2 == col or c2 in assignment:
                continue
            total += sum(1 for r2 in d2 if _conflicts(col, row, c2, r2))
    return total


def _select_column(domains: Domains, assignment: Assignment, mrv: bool, mcv: bool) -> int:
    unassigned = [c for c in domains if c not in assignment]
    candidates = unassigned
    if mrv:
        smallest = min(len(domains[c]) for c in candidates)
        candidates = [c for c in candidates if len(domains[c]) == smallest]
    if mcv and len(candidates) > 1:
        most_constraining = max(
            _constraint_impact(c, domains, assignment) for c in candidates
        )
        candidates = [
            c for c in candidates
            if _constraint_impact(c, domains, assignment) == most_constraining
        ]
    return candidates[0]


def _order_values(col: int, domains: Domains, assignment: Assignment, lcv: bool) -> list[int]:
    values = list(domains[col])
    if not lcv:
        return values

    def rule_out_count(row: int) -> int:
        total = 0
        for c2, d2 in domains.items():
            if c2 == col or c2 in assignment:
                continue
            total += sum(1 for r2 in d2 if _conflicts(col, row, c2, r2))
        return total

    return sorted(values, key=rule_out_count)


def _forward_check(col: int, row: int, domains: Domains, assignment: Assignment) -> Domains | None:
    pruned = {c: set(d) for c, d in domains.items()}
    pruned[col] = {row}
    for c2, d2 in pruned.items():
        if c2 == col or c2 in assignment:
            continue
        remaining = {r2 for r2 in d2 if not _conflicts(col, row, c2, r2)}
        if not remaining:
            return None
        pruned[c2] = remaining
    return pruned


def _enforce_arc_consistency(domains: Domains, assignment: Assignment) -> Domains | None:
    """Repeatedly drop values with no supporting value left anywhere else,
    until a fixed point is reached or some domain is emptied.
    """
    domains = {c: set(d) for c, d in domains.items()}
    unassigned = [c for c in domains if c not in assignment]

    changed = True
    while changed:
        changed = False
        for c1 in unassigned:
            supported = set()
            for r1 in domains[c1]:
                has_support = any(
                    any(not _conflicts(c1, r1, c2, r2) for r2 in domains[c2])
                    for c2 in unassigned
                    if c2 != c1
                ) or len(unassigned) == 1
                if has_support:
                    supported.add(r1)
            if not supported:
                return None
            if supported != domains[c1]:
                domains[c1] = supported
                changed = True
    return domains


def solve_backtracking(
    n: int,
    mrv: bool = False,
    mcv: bool = False,
    lcv: bool = False,
    forward_checking: bool = False,
    arc_consistency: bool = False,
) -> SolveResult:
    """Solve N-Queens with backtracking search, using whichever of the five
    heuristics above are switched on (any combination is valid).
    """
    start = time.perf_counter()
    domains: Domains = {c: set(range(n)) for c in range(n)}
    assignment: Assignment = {}
    nodes = 0

    def backtrack(domains: Domains) -> bool:
        nonlocal nodes
        nodes += 1
        if len(assignment) == n:
            return True

        col = _select_column(domains, assignment, mrv, mcv)
        for row in _order_values(col, domains, assignment, lcv):
            if not _is_consistent(col, row, assignment):
                continue

            assignment[col] = row
            next_domains = domains
            ok = True

            if forward_checking or arc_consistency:
                next_domains = _forward_check(col, row, domains, assignment)
                ok = next_domains is not None

            if ok and arc_consistency:
                next_domains = _enforce_arc_consistency(next_domains, assignment)
                ok = next_domains is not None

            if ok and backtrack(next_domains if next_domains else domains):
                return True

            del assignment[col]

        return False

    solved = backtrack(domains)
    board = [assignment[c] for c in range(n)] if solved else None

    return SolveResult(
        board=board,
        solved=solved,
        algorithm="backtracking",
        steps=nodes,
        elapsed_seconds=time.perf_counter() - start,
        details={
            "mrv": mrv,
            "mcv": mcv,
            "lcv": lcv,
            "forward_checking": forward_checking,
            "arc_consistency": arc_consistency,
        },
    )
