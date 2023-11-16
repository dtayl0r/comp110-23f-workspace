"""File to define Fish class."""

__author__ = "730680410"


class Fish:
    """Making the fish class."""
    age: int
    
    def __init__(self):
        """Constructor."""
        self.age = 0
        return None
    
    def one_day(self):
        """Fish in one day."""
        self.age += 1
        return None