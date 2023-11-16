"""File to define River class."""

__author__ = "730680410"

from exercises.ex08.fish import Fish
from exercises.ex08.bear import Bear


class River:
    """Making the river class."""
    day: int
    bears: list
    fish: list

    def __init__(self, num_fish: int, num_bears: int):
        """New River with num_fish Fish and num_bears Bears."""
        self.day: int = 0
        self.fish: list[Fish] = []
        self.bears: list[Bear] = []
        # populate the river with fish and bears
        for x in range(0, num_fish):
            self.fish.append(Fish())
        for x in range(0, num_bears):
            self.bears.append(Bear())

    def check_ages(self):
        """Checking to see how old the animals are."""
        self.fish = [fish for fish in self.fish if fish.age <= 3]
        self.bear = [bear for bear in self.bears if bear.age <= 5]
        return None

    def bears_eating(self):
        """Seeing how much fish the bears eat."""
        if len(self.fish) >= 5: 
            for bear in self.bears:
                bear.eat(3)
            self.remove_fish(3)
        return None
    
    def check_hunger(self):
        """Showing how hungry the bears are."""
        self.bears = [bear for bear in self.bears if bear.hunger_score >= 0]
        return None
        
    def repopulate_fish(self):
        """Creating new fish for the river."""
        offspring = (len(self.fish) // 2) * 4
        self.fish.extend([Fish() for _ in range(offspring)])
        return None
    
    def repopulate_bears(self):
        """Creating new bears for the river."""
        offspring = (len(self.bears)) // 2
        self.bears.extend([Bear() for _ in range(offspring)])
        return None
    
    def view_river(self):
        """Method to view the river."""
        print(f'~~~ Day {self.day}: ~~~\n')
        print(f'Fish population: {len(self.fish)}')
        print(f'Bear population: {len(self.bears)}')
        return None
            
    def one_river_day(self):
        """Simulate one day of life in the river."""
        # Increase day by 1
        self.day += 1
        # Simulate one day for all Bears
        for bear in self.bears:
            bear.one_day()
        # Simulate one day for all Fish
        for fish in self.fish:
            fish.one_day()
        # Simulate Bear's eating
        self.bears_eating()
        # Remove hungry Bear's from River
        self.check_hunger()
        # Remove old Fish and Bear's from River
        self.check_ages()
        # Simulate Fish repopulation
        self.repopulate_fish()
        # Simulate Bear repopulation
        self.repopulate_bears()
        # Visualize River
        self.view_river()
    
    def one_river_week(self):
        """Simulate one week in the river."""
        for _ in range(7):
            self.one_river_day
        return None
    
    def remove_fish(self, amount: int):
        """Removing the amount of fish that is input."""
        if amount <= len(self.fish):
            self.fish = self.fish[amount]