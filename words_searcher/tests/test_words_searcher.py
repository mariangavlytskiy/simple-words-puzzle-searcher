import pytest

from words_searcher.searcher import WordsSearcher, Direction


# Test puzzle for benchmark tests.
TEST_PUZZLE_SIZE_10 = [
    ['p', 't', 'g', 'b', 'o', 'n', 'f', 'b', 'g', 'u'],
    ['p', 'n', 'r', 'b', 'i', 'n', 'b', 'y', 'y', 's'],
    ['z', 'i', 'e', 'o', 'e', 'r', 'u', 'w', 't', 'g'],
    ['r', 'x', 'a', 'c', 'g', 'l', 'u', 'r', 'r', 'p'],
    ['a', 's', 'o', 'a', 'g', 'y', 'z', 'g', 'e', 'w'],
    ['o', 'l', 'v', 'k', 'u', 'h', 'b', 'o', 'd', 'f'],
    ['u', 'w', 'g', 'g', 'a', 'o', 'c', 'o', 'f', 'v'],
    ['w', 'o', 'd', 'k', 'v', 'w', 'a', 'i', 'w', 'x'],
    ['h', 'j', 's', 'm', 'g', 'o', 'o', 'a', 'z', 'x'],
    ['j', 'c', 'l', 'z', 'h', 't', 'k', 'u', 'd', 'l'],
]
WORDS_IN_PUZZLE_SIZE_10 = ["ptg", "ecgh", "kudl", "wodk"]

TEST_PUZZLE_SIZE_2 = [["1", "2", "3"], ["4", "5", "6"], ["7", "8", "9"]]
WORDS_IN_PUZZLE_SIZE_2 = ["123", "456"]


@pytest.fixture(scope="module")
def words_searcher():
    return WordsSearcher()


def test_get_letter_by_coordinate(words_searcher):
    first_row, first_column = 0, 0
    last_letter_index = 2
    to_right_direction = Direction(0, 1)
    assert words_searcher._get_letter_by_coordinate(
        TEST_PUZZLE_SIZE_2,
        first_row,
        first_column,
        to_right_direction,
        last_letter_index,
    ) == TEST_PUZZLE_SIZE_2[first_row][last_letter_index]


def test_find_word_with_len(words_searcher):
    x, y, d, n = 0, 0, Direction(0, 1), 2
    found_word = words_searcher._find_word_with_len(
        TEST_PUZZLE_SIZE_2, x, y, d, len(WORDS_IN_PUZZLE_SIZE_2[0])
    )
    assert found_word == WORDS_IN_PUZZLE_SIZE_2[0]


@pytest.mark.parametrize("word_to_find", WORDS_IN_PUZZLE_SIZE_2)
def test_find_word(words_searcher, word_to_find):
    assert (
            words_searcher.find_word(TEST_PUZZLE_SIZE_2, word_to_find) ==
            word_to_find
    )


def test_find_words(words_searcher):
    assert (
            words_searcher.find_words(
                TEST_PUZZLE_SIZE_2, WORDS_IN_PUZZLE_SIZE_2) ==
            WORDS_IN_PUZZLE_SIZE_2
    )
