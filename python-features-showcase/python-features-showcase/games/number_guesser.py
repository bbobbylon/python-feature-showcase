"""
number_guesser.py
==================

The classic "guess the secret number" game. Highlights: the `random`
module, `while` loops, conditionals, and basic input validation.
"""

from __future__ import annotations

import random


def play() -> None:
    """Entry point called by main.py."""
    print("\n--- Guess the Number ---")
    print("I'm thinking of a number between 1 and 100. Try to guess it!")
    print("(Type 'q' at any time to quit back to the menu.)\n")

    secret_number = random.randint(1, 100)  # random.randint is inclusive on both ends
    attempts = 0

    while True:  # the "game loop" -- keeps asking until the player wins or quits
        raw_guess = input("Your guess: ").strip()

        if raw_guess.lower() == "q":
            print(f"Quitting! The number was {secret_number}.")
            return

        if not raw_guess.isdigit():
            print("Please enter a whole number (or 'q' to quit).")
            continue  # skip the rest of the loop body, go straight to the next iteration

        guess = int(raw_guess)
        attempts += 1

        if guess < secret_number:
            print("Too low!")
        elif guess > secret_number:
            print("Too high!")
        else:
            print(f"\n🎉 You got it! The number was {secret_number}.")
            print(f"It took you {attempts} attempt{'s' if attempts != 1 else ''}.")
            return


if __name__ == "__main__":
    play()
