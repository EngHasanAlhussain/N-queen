# N-Queens Solver

A from-scratch N-Queens solver with three AI search strategies — genetic
algorithm, hill climbing, and CSP backtracking with configurable heuristics
— plus a Tkinter GUI. Originally built for the Introduction to Artificial
Intelligence course at KFUPM (2021); refactored since into a proper package
with tests.

## The problem

Place N queens on an N×N chessboard so that no two queens attack each
other (no shared row, column, or diagonal).

## AI disclosure

This started as a prototype I submitted for coursework in 2021 (preserved
as-is in `legacy/`). In 2026 I used AI (Claude) to find and fix real bugs,
generalize the algorithms to any board size, add the test suite, and
restructure the code into a proper package -- to bring it up to a standard
worth sharing publicly and useful to others learning this material. See
"What changed from the original submission" below for the specifics.

## Repo structure

```
.
├── n_queens/
│   ├── board.py           # board representation + conflict counting
│   ├── genetic.py         # genetic algorithm solver
│   ├── hill_climbing.py   # steepest-descent hill climbing solver
│   ├── backtracking.py    # CSP backtracking with MRV/MCV/LCV/FC/AC
│   ├── gui.py             # Tkinter GUI wiring it all together
│   └── results.py         # SolveResult, shared by all three solvers
├── tests/                 # pytest suite for the three solvers
├── legacy/
│   └── Application.py     # the original 2021 coursework submission, untouched
├── main.py                # entry point: `python main.py`
└── requirements-dev.txt   # pytest, for running the test suite
```

## Algorithms

**Genetic Algorithm** (`n_queens/genetic.py`) — Maintains a population of
random candidate boards. Each generation: the single weakest candidate
(by conflict count) is replaced with a clone of the fittest; individuals
are paired up and recombined with a fixed-point crossover; every
individual then gets one randomly reset gene. Restarts with a fresh
population if it doesn't converge within `max_generations`.

**Hill Climbing** (`n_queens/hill_climbing.py`) — Steepest-descent local
search: for each column in turn, try every row and keep whichever reduces
the total conflict count the most. This can get stuck at a local optimum
with no improving move, which is a known property of hill climbing, not a
bug — `solve_hill_climbing_with_restarts` compensates by retrying from a
fresh random board until one attempt succeeds.

**Backtracking with CSP heuristics** (`n_queens/backtracking.py`) — Real
recursive backtracking search, one column at a time, with five
independently-toggleable heuristics:
- **MRV** (Minimum Remaining Values) — assign the column with the fewest
  legal rows left first.
- **MCV** (Most Constraining Variable) — break MRV ties by preferring the
  column whose assignment would eliminate the most options elsewhere.
- **LCV** (Least Constraining Value) — try the row that rules out the
  fewest options in other columns first.
- **Forward Checking** — after each assignment, immediately prune the
  newly-attacked row from every other column's remaining options, and
  backtrack right away if that empties one.
- **Arc Consistency** — a simplified AC-3 pass that repeatedly drops any
  value with no remaining support elsewhere, beyond what forward checking
  alone catches.

All three work for any board size N, not just 8.

## Running it

Requires Python 3.10+ with Tkinter (bundled with most Python installations;
on some Linux distros you may need `sudo apt install python3-tk`). No
other dependencies to run the app itself.

```bash
python main.py
```

Enter a board size, then pick an algorithm. For backtracking, tick
whichever heuristics you want to combine before running.

## Running the tests

```bash
pip install -r requirements-dev.txt
pytest
```

142 tests cover the conflict-counting logic directly, all 32 combinations
of the five backtracking heuristics across several board sizes, and that
the genetic algorithm and hill climbing actually converge on solutions
(and fail gracefully, rather than hanging, for N=2 and N=3, which have no
solution).

## What changed from the original submission

`legacy/Application.py` is the code as submitted in 2021 — everything
below it was rewritten from there:

- **Structure** — one 870-line file with algorithm logic, Tkinter widget
  code, and ~300 lines of `if x==0: ... elif x==1: ...` selection chains
  all tangled together, into small, independently testable modules.
- **Naming** — `list1` through `list8`, single-letter loop variables, and
  functions like `MRV_MCV_LCV` that did all five heuristics regardless of
  which were requested, replaced with descriptive names and a proper
  `mrv=`, `mcv=`, `lcv=`, `forward_checking=`, `arc_consistency=` API.
- **Generalized to any N** — the genetic algorithm and hill climbing were
  hardcoded to 8 queens because each candidate board was 8 separate
  Python variables; both now take arbitrary board sizes.
- **Fixed real bugs**, found while reading the original code closely:
  - The "arc consistency" check compared a board value to the Tkinter
    `IntVar` object `N` instead of `N.get()`, so the comparison could
    never be true and the check never actually did anything.
  - The "least constraining value" branch computed a candidate value
    (`board[d][x]`) and never assigned it anywhere — dead code.
  - A crossover step assigned `list7_copy[4:8] = list7[4:8]` and
    `list8_copy[4:8] = list8[4:8]` — copying each list onto itself instead
    of exchanging material with its partner.
  - `Fitness_Function`'s conflict count wasn't proportional to how close a
    board was to solved (it flagged a row as "conflicted" the same way
    whether 2 or 8 queens shared it), which made it a weak search signal.
    `count_conflicts` in `n_queens/board.py` now counts actual attacking
    pairs.
  - The original "backtracking" function wasn't backtracking search at
    all — it was a repair loop capped at 40 iterations that could give up
    without a full solution. `n_queens/backtracking.py` is real recursive
    backtracking, which is complete (guaranteed to find a solution if one
    exists) for any N.

## Known limitations

- Hill climbing (even with restarts) is a local search heuristic, not a
  complete algorithm — for pathological seeds it can take many restarts.
- The arc-consistency pass is a simplified, from-scratch version, not a
  textbook AC-3 with an explicit worklist queue — it's correct, but not
  necessarily the most efficient implementation of the idea.
- The GUI runs each solve synchronously, so the window doesn't repaint
  mid-solve; every algorithm here finishes fast enough in practice
  (milliseconds to low seconds) that this hasn't been a problem, but a
  very large N with weak heuristics could make it look unresponsive.
