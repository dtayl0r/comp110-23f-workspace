"""File to define Bear class."""

__author__ = "730680410"


class Bear:
    """Making a bear class."""
    age: int
    hunger_score: int

    def __init__(self):
        """Constructor."""
        self.age = 0
        self.hunger_score = 0
        return None
    
    def one_day(self):
        """Bears in the span of a day."""
        self.age += 1
        self.hunger_score -= 1
        return None
    
    def eat(self, num_fish: int):
        """Function to show how the bear eats."""
        self.hunger_score += num_fish
        return None