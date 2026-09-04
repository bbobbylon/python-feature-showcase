"""
functions_and_decorators.py
============================

Demonstrates: function definitions, default arguments, *args/**kwargs,
lambdas, first-class functions, map/filter/functools.reduce, and
decorators.

Analogy for decorators (the trickiest concept here): a decorator is like
gift wrapping for a function. The function is the gift itself; the
decorator wraps extra behavior AROUND it (logging, timing, checking
permissions) WITHOUT you having to unwrap the gift and change what's
inside. You can put the same wrapping paper on many different gifts.
"""

from __future__ import annotations

import functools
import time
from typing import Callable


def run_demo() -> None:
    print("\n=== 1. Default Arguments ===")
    _demo_default_args()

    print("\n=== 2. *args and **kwargs ===")
    _demo_args_kwargs()

    print("\n=== 3. Functions Are First-Class Citizens ===")
    _demo_first_class_functions()

    print("\n=== 4. Lambda (anonymous functions) ===")
    _demo_lambdas()

    print("\n=== 5. map(), filter(), functools.reduce() ===")
    _demo_functional_tools()

    print("\n=== 6. Decorators ===")
    _demo_decorators()


def _greet(name: str, greeting: str = "Hello") -> str:
    """A function with a default argument -- `greeting` is optional."""
    return f"{greeting}, {name}!"


def _demo_default_args() -> None:
    """Default argument values let callers omit parameters they don't need."""
    print(f"  {_greet('World')}")  # uses the default greeting
    print(f"  {_greet('World', greeting='Howdy')}")  # overrides the default


def _sum_everything(*args: float, **kwargs: float) -> None:
    """
    `*args` collects any number of extra positional arguments into a tuple.
    `**kwargs` ("keyword arguments") collects any number of extra
    name=value arguments into a dict.

    Analogy: think of `*args` as an open box for "however many unlabeled
    items you hand me" and `**kwargs` as an open box for "however many
    LABELED items you hand me".
    """
    print(f"  args received as a tuple: {args}  -> sum = {sum(args)}")
    print(f"  kwargs received as a dict: {kwargs}  -> sum = {sum(kwargs.values())}")


def _demo_args_kwargs() -> None:
    _sum_everything(1, 2, 3, 4)
    _sum_everything(rent=1200, groceries=300, gas=60)
    _sum_everything(1, 2, extra_bonus=50)  # you can even mix both


def _apply_twice(func: Callable[[int], int], value: int) -> int:
    """
    Demonstrates that functions are "first-class citizens" in Python --
    you can pass a function into another function as if it were any
    other value (an int, a string, etc.), and call it later.
    """
    return func(func(value))


def _double(n: int) -> int:
    return n * 2


def _demo_first_class_functions() -> None:
    result = _apply_twice(_double, 5)
    print(f"  Passing the function `_double` into `_apply_twice(_double, 5)`: {result}")
    print("  (5 -> doubled to 10 -> doubled again to 20)")


def _demo_lambdas() -> None:
    """
    A `lambda` is a small, anonymous (unnamed), single-expression function.
    Use them for short throwaway logic, especially as arguments to other
    functions like `sorted()`. For anything more than one line, prefer a
    normal `def` function -- it's more readable and debuggable.
    """
    square = lambda n: n * n  # equivalent to: def square(n): return n * n
    print(f"  lambda square(6) = {square(6)}")

    people = [
        {"name": "Zoe", "age": 25},
        {"name": "Adam", "age": 40},
        {"name": "Mia", "age": 30},
    ]
    # `key=lambda person: person["age"]` tells sorted() HOW to compare items.
    by_age = sorted(people, key=lambda person: person["age"])
    print(f"  People sorted by age using a lambda key: {[p['name'] for p in by_age]}")


def _demo_functional_tools() -> None:
    """
    map(), filter(), and functools.reduce() are "functional programming"
    tools borrowed from languages like Lisp/Haskell. In modern Python,
    comprehensions (see collections_and_comprehensions.py) are often
    preferred for readability, but you'll still see these in the wild.
    """
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    # map(function, iterable) -> applies `function` to every item.
    doubled = list(map(lambda n: n * 2, numbers))
    print(f"  map() to double every number: {doubled}")

    # filter(function, iterable) -> keeps only items where `function` returns True.
    evens = list(filter(lambda n: n % 2 == 0, numbers))
    print(f"  filter() to keep only even numbers: {evens}")

    # functools.reduce(function, iterable) -> combines all items into one
    # value by repeatedly applying `function` to a running total.
    total = functools.reduce(lambda running_total, n: running_total + n, numbers)
    print(f"  functools.reduce() to sum everything: {total}")


def timer(func: Callable) -> Callable:
    """
    A decorator that measures and prints how long the wrapped function
    took to run.

    How decorators work, step by step:
    1. `func` is the original function being decorated (e.g. `slow_countdown`).
    2. We define `wrapper`, a new function that calls `func` but adds
       extra behavior (timing) before/after.
    3. We return `wrapper` -- so when someone calls the decorated function,
       they're actually calling `wrapper`, which calls the original `func`
       inside it.
    4. `@functools.wraps(func)` preserves the original function's name and
       docstring, which is good practice so debugging tools aren't confused.
    """

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed = time.perf_counter() - start
        print(f"    [timer] '{func.__name__}' took {elapsed:.4f} seconds")
        return result

    return wrapper


@timer  # <-- this line is equivalent to: slow_countdown = timer(slow_countdown)
def _slow_countdown(n: int) -> None:
    """A deliberately slow function so the @timer decorator has something to measure."""
    for i in range(n, 0, -1):
        time.sleep(0.05)  # simulate work
    print(f"    Countdown from {n} finished!")


def _demo_decorators() -> None:
    print("  Calling a function wrapped with @timer:")
    _slow_countdown(5)
    print(
        "\n  Notice we never edited `_slow_countdown`'s body to add timing logic --"
        "\n  the @timer decorator added that behavior from the outside."
    )
