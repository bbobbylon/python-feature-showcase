#!/usr/bin/env python3
"""
main.py
========

The single entry point for the whole "Python Features Showcase" app.
Running this file gives you a menu to explore:

    1. A guided tour of core Python language features (printed to the terminal)
    2. A small Tkinter desktop GUI app (a to-do list)
    3. A menu of tiny playable terminal games

Why one entry point? In real Python projects, it's common to have a single
`main.py` (or a `__main__.py`) that ties together everything else, rather
than asking users to remember which file to run for which feature. This
also demonstrates the `if __name__ == "__main__":` pattern explained
below.

HOW TO RUN THIS APP
--------------------
From inside the `python-features-showcase/` folder, run:

    python3 main.py

Then follow the on-screen menu. See README.md for full setup instructions.
"""

from __future__ import annotations

import sys

# These imports pull in the "run_demo()" function from each module in the
# features/ package. Because features/__init__.py exists, Python treats
# that folder as a "package" we can import from.
from features import (
    basics_and_datatypes,
    collections_and_comprehensions,
    error_handling,
    functions_and_decorators,
    iterators_and_generators,
    modern_python,
    oop_showcase,
)
from games import number_guesser, rock_paper_scissors, tic_tac_toe

# A list of (menu label, function to call) pairs for the feature tour.
# Storing this as DATA (a list of tuples) rather than a long if/elif chain
# is itself a small demonstration of a Pythonic pattern: "code as data".
FEATURE_MODULES = [
    ("Variables, Data Types & Operators", basics_and_datatypes.run_demo),
    ("Lists, Dicts, Sets & Comprehensions", collections_and_comprehensions.run_demo),
    ("Functions & Decorators", functions_and_decorators.run_demo),
    ("Object-Oriented Programming (Classes)", oop_showcase.run_demo),
    ("Iterators & Generators", iterators_and_generators.run_demo),
    ("Error Handling & Context Managers", error_handling.run_demo),
    ("Modern Python (Type Hints, match/case)", modern_python.run_demo),
]

GAME_MODULES = [
    ("Guess the Number", number_guesser.play),
    ("Rock, Paper, Scissors", rock_paper_scissors.play),
    ("Tic-Tac-Toe (2 players)", tic_tac_toe.play),
]


def _print_menu(title: str, options: list[tuple[str, object]]) -> None:
    """Prints a numbered menu. Shared helper used by every menu in this app."""
    print(f"\n{title}")
    print("-" * len(title))
    for index, (label, _) in enumerate(options, start=1):
        print(f"  {index}. {label}")
    print("  0. Back")


def _choose(options: list[tuple[str, object]]) -> int | None:
    """
    Prompts for a menu choice and validates it. Returns the chosen index
    (0-based into `options`), or None if the user chose to go back.
    """
    choice = input("\nEnter a number: ").strip()
    if choice == "0":
        return None
    if not choice.isdigit() or not (1 <= int(choice) <= len(options)):
        print("Invalid choice, please try again.")
        return _choose(options)  # a small example of recursion for retrying input
    return int(choice) - 1


def run_feature_tour() -> None:
    """Lets the user pick a single feature module, or run all of them back to back."""
    while True:
        _print_menu("Python Feature Tour", FEATURE_MODULES + [("Run ALL of the above", None)])
        index = _choose(FEATURE_MODULES + [("Run ALL of the above", None)])
        if index is None:
            return

        if index == len(FEATURE_MODULES):  # the "Run ALL" option
            for _, demo_function in FEATURE_MODULES:
                demo_function()
        else:
            _, demo_function = FEATURE_MODULES[index]
            demo_function()

        input("\nPress Enter to return to the feature menu...")


def run_games_menu() -> None:
    """Lets the user pick a game to play, looping back to this menu after each game."""
    while True:
        _print_menu("Mini Games", GAME_MODULES)
        index = _choose(GAME_MODULES)
        if index is None:
            return
        _, play_function = GAME_MODULES[index]
        play_function()


def run_gui() -> None:
    """
    Launches the Tkinter GUI app. Imported LAZILY (inside the function,
    not at the top of the file) because tkinter requires a display/window
    system to be available -- importing it lazily means the rest of this
    CLI app still works fine in environments without a GUI (e.g. some
    remote servers or CI pipelines), and you only pay the import cost if
    you actually choose the GUI option.
    """
    try:
        from gui import todo_app
    except ImportError as error:
        print(f"Could not load the GUI (is tkinter installed on this system?): {error}")
        return

    try:
        todo_app.launch()
    except Exception as error:  # noqa: BLE001 - deliberately broad: any GUI backend issue
        print(f"The GUI failed to launch in this environment: {error}")
        print("This usually means there's no graphical display available "
              "(common in remote/headless environments/containers).")


def main() -> None:
    """The top-level menu loop that ties the whole app together."""
    print("=" * 60)
    print("  Welcome to the Python Features Showcase!")
    print("=" * 60)

    top_level_options = [
        ("Feature Tour (learn Python concepts)", run_feature_tour),
        ("Launch GUI To-Do App (tkinter)", run_gui),
        ("Play a Mini Game", run_games_menu),
    ]

    while True:
        _print_menu("Main Menu", top_level_options)
        index = _choose(top_level_options)
        if index is None:
            print("\nThanks for exploring Python! Goodbye. 👋")
            sys.exit(0)
        _, action = top_level_options[index]
        action()


# This is one of the most important idioms in Python. When you RUN a file
# directly (`python3 main.py`), Python sets a special variable called
# `__name__` to the string "__main__" for that file. But if this same file
# is IMPORTED by another file instead (`import main`), `__name__` is set
# to "main" instead. This `if` check means: "only start the interactive
# menu if this file was run directly -- don't start it just because
# something imported it." It's Python's equivalent of a `public static
# void main(String[] args)` entry point in Java, but opt-in per file.
if __name__ == "__main__":
    main()
