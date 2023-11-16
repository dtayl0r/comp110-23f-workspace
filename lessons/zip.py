"""Combining two lists into a dictionary."""

__author__ = "730680410"


def zip(list_1: list[str], list_2: list[int]) -> dict[str, int]:
    """Return a dictionary given the two inputs of lists."""
    xs: dict[str, int] = dict()
    if len(list_1) != len(list_2):
        return xs
    for elem in range(len(list_1)):
        xs[list_1[elem]] = list_2[elem]
    return xs