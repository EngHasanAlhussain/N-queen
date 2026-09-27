"""
Genetic algorithm solver.

This generalizes the original ``GA_fun`` / ``Genetic_loop`` (which only
worked for a hardcoded population of 8 lists representing an 8x8 board) to
any board size and population size, and replaces the original's 300+ line
wall of ``if y==0 and x==3: ... elif y==0 and x==2: ...`` selection logic
(one branch per pair of population indices) with a couple of list
operations that do the same thing: find the weakest individual and clone
the fittest one over it.

Algorithm, unchanged in spirit from the original:
    1. Start with a random population.
    2. Each generation, if any individual has zero conflicts, stop.
    3. Elitism: overwrite the single weakest individual with a copy of the
       single fittest one.
    4. Crossover: pair up individuals and swap a fixed tail segment,
       avoiding crossing an individual with an identical partner.
    5. Mutation: give every individual one randomly reset gene.
    6. If no solution is found within ``max_generations``, restart with a
       fresh random population (bounded by ``max_restarts`` so that calling
       this for an N with no solution -- e.g. N=2 or N=3 -- can't hang
       forever).
"""

from __future__ import annotations

import random
import time

from n_queens.board import count_conflicts, random_board
from n_queens.results import SolveResult


def _crossover_point(n: int) -> int:
    # The original used a fixed split around the 3rd/4th gene out of 8;
    # picking the midpoint generalizes that to any board size.
    return max(1, n // 2)


def _breed_generation(population: list[list[int]], rng: random.Random) -> None:
    """Elitism + crossover + mutation, applied in place."""
    n = len(population[0])
    fitnesses = [count_conflicts(individual) for individual in population]

    best = fitnesses.index(min(fitnesses))
    worst = fitnesses.index(max(fitnesses))
    if best != worst:
        population[worst] = population[best][:]

    point = _crossover_point(n)
    for i in range(0, len(population) - 1, 2):
        a, b = population[i], population[i + 1]
        if a == b:
            # crossing an individual with an identical copy of itself is a
            # no-op, so swap one side with a different member first
            other = (i + 2) % len(population)
            population[i], population[other] = population[other], population[i]
            a, b = population[i], population[i + 1]
        population[i] = a[:point] + b[point:]
        population[i + 1] = b[:point] + a[point:]

    for individual in population:
        gene = rng.randrange(n)
        individual[gene] = rng.randrange(n)


def solve_genetic(
    n: int = 8,
    population_size: int = 8,
    max_generations: int = 7000,
    max_restarts: int = 50,
    rng: random.Random | None = None,
) -> SolveResult:
    """Solve N-Queens with a genetic algorithm.

    Returns a :class:`SolveResult` whose ``steps`` is the total number of
    generations run across all restarts, and whose ``details`` includes the
    number of restarts used. ``solved`` is False if no solution was found
    within ``max_restarts`` attempts (this will always be the case for
    N == 2 or N == 3, which have no valid N-Queens solution).
    """
    rng = rng or random
    start = time.perf_counter()
    total_generations = 0
    best_board = None
    best_conflicts = None

    for restart in range(max_restarts):
        population = [random_board(n, rng) for _ in range(population_size)]
        for generation in range(max_generations):
            total_generations += 1
            fitnesses = [count_conflicts(individual) for individual in population]
            local_best = min(fitnesses)
            if best_conflicts is None or local_best < best_conflicts:
                best_conflicts = local_best
                best_board = population[fitnesses.index(local_best)][:]
            if local_best == 0:
                return SolveResult(
                    board=best_board,
                    solved=True,
                    algorithm="genetic",
                    steps=total_generations,
                    elapsed_seconds=time.perf_counter() - start,
                    details={"restarts": restart, "generation": generation},
                )
            _breed_generation(population, rng)

    return SolveResult(
        board=best_board,
        solved=False,
        algorithm="genetic",
        steps=total_generations,
        elapsed_seconds=time.perf_counter() - start,
        details={"restarts": max_restarts, "best_conflicts": best_conflicts},
    )
