"""
rock_paper_scissors.py
=======================

Classic rock-paper-scissors against the computer. Highlights: dicts used
as lookup/rule tables (instead of a long chain of if/elif statements),
the `random` module, and a running score kept across rounds.
"""

from __future__ import annotations

import random

CHOICES = ["rock", "paper", "scissors"]

# A dict where each key "beats" the value it maps to. This is a classic
# Python trick: instead of writing
#     if player == "rock" and computer == "scissors": ...
#     elif player == "paper" and computer == "rock": ...
#     elif player == "scissors" and computer == "paper": ...
# we encode the RULES as data and just look them up. Less code, easier to
# extend (e.g. adding "lizard" and "Spock" would just mean adding entries).
BEATS = {
    "rock": "scissors",
    "paper": "rock",
    "scissors": "paper",
}


def _decide_winner(player: str, computer: str) -> str:
    """Returns 'player', 'computer', or 'tie'."""
    if player == computer:
        return "tie"
    if BEATS[player] == computer:
        return "player"
    return "computer"


def play() -> None:
    """Entry point called by main.py."""
    print("\n--- Rock, Paper, Scissors ---")
    print("Type 'rock', 'paper', or 'scissors'. Type 'q' to quit back to the menu.\n")

    score = {"player": 0, "computer": 0, "ties": 0}

    while True:
        raw_choice = input("Your choice: ").strip().lower()

        if raw_choice == "q":
            break

        if raw_choice not in CHOICES:
            print(f"Please choose one of: {', '.join(CHOICES)} (or 'q' to quit).")
            continue

        computer_choice = random.choice(CHOICES)
        winner = _decide_winner(raw_choice, computer_choice)

        print(f"You chose {raw_choice}, the computer chose {computer_choice}.")

        if winner == "tie":
            score["ties"] += 1
            print("It's a tie!")
        elif winner == "player":
            score["player"] += 1
            print("You win this round! 🎉")
        else:
            score["computer"] += 1
            print("The computer wins this round!")

        print(f"Score -> You: {score['player']}  Computer: {score['computer']}  Ties: {score['ties']}\n")

    print(
        f"\nFinal score -> You: {score['player']}  "
        f"Computer: {score['computer']}  Ties: {score['ties']}"
    )


if __name__ == "__main__":
    play()
