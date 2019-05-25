from argparse import ArgumentParser

from puzzle_builder.random_puzzle_builder import WordsPuzzleBuilder
from words_searcher.searcher import WordsSearcher
from helpers.helpers import read_from_file


MIN_PUZZLE_SIZE = 2


def validate_input(puzzle_size, words, filepath):
    if puzzle_size <= MIN_PUZZLE_SIZE:
        return False, "Puzzle size should be bigger than 2."
    if not(words or filepath):
        return False, "Write one more word to find. " \
                      "Or specify filepath with words."
    return True, ""


def main(puzzle_size, words, filepath):
    """
    Start words searching.
    :param puzzle_size:
    :param words:
    :return:
    """
    is_correct, err_string = validate_input(puzzle_size, words, filepath)
    if not is_correct:
        print(err_string)

    if words and filepath:
        words.extend(read_from_file(filepath))
    elif filepath:
        words = read_from_file(filepath)

    words_builder = WordsPuzzleBuilder(puzzle_size)
    puzzle = words_builder.puzzle
    words_searcher = WordsSearcher()
    found_words = words_searcher.find_words(puzzle, set(words))
    not_found_words = list(set(words) - set(found_words))
    print(
        f"In the puzzle:\n{words_builder}.\n"
        f"Found words: {found_words}.\n"
        f"Not found words: {not_found_words}"
    )


if __name__ == "__main__":
    parser = ArgumentParser(
        description="This is program to search words in the random puzzle.",
    )
    parser.add_argument(
        "--puzzle_size",
        type=int,
        action="store",
        default=15,
        help="Describes puzzle's size",
    )
    parser.add_argument(
        "--words",
        type=str,
        nargs="+",
        help="Describes words which would be tried found in the puzzle.",
    )
    parser.add_argument(
        "--filepath",
        type=str,
        action="store",
        help="Path to file with words"
    )
    args = parser.parse_args()
    main(args.puzzle_size, args.words, args.filepath)
