import pytest

from words_searcher.searcher import WordsSearcher, Direction

# Be carefully when change constants in this file.


STRING_TO_MATRIX_TEST_DATA = [
    ("a\na", [["a"], ["a"]]),
    ("a a\na", [["a", "a"], ["a"]]),
    ("", "wrong puzzle string."),
    (1, "wrong puzzle string.")
]
# Test puzzle for benchmark tests.
TEST_PUZZLE_SIZE_15 = """g v c b z m d e m f g o l i q
    d f p v z w d q h b t f s m o
    s h b c z e w r v a q u f d n
    s s i l s u d s g n w z o v s
    t d j g n d b u o d r f h o n
    y c j k d o p b o d a x g h r
    e j u r l h o y s n z v b t n
    e n c j c m t e q i p g f t b
    l o g a h p n f z e l f f v j
    e d k k w n h y l k c s i g a
    v e o z g r q a j e w i x m h
    h y o h u r b g v x r o b r l
    c i v b l h c t x u m j m d i
    h n w d q i c b z x d b r f t
    m v o t n d e s a c b t y x l"""
WORDS_IN_PUZZLE_SIZE_15 = ["fbl", "awrb", "siga", "mfgoliq"]

TEST_PUZZLE = "1 2 3\n4 5 6"
TEST_PUZZLE_MATRIX = [["1", "2", "3"], ["4", "5", "6"]]
TEST_PUZZLE_WORDS = ["123", "456"]


@pytest.fixture(scope="module")
def words_searcher():
    return WordsSearcher()


@pytest.mark.parametrize(
    "puzzle_string, expected",
    STRING_TO_MATRIX_TEST_DATA,
    ids=[
        "two_letters_without_space",
        "three_letters_with_space",
        "empty_puzzle",
        "not_valid_type_puzzle",
    ]
)
def test_puzzle_string_to_matrix(words_searcher, puzzle_string, expected):
    if not isinstance(puzzle_string, str) or puzzle_string == "":
        with pytest.raises(ValueError, match=expected):
            words_searcher._puzzle_string_to_matrix(puzzle_string)
    else:
        assert (
                words_searcher._puzzle_string_to_matrix(puzzle_string) ==
                expected
        )


def test_get_letter_by_coordinate(words_searcher):
    first_raw, first_column = 0, 0
    last_letter_index = 2
    to_right_direction = Direction(0, 1)
    assert words_searcher._get_letter_by_coordinate(
        TEST_PUZZLE_MATRIX,
        first_raw,
        first_column,
        to_right_direction,
        last_letter_index,
    ) == TEST_PUZZLE_MATRIX[first_raw][last_letter_index]


def test_find_word_with_len(words_searcher):
    x, y, d, n = 0, 0, Direction(0, 1), 2
    found_word = words_searcher._find_word_with_len(
        TEST_PUZZLE_MATRIX, x, y, d, 3
    )
    assert found_word == TEST_PUZZLE_WORDS[0]


@pytest.mark.parametrize("word_to_find", TEST_PUZZLE_WORDS)
def test_find_word(words_searcher, word_to_find):
    assert (
            words_searcher.find_word(TEST_PUZZLE_MATRIX, word_to_find) ==
            word_to_find
    )


def test_find_words(words_searcher):
    assert words_searcher.find_words(
        TEST_PUZZLE_MATRIX,
        TEST_PUZZLE_WORDS,
    ) == TEST_PUZZLE_WORDS


@pytest.mark.parametrize(
    "puzzle, words_to_find",
    [
        (TEST_PUZZLE_SIZE_15, WORDS_IN_PUZZLE_SIZE_15),
        (TEST_PUZZLE, TEST_PUZZLE_WORDS),
    ],
    ids=[
        f"15_size_puzzle_{len(WORDS_IN_PUZZLE_SIZE_15)}_words_to_find",
        f"puzzle_with_size_2_and_{len(TEST_PUZZLE_WORDS)}_words_to_find"
    ]
)
def test_benchmark_words_searcher(
    benchmark,
    words_searcher,
    puzzle,
    words_to_find,
):
    @benchmark
    def wrap():
        words_searcher.find_words(puzzle, words_to_find)
