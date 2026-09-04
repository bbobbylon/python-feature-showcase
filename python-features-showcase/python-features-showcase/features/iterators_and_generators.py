"""
iterators_and_generators.py
============================

Demonstrates: the iterator protocol, generator functions (`yield`),
generator expressions, and handy tools from `itertools`.

Analogy: A regular function is like baking an entire tray of cookies and
handing you the whole tray at once (all the results, computed immediately,
sitting in memory). A generator is like a cookie machine that hands you
ONE cookie at a time, only baking the next one when you ask for it. This
means generators can represent sequences that are huge (or even infinite)
without ever needing to hold them all in memory at once.
"""

from __future__ import annotations

import itertools
from typing import Iterator


def run_demo() -> None:
    print("\n=== 1. The Iterator Protocol (for loops, under the hood) ===")
    _demo_iterator_protocol()

    print("\n=== 2. Generator Functions (yield) ===")
    _demo_generator_function()

    print("\n=== 3. Generator Expressions ===")
    _demo_generator_expression()

    print("\n=== 4. itertools ===")
    _demo_itertools()


def _demo_iterator_protocol() -> None:
    """
    Every time you write `for item in some_list:`, Python is doing this
    behind the scenes:
        iterator = iter(some_list)   # get an iterator from the list
        while True:
            try:
                item = next(iterator)  # ask for the next item
            except StopIteration:
                break                   # no more items -- stop looping
    """
    fruits = ["apple", "banana", "cherry"]
    iterator = iter(fruits)

    print("  Manually pulling items with next() instead of using a for-loop:")
    print(f"    next(iterator) -> {next(iterator)}")
    print(f"    next(iterator) -> {next(iterator)}")
    print(f"    next(iterator) -> {next(iterator)}")
    try:
        next(iterator)
    except StopIteration:
        print("    next(iterator) -> raised StopIteration (no items left)")


def countdown(start: int) -> Iterator[int]:
    """
    A GENERATOR FUNCTION. Notice it uses `yield` instead of `return`.
    Each time the caller asks for the next value, this function's code
    runs UP TO the next `yield`, hands back that value, and then PAUSES --
    its local variables (like `start`) are preserved until the next
    request. This is fundamentally different from `return`, which exits
    the function completely.
    """
    print(f"    (generator starting at {start})")
    while start > 0:
        yield start
        start -= 1
    print("    (generator finished)")


def _demo_generator_function() -> None:
    print("  Consuming a generator with a for-loop (each print interleaves with the generator running):")
    for number in countdown(3):
        print(f"    got: {number}")

    print("\n  Generators are 'lazy' -- creating one does no work yet:")
    gen = countdown(1_000_000)  # instant, even though it "counts down" a million numbers
    print(f"    gen created: {gen!r}  <- no numbers computed yet!")
    print(f"    first value pulled with next(gen): {next(gen)}")


def _demo_generator_expression() -> None:
    """
    A generator EXPRESSION looks just like a list comprehension but with
    parentheses instead of square brackets. It produces a generator
    (lazy, memory-efficient) instead of a fully-built list.
    """
    numbers = range(1, 1_000_001)  # a million numbers

    # This builds a full million-item list in memory immediately:
    list_version = [n * n for n in numbers]
    # This creates a generator that computes each square ON DEMAND:
    generator_version = (n * n for n in numbers)

    print(f"  List comprehension result type: {type(list_version).__name__} (all 1,000,000 squares computed now)")
    print(f"  Generator expression result type: {type(generator_version).__name__} (nothing computed yet)")
    print(f"  Pulling just the first value from the generator: {next(generator_version)}")
    print("  This is why generators are great for huge datasets or streams -- you only pay for what you use.")


def _demo_itertools() -> None:
    """
    The `itertools` module (part of Python's standard library) provides
    battle-tested building blocks for working with iterators.
    """
    # itertools.count() is an INFINITE generator -- always pair it with
    # something like itertools.islice() or a manual break condition.
    first_five_evens = list(itertools.islice(itertools.count(0, step=2), 5))
    print(f"  itertools.count(0, step=2) sliced to 5 items: {first_five_evens}")

    # itertools.chain() links multiple iterables into one continuous stream.
    combined = list(itertools.chain([1, 2], ["a", "b"], (True, False)))
    print(f"  itertools.chain() combining a list, a list, and a tuple: {combined}")

    # itertools.cycle() repeats a sequence forever -- again, slice it.
    cycled = list(itertools.islice(itertools.cycle(["rock", "paper", "scissors"]), 7))
    print(f"  itertools.cycle() sliced to 7 items: {cycled}")

    # itertools.groupby() groups consecutive items sharing a key.
    scores = [("Alice", 90), ("Alice", 85), ("Bob", 70), ("Bob", 75), ("Carol", 60)]
    print("  itertools.groupby() grouping consecutive same-name entries:")
    for name, group in itertools.groupby(scores, key=lambda pair: pair[0]):
        points = [score for _, score in group]
        print(f"    {name}: {points}")
