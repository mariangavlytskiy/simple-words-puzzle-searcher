import pytest

from puzzle_builder.random_puzzle_builder import WordsPuzzleBuilder


@pytest.mark.parametrize("puzzle_size", [1, 5, 15])
def test_random_puzzle_builder_as_string(puzzle_size):
    words_puzzle = WordsPuzzleBuilder(puzzle_size)
    assert type(words_puzzle.puzzle) == list
    assert len(words_puzzle.puzzle) == puzzle_size
    for i in range(puzzle_size):
        assert len(words_puzzle.puzzle[i]) == puzzle_size
