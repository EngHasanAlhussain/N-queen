# N-Queens Solver

A Tkinter desktop app that solves the classic N-Queens problem using three different AI search strategies. Built for the Introduction to Artificial Intelligence course at KFUPM, 2021.

## The problem

Place N queens on an N×N chessboard so that no two queens attack each other (no shared row, column, or diagonal). This project explores three very different AI approaches to finding a solution and lets you compare how they perform.

## Algorithms

**Genetic Algorithm** — Starts with a population of 8 random candidate boards (8-Queens only). Each candidate's fitness is its number of conflicts (attacking pairs). Every generation, the weakest candidate is replaced with a clone of the fittest, candidates are recombined with fixed-point crossover, and a random mutation is applied to each. Runs for up to 7000 generations before restarting with a fresh population.

**Backtracking with CSP heuristics** — Works for any board size N (you choose N in the app). Assigns queens column by column, with optional heuristics you can toggle and combine:
- **MRV** (Minimum Remaining Values)
- **MCV** (Most Constraining Variable)
- **LCV** (Least Constraining Value)
- **Arc Consistency (AC)**
- **Forward Checking (FC)**

**Hill Climbing** — A steepest-descent local search that repeatedly moves to the neighboring board state with the fewest conflicts. It's implemented in the code (`A_loop`) but isn't currently wired to a button in the GUI — the app's menu only exposes Genetic Algorithm and Backtracking.

## Running it

Requires Python 3 with Tkinter (bundled with most Python installations; on some Linux distros you may need `sudo apt install python3-tk`). No other dependencies.

```bash
python Application.py
```

From the app window:
1. Choose **Genetic algorithm** or **backtracking**.
2. For backtracking, enter a board size (N) and tick whichever heuristics you want to combine, then click **Run backtrack**.
3. For the genetic algorithm, click **Run GA**.
4. The solved board and the time/iterations taken are displayed once a solution is found.

## Repo structure

```
.
├── Application.py   # GUI + all three solving algorithms
└── README.md
```

## Notes

- The genetic algorithm and hill climbing are hardcoded to 8-Queens; only backtracking generalizes to arbitrary N.
- `Application.py` is left as originally submitted for the course — only an explanatory header comment was added on top of it, no logic was changed.
