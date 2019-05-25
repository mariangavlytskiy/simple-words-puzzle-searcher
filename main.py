from argparse import ArgumentParser

from puzzle_builder.random_puzzle_builder import WordsPuzzleBuilder
from words_searcher.searcher import WordsSearcher


MIN_PUZZLE_SIZE = 2


def main(puzzle_size, words):
    """
    Start words searching.
    :param puzzle_size:
    :param words:
    :return:
    """
    if puzzle_size <= MIN_PUZZLE_SIZE:
        print("Puzzle size should be bigger than 2.")
    elif not words:
        print("Write one more word to find.")
    else:
        puzzle_builder = WordsPuzzleBuilder(puzzle_size)
        puzzle = puzzle_builder.as_string()
        words_searcher = WordsSearcher()
        found_words = words_searcher.find_words(puzzle, words)
        not_found_words = list(set(words) - set(found_words))
        print(
            f"In the puzzle:\n{puzzle}.\n"
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
    args = parser.parse_args()
    main(args.puzzle_size, args.words)
