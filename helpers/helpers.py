""" This module consist of helpers functions."""


def check_boundaries(val, left=0, right=0) -> bool:
    """
    This function shows does val inside [left, right]. If it is not int or
    float raises Exception.

    :param val: value which is checked in boundaries.
    :param left: left boundary.
    :param right: right boundary.
    :return: True if val in [left, right], or False if not.
    """
    if not isinstance(val, (int, float)):
        raise TypeError("wrong val type. Should be number.")

    return left <= val <= right


def read_from_file(filepath):
    """
    This function read words from specific file and returns list ow words.
    :param filepath: 
    :return:
    """
    with open(filepath, "r") as f:
        return [word.strip("\n") for word in f.readlines()]
