"""Defining a Class!"""

from __future__ import annotations
"""
Think of a class definition as 
a "roadmap" for objects that 
belong to the class 
You are defining the underlying structure 
every instance of this class will have
"""


class Pizza:
    # attributes
    # Think of these as variables
    # each instance of my class will have
    # <name> : <type>
    size: str
    toppings: int
    gluten_free: bool

    # my_pizza: Pizza = Pizza("large")
    def __init__ (self, inp_size: str, inp_top: int, gf: bool):
        """My constructor"""
        self.size = inp_size
        self.toppings = inp_top
        self.gluten_free = gf
        # returns a Pizza object

    def price(self) -> float:
        """ Method to calculate price of pizza"""
        if self.size == "large":
            price: float = 6.25
        else:
            price: float = 5.00
        price += .75 * self.toppings
        if self.gluten_free:
            price += 1.00
        return price

    def add_toppings(self, num_toppings: int):
        """Add toppings to existing pizza"""
        self.toppings += num_toppings

    def make_new_pizza_add_toppings(self, num_toppings: int) -> Pizza:
        """Make new pizza with existing pizza's properties and add toppings"""
        my_pizza: Pizza = Pizza(self.size, self.toppings + num_toppings, self.gluten_free)
        return my_pizza
    
    def __str__(self) -> str:
        pizza_info: str = f"Pizza Order: size: {self.size}, toppings: {self.toppings}, GF: {self.gluten_free}"
        return pizza_info
    
    
my_pizza: Pizza = Pizza("medium", 3, False)
print(str(my_pizza))
sals_pizza: Pizza = Pizza("large", 1, True)
print(sals_pizza)