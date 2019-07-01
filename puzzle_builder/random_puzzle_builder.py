"""This module contains code to generate puzzles with random letters."""
from random import choices
from string import ascii_lowercase


class WordsPuzzleBuilder:
    """
    WordsPuzzleBuilder is implemented to generate random words puzzle string.

    :arg puzzle_size: define words puzzle size.
    """

    def __init__(self, puzzle_size):
        self.size = puzzle_size
        self.puzzle = [
            choices(ascii_lowercase, k=self.size)
            for _ in range(self.size)
        ]

    def __repr__(self):
        """
        This method generate words puzzle string with specified size.
        :return: words puzzle as string.
        """
        return "\n".join([" ".join(row) for row in self.puzzle])
