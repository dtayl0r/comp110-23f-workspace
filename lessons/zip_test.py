"""Testing zip function."""

from lessons.zip import zip


def test_dict_zip():
    """Test to see if the function makes a dictionary."""
    turtles = ["Leo", "Raph", "Donnie", "Mikey"]
    order = [1, 2, 3, 4]
    together = {"Leo": 1, "Raph": 2, "Donnie": 3, "Mikey": 4}
    assert zip(turtles, order) == together


def test_return_zip():
    """Test to see if the zip function returns the correct information"""
    turtles = ["Leo", "Raph", "Donnie", "Mikey"]
    order = [1, 2, 3, 4, 5]
    together = {"Leo": 1, "Raph": 2, "Donnie": 3, "Mikey": 4}
    assert zip(turtles, order) != together


def test_len_zip():
    """Test to see if dictionary is the correct length."""
    turtles = ["Leo", "Raph", "Donnie", "Mikey"]
    order = [1, 2, 3, 4]
    together = {"Leo": 1, "Raph": 2, "Donnie": 3, "Mikey": 4}
    assert len(zip(turtles, order)) == len(together)