"""
collections_and_comprehensions.py
==================================

Demonstrates: lists, tuples, dicts, sets, slicing, and comprehensions
(Python's compact syntax for building collections).

Analogy: If a variable is a sticky note on ONE value, a collection is a
labeled container holding MANY sticky notes.
    - list  -> a numbered shelf where order matters and items can repeat,
               and you can add/remove things (like a Word document's list
               of paragraphs).
    - tuple -> the same idea as a list, but sealed shut once created
               (like a printed receipt -- you can read it, not edit it).
    - dict  -> a lookup table / phone book: you look things up by a key
               ("name") to get a value ("phone number"), not by position.
    - set   -> a bag that automatically throws out duplicates and doesn't
               care about order -- great for "have I seen this before?"
               and set-math (union, intersection).
"""

from __future__ import annotations


def run_demo() -> None:
    """Entry point called by main.py -- see basics_and_datatypes.py for the pattern."""
    print("\n=== 1. Lists ===")
    _demo_lists()

    print("\n=== 2. Tuples ===")
    _demo_tuples()

    print("\n=== 3. Dictionaries ===")
    _demo_dicts()

    print("\n=== 4. Sets ===")
    _demo_sets()

    print("\n=== 5. Slicing ===")
    _demo_slicing()

    print("\n=== 6. Comprehensions (list/dict/set) ===")
    _demo_comprehensions()


def _demo_lists() -> None:
    """Lists are ordered, mutable (changeable), and allow duplicates."""
    fruits = ["apple", "banana", "cherry"]
    print(f"  Starting list: {fruits}")

    fruits.append("date")  # add to the end
    print(f"  After append('date'): {fruits}")

    fruits.insert(1, "apricot")  # insert at a specific position
    print(f"  After insert(1, 'apricot'): {fruits}")

    fruits.remove("banana")  # remove by value
    print(f"  After remove('banana'): {fruits}")

    print(f"  Length: {len(fruits)}")
    print(f"  Is 'cherry' in the list? {'cherry' in fruits}")


def _demo_tuples() -> None:
    """
    Tuples look like lists but are immutable -- once created, you cannot
    change their contents. This makes them useful for data that shouldn't
    change (coordinates, RGB colors) and as dictionary keys (lists can't be
    used as dict keys because they're mutable; tuples can).
    """
    point = (3, 7)
    print(f"  A 2D point as a tuple: {point}")

    # "Unpacking" -- assigning each element of the tuple to its own variable
    # in one line. Very idiomatic Python.
    x, y = point
    print(f"  Unpacked: x={x}, y={y}")

    try:
        point[0] = 99  # this will raise an error -- tuples can't be modified
    except TypeError as error:
        print(f"  Tried to modify a tuple and got an error (as expected): {error}")


def _demo_dicts() -> None:
    """
    Dictionaries (dicts) map keys to values, like a real-world dictionary
    maps a word to its definition. As of Python 3.7+, dicts also remember
    the order items were inserted in.
    """
    contact = {
        "name": "Grace Hopper",
        "role": "Computer Scientist",
        "languages": ["COBOL", "FORTRAN"],
    }
    print(f"  Full dict: {contact}")
    print(f"  Look up by key: contact['name'] -> {contact['name']}")

    # .get() is a safer lookup -- returns a default instead of crashing
    # if the key doesn't exist.
    print(f"  Safe lookup for missing key: contact.get('email', 'not provided')")
    print(f"    -> {contact.get('email', 'not provided')}")

    contact["email"] = "grace@example.com"  # dicts are mutable
    print(f"  After adding 'email': {contact}")

    print("  Iterating over key-value pairs:")
    for key, value in contact.items():
        print(f"    {key} -> {value}")


def _demo_sets() -> None:
    """
    Sets store unique, unordered items. They shine when you need to
    de-duplicate data or do math-class set operations.
    """
    team_a = {"Alice", "Bob", "Carol"}
    team_b = {"Bob", "Dave", "Eve"}

    print(f"  team_a: {team_a}")
    print(f"  team_b: {team_b}")
    print(f"  Union (everyone, no duplicates): {team_a | team_b}")
    print(f"  Intersection (on both teams): {team_a & team_b}")
    print(f"  Difference (only in team_a): {team_a - team_b}")

    numbers_with_dupes = [1, 2, 2, 3, 3, 3, 4]
    print(f"\n  De-duplicating a list via set(): {list(set(numbers_with_dupes))}")


def _demo_slicing() -> None:
    """
    Slicing lets you pull out a sub-section of a sequence (list, tuple,
    string) using `sequence[start:stop:step]`. `start` is inclusive,
    `stop` is exclusive -- a common gotcha for newcomers.
    """
    letters = list("abcdefghij")
    print(f"  Full list: {letters}")
    print(f"  letters[2:5]   (index 2 up to, not including, 5): {letters[2:5]}")
    print(f"  letters[:3]    (from the start up to index 3): {letters[:3]}")
    print(f"  letters[7:]    (from index 7 to the end): {letters[7:]}")
    print(f"  letters[::2]   (every 2nd element): {letters[::2]}")
    print(f"  letters[::-1]  (reversed -- a classic Python trick): {letters[::-1]}")


def _demo_comprehensions() -> None:
    """
    Comprehensions are Python's compact syntax for building a new list,
    dict, or set from an existing iterable, optionally filtering and
    transforming as you go.

    Analogy: A comprehension is a one-line factory line: it takes items in
    the front, transforms them and filters them, and puts finished items
    out the back, all described in a single readable statement.

    The equivalent "manual" loop is shown in a comment above each one so
    you can see exactly what the compact syntax replaces.
    """
    numbers = range(1, 11)  # 1 through 10

    # Manual loop equivalent of a list comprehension:
    #     squares = []
    #     for n in numbers:
    #         squares.append(n * n)
    squares = [n * n for n in numbers]
    print(f"  List comprehension - squares 1-10: {squares}")

    # A comprehension with a filter (the `if` clause at the end):
    #     even_squares = []
    #     for n in numbers:
    #         if n % 2 == 0:
    #             even_squares.append(n * n)
    even_squares = [n * n for n in numbers if n % 2 == 0]
    print(f"  Filtered - squares of even numbers only: {even_squares}")

    # Dict comprehension: build a dict mapping each number to its square.
    square_lookup = {n: n * n for n in range(1, 6)}
    print(f"  Dict comprehension - number -> square: {square_lookup}")

    # Set comprehension: unique word lengths in a sentence.
    words = "the quick brown fox jumps over the lazy dog".split()
    word_lengths = {len(word) for word in words}
    print(f"  Set comprehension - unique word lengths: {word_lengths}")

    # Nested comprehension: flatten a 2D grid into a single list.
    grid = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    flattened = [value for row in grid for value in row]
    print(f"  Nested comprehension - flattened grid: {flattened}")
