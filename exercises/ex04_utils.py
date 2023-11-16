"""EX04 - 'list' Utility Functions."""

__author__ = "730680410"


# this should be able to determine whether or not a list is comprised of a specific number.
def all(xs: list[int], num: int) -> bool:
    """Tells whether a list has only a specific number."""
    idx: int = 0
    while idx < len(xs):
        if xs[idx] != num:
            return False
        idx += 1
    if len(xs) == 0:
        return False
    return True


# a little troubling but determines the largest number in a given list.
def max(group: list[int]) -> int:
    """Gives the largest value in list of ints."""
    if len(group) == 0:
        raise ValueError("max() arg is an empty List")
    x: int = 0
    b_num: int = group[0]
    while x < len(group):
        if group[x] > b_num:
            b_num = group[x]
        x += 1
    return b_num


# given two lists of numbers this function should be able to tell if they have the same index; took some time to figure out.
def is_equal(group1: list[int], group2: list[int]) -> bool:
    """Tell if two lists index values are equal."""
    x: int = 0
    same_place: bool = True
    while x < len(group1) and x < len(group2):
        if group1[x] != group2[x]:
            same_place = False
        x += 1
    if len(group1) != len(group2):
        same_place = False
    return same_place