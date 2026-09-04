"""
modern_python.py
=================

Demonstrates: type hints, the `match`/`case` statement (structural pattern
matching, added in Python 3.10), and unpacking tricks.

Analogy for type hints: think of them as LABELS on the outside of the
sticky-note boxes from basics_and_datatypes.py. Python still won't force
the box to only hold that type (that's the "dynamic typing" trade-off),
but the labels let humans AND tools (like the `mypy` type checker, or
your editor's autocomplete) understand your intent and catch mistakes
before you even run the code.
"""

from __future__ import annotations


def run_demo() -> None:
    print("\n=== 1. Type Hints ===")
    _demo_type_hints()

    print("\n=== 2. match/case (structural pattern matching) ===")
    _demo_match_case()

    print("\n=== 3. Extended Unpacking ===")
    _demo_extended_unpacking()


def add(a: int, b: int) -> int:
    """
    A type-hinted function: `a: int` and `b: int` say "these should be
    ints"; `-> int` says "this function returns an int". These hints are
    NOT enforced at runtime by Python itself -- they're documentation and
    tooling support. If you want them enforced, you'd run a separate tool
    like `mypy` against your code.
    """
    return a + b


def _demo_type_hints() -> None:
    print(f"  add(2, 3) -> {add(2, 3)}")

    # Python will NOT stop you from doing this, even though the hints say
    # `int`. This is the key difference from a statically-typed language.
    result = add("2", "3")  # type: ignore -- strings support + too (concatenation)!
    print(f"  add('2', '3') -> {result!r}  (Python let this through -- hints aren't enforced at runtime)")

    # More advanced hints: Optional, list of a type, dict of types.
    from typing import Optional

    def find_user(user_id: int, users: dict[int, str]) -> Optional[str]:
        """`Optional[str]` means 'a str, or None'. This documents that the
        function might not find a match."""
        return users.get(user_id)

    directory = {1: "Alice", 2: "Bob"}
    print(f"  find_user(1, directory) -> {find_user(1, directory)!r}")
    print(f"  find_user(99, directory) -> {find_user(99, directory)!r}")


def _describe_http_status(code: int) -> str:
    """
    `match`/`case` is Python's version of a "switch statement", but more
    powerful -- it can match on VALUE, TYPE, and STRUCTURE (like unpacking
    a specific shape out of a list or object), not just simple equality.

    Analogy: think of it like a bouncer at a club checking IDs against a
    list of patterns -- "if you're exactly 21, go here; if you're in this
    age range, go there; otherwise, general line."
    """
    match code:
        case 200:
            return "OK"
        case 404:
            return "Not Found"
        case 500:
            return "Internal Server Error"
        case code if 400 <= code < 500:
            # a "guard" clause -- matches any code in this range
            return "Some other client error"
        case _:
            # `_` is the wildcard -- matches anything not caught above,
            # similar to `default:` in other languages' switch statements.
            return "Unknown status code"


def _demo_match_case() -> None:
    for code in [200, 404, 418, 500, 999]:
        print(f"  status {code} -> {_describe_http_status(code)}")

    # match/case can also destructure data structures by shape:
    def describe_point(point: tuple) -> str:
        match point:
            case (0, 0):
                return "the origin"
            case (0, y):
                return f"on the y-axis at y={y}"
            case (x, 0):
                return f"on the x-axis at x={x}"
            case (x, y):
                return f"a point at ({x}, {y})"
            case _:
                return "not a 2D point"

    print("\n  match/case destructuring tuples by shape:")
    for point in [(0, 0), (0, 5), (3, 0), (2, 4), "not-a-tuple"]:
        print(f"    {point!r:<20} -> {describe_point(point)}")


def _demo_extended_unpacking() -> None:
    """
    The `*` (star) operator in an assignment lets you grab "the rest" of a
    sequence into a list, similar to how it collects extra function
    arguments in *args (see functions_and_decorators.py).
    """
    scores = [100, 85, 90, 76, 88, 95]

    first, *middle, last = scores
    print(f"  scores = {scores}")
    print(f"  first, *middle, last = scores  ->  first={first}, middle={middle}, last={last}")

    head, *tail = scores
    print(f"  head, *tail = scores  ->  head={head}, tail={tail}")

    # Star unpacking is also handy for merging collections:
    a = [1, 2, 3]
    b = [4, 5, 6]
    merged = [*a, *b, 999]
    print(f"  [*a, *b, 999] merges two lists plus an extra value: {merged}")
