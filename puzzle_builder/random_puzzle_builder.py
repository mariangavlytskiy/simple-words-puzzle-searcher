"""This module contains code to generate puzzles with random letters."""
from random import choices
from string import ascii_lowercase


NEW_LINE_CHARACTER = "\n"


class WordsPuzzleBuilder:
    """
    WordsPuzzleBuilder is implemented to generate random words puzzle string.

    :arg puzzle_size: define words puzzle size.

    """

    def __init__(self, puzzle_size):
        self.size = puzzle_size
        self._letters_list = choices(ascii_lowercase, k=self.size*self.size)

    def as_string(self):
        """
        This method generate words puzzle string with specified size.
        :return: words puzzle as string.
        """
        start = 0
        puzzles_rows = []
        for i in range(self.size, len(self._letters_list)+1, self.size):
            puzzles_rows.append(" ".join(self._letters_list[start:i]))
            start = i
        return "\n".join(puzzles_rows)
