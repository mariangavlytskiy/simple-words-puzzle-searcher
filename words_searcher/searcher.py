"""This module contains the main instrument to search words in the puzzle."""

from collections import namedtuple, defaultdict
from itertools import product

from helpers.helpers import check_boundaries


Direction = namedtuple("Direction", ["x", "y"])
DIRECTIONS = [Direction(x, y) for x, y in product((-1, 0, 1), (-1, 0, 1))]


class WordsSearcher:
    """
    WordsSearcher implements necessary words search in the specified
    words puzzle.
    """

    def __init__(self):
        self._found_words = defaultdict(list)

    @staticmethod
    def _puzzle_string_to_matrix(puzzle_string):
        """
        This method transforms puzzle string to list of the letters.

        :param puzzle_string: words puzzle string. (e.g. "a a\na a")

        :return: list of the letters.
        """
        if not isinstance(puzzle_string, str) or puzzle_string == "":
            raise ValueError("wrong puzzle string.")
        return [line.split(" ") for line in puzzle_string.split("\n")]

    @staticmethod
    def _get_letter_by_coordinate(puzzle, x, y, direction, number_in_the_word):
        """
        This method returns word letter.
        :param puzzle: puzzle as 2D matrix [[str,... ]..].
        :param x: possible word coordinate in the raw.
        :param y: possible word coordinate in the column.
        :param direction: tuple with direction values.
        :param number_in_the_word: order number in the possible word.
        :return:
        """
        raw_index, column_index = (
            (x + number_in_the_word * direction.x),
            (y + number_in_the_word * direction.y),
        )
        return puzzle[raw_index][column_index]

    @staticmethod
    def _puzzle_letters_coordinates(puzzle_size):
        """
        This method returns all puzzle's letters coordinates with direction.

        :param puzzle_size: puzzle size.
        :return: list of tuples with letter coordinates and
        """
        return product(range(puzzle_size), range(puzzle_size), DIRECTIONS)

    def _find_word_with_len(self, puzzle, x, y, direction, word_len):
        """
        This method returns found word string and its coordinates.
        It checks that we have not go out from the puzzle boundaries.

        :param puzzle: puzzle as 2D matrix [[str,... ]..].
        :param x: possible word coordinate in the raw.
        :param y: possible word coordinate in the column.
        :param direction: tuple with direction values.
        :param word_len: length of the searched word.
        :return: return any word with defined length.
        """
        letter_raw = x + (word_len - 1) * direction.x
        letter_col = y + (word_len - 1) * direction.y
        if (
                check_boundaries(letter_raw, right=len(puzzle)-1) and
                check_boundaries(letter_col, right=len(puzzle)-1)
        ):
            possible_word = "".join(
                self._get_letter_by_coordinate(puzzle, x, y, direction, n)
                for n in range(word_len)
            )
            self._found_words[word_len].append(possible_word)
            return possible_word

    def find_word(self, puzzle, word):
        """
        This method check is the word is contained in the puzzle and returns
        it if yes.

        :arg puzzle: words puzzle.
        :arg word: word that must be found.
        """

        for x, y, d in self._puzzle_letters_coordinates(len(puzzle)):
            if word == self._find_word_with_len(puzzle, x, y, d, len(word)):
                return word

    def find_words(self, puzzle_str, words_to_search):
        """
        This method returns all words that were found in the puzzle_str.

        :param words_to_search: list of words.
        :param puzzle_str: puzzle.
        :return: list of found words.
        """
        transformed_puzzle = self._puzzle_string_to_matrix(puzzle_str)
        matched_words = []
        for word in words_to_search:
            possible_words = self._found_words.get(len(word))
            if possible_words and word in possible_words:
                matched_words.append(word)
            elif self.find_word(transformed_puzzle, word):
                matched_words.append(word)
        return matched_words
