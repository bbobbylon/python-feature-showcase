# Python Features Showcase

A learning-focused Python project with **no external dependencies** (it
only uses Python's standard library). It exists to demonstrate what makes
Python "Python" -- the language features and idioms that make it distinct
from languages like Java, C#, or JavaScript.

This app has three parts, all reachable from one menu:

1. **Feature Tour** -- a guided, printed walkthrough of core Python
   concepts (variables, data structures, functions, OOP, generators,
   error handling, and modern syntax).
2. **GUI To-Do App** -- a small desktop window app built with `tkinter`
   (Python's built-in GUI toolkit), showing that Python isn't limited to
   the terminal.
3. **Mini Games** -- three tiny playable terminal games (Guess the
   Number, Rock-Paper-Scissors, Tic-Tac-Toe), each chosen to highlight a
   different set of features in a low-stakes, fun way.

If you're new to Python: think of Python as a language that optimizes for
**reading and writing code quickly**, often at the cost of the stricter
guardrails you get in languages like Java or C++. It uses **indentation**
(whitespace) instead of `{curly braces}` to mark code blocks -- that's not
a style choice, it's required syntax. You'll see this in every file here.

## Project Structure

```
python-features-showcase/
├── main.py                       # single entry point -- run this file
├── features/                     # the "Feature Tour" content
│   ├── basics_and_datatypes.py       # variables, types, operators, f-strings
│   ├── collections_and_comprehensions.py  # lists, dicts, sets, comprehensions
│   ├── functions_and_decorators.py   # functions, *args/**kwargs, decorators
│   ├── oop_showcase.py               # classes, inheritance, dataclasses
│   ├── iterators_and_generators.py   # generators, yield, itertools
│   ├── error_handling.py             # try/except, custom exceptions, context managers
│   └── modern_python.py              # type hints, match/case, unpacking
├── gui/
│   └── todo_app.py                # tkinter desktop GUI demo
├── games/
│   ├── number_guesser.py
│   ├── rock_paper_scissors.py
│   └── tic_tac_toe.py
└── README.md
```

Every module has a `run_demo()` (or `play()` / `launch()`) function that
`main.py` calls -- this "consistent interface" pattern is what lets
`main.py` treat every module the same way without needing to know its
internal details.

## Prerequisites

- **Python 3.10 or newer** (this project uses `match`/`case`, added in
  3.10, and modern type-hint syntax). Check your version with:

  ```bash
  python3 --version
  ```

  If you don't have Python installed, download it from
  [python.org/downloads](https://www.python.org/downloads/) (macOS/Windows)
  or install it via your Linux distribution's package manager
  (e.g. `sudo apt install python3` on Ubuntu/Debian).

- **tkinter** for the GUI option. On Windows and macOS, tkinter ships
  with the standard Python installer, so there's nothing extra to do. On
  Linux, you may need to install it separately, e.g.:

  ```bash
  sudo apt install python3-tk       # Debian/Ubuntu
  sudo dnf install python3-tkinter  # Fedora
  ```

  If tkinter isn't available, everything else in the app (the feature
  tour and the games) still works fine -- `main.py` catches that error
  gracefully and tells you.

No `pip install` is required for this project -- it's 100% standard
library, on purpose, so there's nothing to break or version-mismatch.

## Running Locally

1. Download or clone this folder onto your computer.
2. Open a terminal and navigate into the project folder:

   ```bash
   cd python-features-showcase
   ```

3. Run the app:

   ```bash
   python3 main.py
   ```

   (On Windows, you may need to use `python` instead of `python3`,
   depending on how Python was installed.)

4. Use the on-screen numbered menu to explore. Type `0` at any menu to go
   back, and `q` to quit out of a game early.

You can also run any single module directly to jump straight to it, since
each one has its own `if __name__ == "__main__":` block, for example:

```bash
python3 -m games.tic_tac_toe
python3 -m features.oop_showcase
python3 gui/todo_app.py
```

## "Deploying" a Script-Based App

Unlike a web app, a terminal/GUI Python app like this one doesn't get
"deployed" to a server -- it's distributed to run on someone's own
machine. Here are the realistic ways to share or "ship" it:

### Option A: Share the source code (simplest)

Anyone with Python 3.10+ installed can run it exactly as described above.
This is the standard way small Python tools and scripts are shared.

### Option B: Package it as a standalone executable

Tools like [PyInstaller](https://pyinstaller.org/) bundle your script AND
a Python interpreter into a single executable file, so someone without
Python installed can still run it.

```bash
pip install pyinstaller --break-system-packages   # one-time setup
pyinstaller --onefile main.py
# the executable will be created in a new dist/ folder
```

### Option C: Publish it to PyPI (the Python Package Index)

If you wanted other Python developers to `pip install` your project as a
reusable package (more relevant for libraries than end-user apps like
this one), you'd add a `pyproject.toml` describing the package and
publish it with a tool like [`twine`](https://twine.readthedocs.io/).
That's a bigger step than this project needs today, but it's the natural
next stage if this ever grows into a library other code depends on.

### Continuous Integration (CI) for a project like this

Even without a server to deploy to, it's good practice to automatically
check that the code still runs correctly every time you push a change.
A simple GitHub Actions workflow for this project might live at
`.github/workflows/ci.yml` and look like:

```yaml
name: CI
on: [push, pull_request]
jobs:
  smoke-test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: "3.11"
      - name: Import-check every module (catches syntax errors)
        run: |
          python -c "import ast, pathlib
          for f in pathlib.Path('.').rglob('*.py'):
              ast.parse(f.read_text())
          print('All files parse successfully.')"
```

This isn't included in the project by default (it needs a GitHub
repository to run in), but it's a template for the kind of automated
check that's worth adding once this code lives in version control.

## Concepts Glossary (quick reference)

| Term | What it means here |
|---|---|
| Dynamic typing | A variable's type can change at runtime; Python doesn't lock it in. |
| Comprehension | Compact syntax to build a list/dict/set from an existing iterable. |
| Decorator (`@something`) | A function that wraps another function to add behavior. |
| `*args` / `**kwargs` | Ways to accept a variable number of positional/keyword arguments. |
| Generator (`yield`) | A function that produces values lazily, one at a time, instead of all at once. |
| Context manager (`with`) | A pattern that guarantees setup/cleanup code runs, even on errors. |
| Type hint | An optional annotation documenting expected types; not enforced at runtime. |
| `__name__ == "__main__"` | A guard that only runs code when a file is executed directly, not when imported. |

Have fun exploring -- the best way to learn is to change a number, break
something on purpose, and see what error Python gives you!
