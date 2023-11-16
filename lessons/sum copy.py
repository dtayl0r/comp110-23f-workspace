"""CQ04 - Loops Practice."""

__author__ = "730680410"


def w_sum(vals: list[float]) -> float:
    """Using a while loop find the sum of the list."""
    idx: int = 0
    value: float = 0.0
    while idx < len(vals):
        value += vals[idx]
        idx += 1
    return value


def f_sum(vals: list[float]) -> float:
    """Using a for loop find the sum of the list."""
    value: float = 0.0
    for elem in vals:
        value += elem
    return value


def f_range_sum(vals: list[float]) -> float:
    """Using a for loop and range find the sum of the list"""
    value: float = 0.0
    for elem in range(0, len(vals)):
        value += vals[elem]
    return value