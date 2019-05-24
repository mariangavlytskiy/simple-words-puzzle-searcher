import pytest

from helpers.helpers import check_boundaries


BOUNDARIES_TEST_DATA = [
    (1, 0, 10, True),
    (1, 1, 10, True),
    (1, 0, 1, True),
    (1, 2, 3, False),
    (1, -2, 0, False),
]


@pytest.mark.parametrize(
    "val, left, right, expected",
    BOUNDARIES_TEST_DATA,
    ids=[
        "not_straight_including",
        "left_straight_including",
        "right_straight_including",
        "not_include_from_left",
        "left_not_include"
    ],
)
def test_check_boundaries_correct_data(val, left, right, expected):
    assert check_boundaries(val, left, right) == expected
