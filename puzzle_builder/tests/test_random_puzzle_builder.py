import pytest

from puzzle_builder.random_puzzle_builder import WordsPuzzleBuilder


@pytest.mark.parametrize("puzzle_size", [1, 5, 15])
def test_random_puzzle_builder_as_string(puzzle_size):
    words_puzzle = WordsPuzzleBuilder(puzzle_size)
    puzzle = words_puzzle.as_string()
    assert type(puzzle) == str
    assert (
            len("".join(puzzle.replace(" ", "").split("\n"))) ==
            puzzle_size*puzzle_size
    )
