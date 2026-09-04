"""
basics_and_datatypes.py
========================

Demonstrates: variables, dynamic typing, core data types, operators,
f-strings (formatted string literals), and the walrus operator.

Analogy: In a statically-typed language (Java, C#), a variable is like a
labeled box that can ONLY ever hold one kind of thing -- you write
`int x = 5;` and that box is forever an "int box". In Python, a variable
is more like a sticky note you slap onto a value. The sticky note
(the name `x`) can be moved to point at a completely different kind of
value later. This is called "dynamic typing".
"""

from __future__ import annotations


def run_demo() -> None:
    """
    Run every mini-demo in this module, printing output with headers so the
    terminal reads like a guided tour. This function is the single entry
    point that main.py calls -- every module in features/ has one of these
    so the CLI can treat them all identically (this is a small example of
    a "consistent interface", a big idea in software design).
    """
    print("\n=== 1. Variables & Dynamic Typing ===")
    _demo_dynamic_typing()

    print("\n=== 2. Core Data Types ===")
    _demo_core_types()

    print("\n=== 3. Operators ===")
    _demo_operators()

    print("\n=== 4. f-strings (formatted string literals) ===")
    _demo_fstrings()

    print("\n=== 5. The Walrus Operator (:=) ===")
    _demo_walrus()


def _demo_dynamic_typing() -> None:
    """Show that one variable name can be reassigned to different types."""
    # `x` starts life as an integer.
    x = 5
    print(f"x = {x!r}  -> type is {type(x).__name__}")

    # Now we point the SAME name at a string. Python doesn't complain --
    # there's no compiler enforcing "x must always be an int".
    x = "now I'm a string!"
    print(f"x = {x!r}  -> type is {type(x).__name__}")

    # And now a list. The sticky-note analogy: the note moved, the old
    # value (5) is still valid Python, we just stopped pointing at it.
    x = [1, 2, 3]
    print(f"x = {x!r}  -> type is {type(x).__name__}")

    # Why this matters: it makes Python fast to prototype in, but it also
    # means typos in variable names or unexpected types are caught at
    # RUN time, not compile time. That's why tools like type hints
    # (see modern_python.py) and testing matter more in larger Python
    # projects.


def _demo_core_types() -> None:
    """Tour the built-in scalar types you'll use constantly."""
    an_int: int = 42
    a_float: float = 3.14159
    a_bool: bool = True
    a_string: str = "Python"
    none_value = None  # Python's "nothing here" value, like null/nil elsewhere

    for label, value in [
        ("int", an_int),
        ("float", a_float),
        ("bool", a_bool),
        ("str", a_string),
        ("NoneType", none_value),
    ]:
        print(f"  {label:<10} -> value={value!r:<15} type={type(value).__name__}")

    # Fun fact: in Python, `bool` is actually a subclass of `int`.
    # `True` behaves like 1 and `False` behaves like 0 in arithmetic.
    print(f"\n  True + True == {True + True}  (bool is secretly an int subclass)")


def _demo_operators() -> None:
    """Arithmetic, comparison, and the Python-specific operators."""
    a, b = 17, 5

    print(f"  {a} + {b}  = {a + b}")
    print(f"  {a} - {b}  = {a - b}")
    print(f"  {a} * {b}  = {a * b}")
    print(f"  {a} / {b}  = {a / b}   <- true division, ALWAYS returns a float")
    print(f"  {a} // {b} = {a // b}   <- floor division, rounds down to an int")
    print(f"  {a} % {b}  = {a % b}   <- modulo (remainder)")
    print(f"  {a} ** {b} = {a ** b}  <- exponent (a to the power of b)")

    # Comparison chaining: Python lets you chain comparisons the way you
    # would write them in math class. `1 < x < 10` reads exactly like
    # "1 is less than x, which is less than 10" -- most languages make
    # you write `1 < x and x < 10`.
    x = 7
    print(f"\n  Comparison chaining: 1 < {x} < 10 -> {1 < x < 10}")


def _demo_fstrings() -> None:
    """
    f-strings (introduced in Python 3.6) let you embed expressions directly
    inside string literals using {curly braces}. They are the modern,
    preferred way to build strings -- faster and more readable than the
    older `%` formatting or `.format()` methods.
    """
    name = "Ada"
    projects_completed = 12
    pi = 3.14159265

    print(f"  Hello, {name}!")
    print(f"  {name} has completed {projects_completed} projects.")
    # You can call functions and do arithmetic inline:
    print(f"  {name.upper()} has {projects_completed * 2} project-equivalents of experience.")
    # Formatting specifiers control number of decimals, padding, etc.
    print(f"  pi rounded to 2 decimals: {pi:.2f}")
    print(f"  right-aligned in a 10-char field: '{name:>10}'")


def _demo_walrus() -> None:
    """
    The walrus operator `:=` (added in Python 3.8) lets you assign a value
    to a variable AS PART OF a larger expression, instead of needing a
    separate line. It's named "walrus" because `:=` looks like a walrus's
    eyes and tusks.

    It's most useful for avoiding repeated computation inside conditions
    or loops.
    """
    data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    # Without the walrus operator, you'd have to compute `total` on one
    # line and then check it on the next:
    #     total = sum(data)
    #     if total > 30:
    #         print(total)
    #
    # With the walrus operator, you compute AND check in one breath:
    if (total := sum(data)) > 30:
        print(f"  The total {total} is greater than 30!")

    # Another common use: filtering a list while reusing a computed value.
    results = [y for x in data if (y := x * x) > 25]
    print(f"  Squares greater than 25: {results}")
