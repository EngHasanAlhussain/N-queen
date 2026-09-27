"""
Tkinter GUI for the N-Queens solvers.

This keeps the same idea as the original ``Application.py`` window (pick an
algorithm, optionally tick some heuristics, see the solved board and how
long it took) but is a single class instead of a dozen functions mutating
module-level globals, and it drives the solver functions in
``n_queens.genetic``, ``n_queens.hill_climbing`` and ``n_queens.backtracking``
instead of duplicating that logic inline.

One behavior change from the original: the board size (N) applies to all
three algorithms here, not just backtracking -- the genetic algorithm and
hill climbing were only ever hardcoded to 8 because the original code
built each candidate board by hand as 8 separate variables; now that they
work on plain lists, there's no reason to special-case 8.
"""

from __future__ import annotations

import tkinter as tk
from tkinter import messagebox

from n_queens.backtracking import solve_backtracking
from n_queens.genetic import solve_genetic
from n_queens.hill_climbing import solve_hill_climbing_with_restarts
from n_queens.results import SolveResult

BG = "#6b868e"
ACCENT = "#478e2c"
TEXT_DARK = "#371e86"
TITLE_COLOR = "#f60b86"
STATUS_COLOR = "#febe00"
BOARD_LIGHT = "#e8e8e8"
BOARD_DARK = "#3a3a3a"
QUEEN_COLOR = "#b5121b"


class NQueensApp:
    def __init__(self, root: tk.Tk):
        self.root = root
        root.title("N-Queens Solver")
        root.configure(bg=BG)

        self.heuristic_vars = {
            "mrv": tk.BooleanVar(),
            "mcv": tk.BooleanVar(),
            "lcv": tk.BooleanVar(),
            "forward_checking": tk.BooleanVar(),
            "arc_consistency": tk.BooleanVar(),
        }

        self._build_controls()
        self._build_board_area()
        self._build_status_area()

    # -- layout -----------------------------------------------------------

    def _build_controls(self) -> None:
        controls = tk.Frame(self.root, bg=BG)
        controls.grid(row=0, column=0, sticky="n", padx=16, pady=16)

        tk.Label(
            controls,
            text="N-Queens Solver",
            font=("Arial", 20, "bold"),
            bg=BG,
            fg=TITLE_COLOR,
        ).grid(row=0, column=0, columnspan=2, pady=(0, 12))

        tk.Label(controls, text="Board size (N):", font=("Arial", 12), bg=BG, fg=TEXT_DARK).grid(
            row=1, column=0, sticky="w"
        )
        self.n_var = tk.IntVar(value=8)
        tk.Entry(controls, textvariable=self.n_var, font=("Arial", 12), width=6).grid(
            row=1, column=1, sticky="w"
        )

        tk.Button(
            controls,
            text="Genetic Algorithm",
            font=("Arial", 12, "bold"),
            bg=ACCENT,
            fg="white",
            command=self.run_genetic,
        ).grid(row=2, column=0, columnspan=2, sticky="ew", pady=(12, 4))

        tk.Button(
            controls,
            text="Hill Climbing (random restarts)",
            font=("Arial", 12, "bold"),
            bg=ACCENT,
            fg="white",
            command=self.run_hill_climbing,
        ).grid(row=3, column=0, columnspan=2, sticky="ew", pady=4)

        tk.Label(
            controls,
            text="Backtracking heuristics:",
            font=("Arial", 12),
            bg=BG,
            fg=TEXT_DARK,
        ).grid(row=4, column=0, columnspan=2, sticky="w", pady=(12, 0))

        labels = {
            "mrv": "Minimum Remaining Values (MRV)",
            "mcv": "Most Constraining Variable (MCV)",
            "lcv": "Least Constraining Value (LCV)",
            "forward_checking": "Forward Checking (FC)",
            "arc_consistency": "Arc Consistency (AC)",
        }
        row = 5
        for key, label in labels.items():
            tk.Checkbutton(
                controls,
                text=label,
                variable=self.heuristic_vars[key],
                font=("Arial", 11),
                bg=BG,
                fg=TEXT_DARK,
                anchor="w",
            ).grid(row=row, column=0, columnspan=2, sticky="w")
            row += 1

        tk.Button(
            controls,
            text="Run Backtracking",
            font=("Arial", 12, "bold"),
            bg=ACCENT,
            fg="white",
            command=self.run_backtracking,
        ).grid(row=row, column=0, columnspan=2, sticky="ew", pady=(8, 0))

    def _build_board_area(self) -> None:
        self.board_frame = tk.Frame(self.root, bg=BG)
        self.board_frame.grid(row=0, column=1, padx=16, pady=16)

    def _build_status_area(self) -> None:
        self.status_label = tk.Label(
            self.root,
            text="Choose an algorithm to begin.",
            font=("Arial", 12),
            bg=BG,
            fg=STATUS_COLOR,
            justify="left",
        )
        self.status_label.grid(row=1, column=0, columnspan=2, sticky="w", padx=16, pady=(0, 16))

    # -- board size -------------------------------------------------------

    def _get_n(self) -> int | None:
        try:
            n = int(self.n_var.get())
        except (tk.TclError, ValueError):
            messagebox.showerror("Invalid input", "Board size (N) must be a whole number.")
            return None
        if n < 1:
            messagebox.showerror("Invalid input", "Board size (N) must be at least 1.")
            return None
        return n

    # -- algorithm actions --------------------------------------------------

    def run_genetic(self) -> None:
        n = self._get_n()
        if n is None:
            return
        self.status_label.config(text=f"Running genetic algorithm for N={n} ...")
        self.root.update_idletasks()
        result = solve_genetic(n)
        self._show_result(result)

    def run_hill_climbing(self) -> None:
        n = self._get_n()
        if n is None:
            return
        self.status_label.config(text=f"Running hill climbing for N={n} ...")
        self.root.update_idletasks()
        result = solve_hill_climbing_with_restarts(n)
        self._show_result(result)

    def run_backtracking(self) -> None:
        n = self._get_n()
        if n is None:
            return
        flags = {key: var.get() for key, var in self.heuristic_vars.items()}
        self.status_label.config(text=f"Running backtracking for N={n} ...")
        self.root.update_idletasks()
        result = solve_backtracking(n, **flags)
        self._show_result(result)

    # -- rendering ----------------------------------------------------------

    def _show_result(self, result: SolveResult) -> None:
        if result.board:
            self._render_board(result.board)
        outcome = "Solved" if result.solved else "No solution found"
        details = ", ".join(f"{k}={v}" for k, v in result.details.items())
        self.status_label.config(
            text=(
                f"[{result.algorithm}] {outcome} in {result.elapsed_seconds:.4f}s "
                f"({result.steps} steps). {details}"
            )
        )

    def _render_board(self, board: list[int]) -> None:
        for widget in self.board_frame.winfo_children():
            widget.destroy()

        n = len(board)
        cell_size = max(24, min(56, 480 // n))
        for col in range(n):
            for row in range(n):
                is_queen = board[col] == row
                color = BOARD_LIGHT if (row + col) % 2 == 0 else BOARD_DARK
                text = "Q" if is_queen else ""
                fg = QUEEN_COLOR if is_queen else color
                tk.Label(
                    self.board_frame,
                    text=text,
                    width=2,
                    height=1,
                    font=("Arial", max(10, cell_size // 3), "bold"),
                    bg=color,
                    fg=fg,
                    relief="solid",
                    borderwidth=1,
                ).grid(row=row, column=col)


def main() -> None:
    root = tk.Tk()
    NQueensApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
