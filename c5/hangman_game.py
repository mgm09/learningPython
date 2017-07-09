# Hangman game
#
# The classic game of hangman. The computer picks a random word and the player needs to guess the word right, by guessing
# one letter at a time. If the player can't guess the word in time, the little stick figure gets hanged.

# imports
import random

# contants

HANGMAN = (
    """
    - - - - -
    |       |
    |
    |
    |
    |
    |
    |
    |
    - - - - - - - -
    """,
    """
    - - - - -
    |       |
    |       0
    |
    |
    |
    |
    |
    |
    - - - - - - - -
    """,
    """
    - - - - -
    |       |
    |       0
    |      -+-
    |
    |
    |
    |
    |
    - - - - - - - -
    """,
    """
    - - - - -
    |       |
    |       0
    |     /-+-
    |
    |
    |
    |
    |
    - - - - - - - -
    """,
    """
    - - - - -
    |       |
    |       0
    |     /-+-/
    |
    |
    |
    |
    |
    - - - - - - - -
    """,
    """
    - - - - -
    |       |
    |       0
    |     /-+-/
    |       |
    |
    |
    |
    |
    - - - - - - - -
    """,
    """
    - - - - -
    |       |
    |       0
    |     /-+-/
    |       |
    |       |
    |
    |
    |
    - - - - - - - -
    """,
    """
    - - - - -
    |       |
    |       0
    |     /-+-/
    |       |
    |       |
    |     |
    |     |
    |
    - - - - - - - -
    """,
    """
    - - - - -
    |       |
    |       0
    |     /-+-/
    |       |
    |       |
    |     |   |
    |     |   |
    |
    - - - - - - - -
    """)
