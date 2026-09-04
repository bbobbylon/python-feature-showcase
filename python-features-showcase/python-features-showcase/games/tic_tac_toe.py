"""
tic_tac_toe.py
================

Two-player (same keyboard) tic-tac-toe. Highlights: representing a 2D
grid with a plain Python list, functions that operate on shared state,
a "game loop" that alternates turns, and simple win-condition checking
using list comprehensions.
"""

from __future__ import annotations

Board = list[str]  # a type alias: a Board is just a list of 9 strings ("X", "O", or " ")

WIN_LINES = [
    (0, 1, 2), (3, 4, 5), (6, 7, 8),  # rows
    (0, 3, 6), (1, 4, 7), (2, 5, 8),  # columns
    (0, 4, 8), (2, 4, 6),             # diagonals
]


def _new_board() -> Board:
    """A tic-tac-toe board is just a flat list of 9 cells, indexed 0-8:
        0 | 1 | 2
        3 | 4 | 5
        6 | 7 | 8
    """
    return [" "] * 9


def _render(board: Board) -> str:
    """Builds a printable string of the board using f-strings and slicing."""
    rows = [" | ".join(board[i:i + 3]) for i in (0, 3, 6)]
    return f"\n{rows[0]}\n---------\n{rows[1]}\n---------\n{rows[2]}\n"


def _winner(board: Board) -> str | None:
    """
    Checks every possible winning line. A list comprehension + `all()`
    checks whether every cell in a line matches and is non-empty.
    """
    for line in WIN_LINES:
        values = [board[i] for i in line]
        if values[0] != " " and all(value == values[0] for value in values):
            return values[0]
    return None


def _is_full(board: Board) -> bool:
    return " " not in board


def play() -> None:
    """Entry point called by main.py."""
    print("\n--- Tic-Tac-Toe (two players, same keyboard) ---")
    print("Positions are numbered 0-8, left to right, top to bottom.")
    print("Type 'q' at any time to quit back to the menu.\n")

    board = _new_board()
    current_player = "X"

    while True:
        print(_render(board))
        raw_move = input(f"Player {current_player}, pick a position (0-8): ").strip()

        if raw_move.lower() == "q":
            print("Quitting to the menu.")
            return

        if not raw_move.isdigit() or not (0 <= int(raw_move) <= 8):
            print("Please enter a number from 0 to 8 (or 'q' to quit).")
            continue

        position = int(raw_move)
        if board[position] != " ":
            print("That spot is already taken -- choose another.")
            continue

        board[position] = current_player

        winner = _winner(board)
        if winner:
            print(_render(board))
            print(f"🎉 Player {winner} wins!")
            return

        if _is_full(board):
            print(_render(board))
            print("It's a draw!")
            return

        # Switch turns: a compact way to alternate between two values,
        # avoiding an if/else.
        current_player = "O" if current_player == "X" else "X"


if __name__ == "__main__":
    play()
