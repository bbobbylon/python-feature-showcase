"""
error_handling.py
==================

Demonstrates: try/except/else/finally, catching specific exceptions,
raising your own exceptions, custom exception classes, and context
managers (the `with` statement).

Analogy: `try`/`except` is a safety net under a tightrope walker. The
`try` block is the tightrope walk (code that MIGHT go wrong); the
`except` block is the net that catches a specific KIND of fall. `finally`
is the cleanup crew that shows up no matter what happened -- successful
walk or a fall into the net.
"""

from __future__ import annotations

from contextlib import contextmanager
from typing import Iterator


def run_demo() -> None:
    print("\n=== 1. Basic try/except ===")
    _demo_basic_try_except()

    print("\n=== 2. try/except/else/finally (all four blocks) ===")
    _demo_full_try_except()

    print("\n=== 3. Catching Multiple / Specific Exception Types ===")
    _demo_specific_exceptions()

    print("\n=== 4. Custom Exceptions ===")
    _demo_custom_exceptions()

    print("\n=== 5. Context Managers (the `with` statement) ===")
    _demo_context_managers()


def _demo_basic_try_except() -> None:
    """The simplest form: attempt something risky, handle the failure."""
    numbers = ["10", "20", "not-a-number", "40"]

    for text in numbers:
        try:
            value = int(text)  # this raises ValueError if `text` isn't numeric
        except ValueError:
            print(f"  '{text}' is not a valid number -- skipping it.")
        else:
            # Only runs if int() DIDN'T raise -- keeps the "happy path"
            # separate from error handling, which is good practice.
            print(f"  '{text}' converted successfully to {value}")


def _demo_full_try_except() -> None:
    """
    All four blocks together:
      try:     the risky code
      except:  runs only if an exception occurred
      else:    runs only if NO exception occurred
      finally: ALWAYS runs, exception or not (great for cleanup)
    """

    def divide(a: float, b: float) -> None:
        try:
            result = a / b
        except ZeroDivisionError:
            print(f"    Cannot divide {a} by zero!")
        else:
            print(f"    {a} / {b} = {result}")
        finally:
            print(f"    (finished attempting to divide {a} by {b})")

    divide(10, 2)
    divide(10, 0)


def _demo_specific_exceptions() -> None:
    """
    Catch the MOST SPECIFIC exception type you can, rather than a bare
    `except:`, so you don't accidentally swallow bugs you didn't expect.
    You can also catch several types at once with a tuple.
    """
    risky_operations = [
        lambda: 1 / 0,  # raises ZeroDivisionError
        lambda: [1, 2, 3][10],  # raises IndexError
        lambda: {"a": 1}["missing-key"],  # raises KeyError
        lambda: int("oops"),  # raises ValueError
    ]

    for operation in risky_operations:
        try:
            operation()
        except (ZeroDivisionError, IndexError) as error:
            print(f"  Caught a math/index problem: {type(error).__name__}: {error}")
        except (KeyError, ValueError) as error:
            print(f"  Caught a data problem: {type(error).__name__}: {error}")


class InsufficientFundsError(Exception):
    """
    A custom exception. Inheriting from `Exception` (Python's base error
    class) means our new error type gets all the standard exception
    behavior (it can be raised, caught, carries a message) while letting
    calling code catch it SPECIFICALLY, separate from generic errors.
    """

    def __init__(self, requested: float, available: float) -> None:
        self.requested = requested
        self.available = available
        message = f"Tried to withdraw ${requested:.2f} but only ${available:.2f} is available."
        super().__init__(message)


class BankAccount:
    """A tiny class used to demonstrate `raise` with a custom exception."""

    def __init__(self, balance: float) -> None:
        self.balance = balance

    def withdraw(self, amount: float) -> None:
        if amount > self.balance:
            # `raise` throws the exception up to whoever called this method.
            raise InsufficientFundsError(requested=amount, available=self.balance)
        self.balance -= amount


def _demo_custom_exceptions() -> None:
    account = BankAccount(balance=100.0)

    try:
        account.withdraw(250.0)
    except InsufficientFundsError as error:
        print(f"  Custom exception caught: {error}")
        print(f"  We can also inspect its specific attributes: requested=${error.requested}, available=${error.available}")


@contextmanager
def timed_section(label: str) -> Iterator[None]:
    """
    A context manager built with the `@contextmanager` decorator. Code
    before `yield` runs when entering the `with` block; code after `yield`
    runs when leaving it -- even if an exception happened inside.

    Analogy: a context manager is like a hotel check-in/check-out process.
    "Entering" (check-in) sets things up; "exiting" (check-out) always
    happens, guaranteeing cleanup, whether the guest's stay was smooth or
    a disaster.
    """
    import time

    start = time.perf_counter()
    print(f"    [enter] starting '{label}'")
    try:
        yield  # control passes to the code inside the `with` block here
    finally:
        elapsed = time.perf_counter() - start
        print(f"    [exit]  '{label}' finished in {elapsed:.4f}s (cleanup always runs)")


def _demo_context_managers() -> None:
    """
    The most common context manager you'll see is `open()` for files:
        with open("file.txt") as f:
            contents = f.read()
        # the file is automatically closed here, even if read() raised an error

    Below, we use our own custom context manager to show the same
    guaranteed-cleanup pattern without needing an actual file.
    """
    with timed_section("a quick calculation"):
        total = sum(range(1_000_000))
        print(f"    calculated a sum of {total} inside the `with` block")

    print("\n  Now let's see cleanup still happen even when an error occurs inside the block:")
    try:
        with timed_section("a calculation that fails"):
            raise RuntimeError("something went wrong inside the with block")
    except RuntimeError as error:
        print(f"  Caught the error after the context manager cleaned up: {error}")
