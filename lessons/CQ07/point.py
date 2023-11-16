"""Making Point Class."""

from __future__ import annotations


class Point:
    """Class for Points."""
    x: float
    y: float

    def __init__(self, x_init: float = 0.0, y_init: float = 0.0):
        """My Constructor."""
        self.x = x_init
        self.y = y_init

    def scale_by(self, factor: int) -> None:
        """Change point by multipling by the same value."""
        self.x *= factor
        self.y *= factor

    def scale(self, factor: int) -> Point:
        """Creating a new point from the original point."""
        new_point: Point = Point(self.x * factor, self.y * factor)
        return new_point
    
    def __str__(self):
        """String operation overload."""
        output = (f"x: {self.x}; y: {self.y}")
        return output
    
    def __mul__(self, factor: int | float) -> Point:
        """Multiplication operation overload."""
        new_point: Point = Point(self.x * factor, self.y * factor)
        return new_point
    
    def __add__(self, value: int | float) -> Point:
        """Addition operation overload."""
        new_point: Point = Point(self.x + value, self.y + value)
        return new_point