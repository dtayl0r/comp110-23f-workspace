"""Instantiating A Class."""

"""
This is where we instantiate the class
we defined in classes.py.
In other words, we're creating objects
that belong to that class
"""

# import the class
# from <file_name>.<module_name> import <class_name>
from lessons.classes.pizza import Pizza

# CONSTRUCTOR
# add <"large", 10, True> back in Pizza()
my_pizza: Pizza = Pizza("large", 10, True)

# accesssing/setting attributes
my_pizza.size = "large"
my_pizza.toppings = 10
my_pizza.gluten_free = True

# Printing out values
print("My_pizza: ")
print(my_pizza)

print("Pizza: ")
print(Pizza)

print("Size Attribute: ")
print(my_pizza.size)

# sals_pizza size "medium", 5 toppings, Not GF
sals_pizza: Pizza = Pizza("medium", 5, False)
print(sals_pizza.size)

def price(input_pizza: Pizza) -> float:
    """Calculate Pizza Price"""
    if input_pizza.size == "large":
        price: float = 6.25
    else:
        price: float = 5.00
    price += .75 * input_pizza.toppings
    if input_pizza.gluten_free:
        price += 1.00
    return price


# Calling price function
print(price(sals_pizza))
print(price(my_pizza))

# Calling price method
print(sals_pizza.price())
print(my_pizza.price())

# python -m lessons.classes.pizza_orders

my_pizza.add_toppings(2)
print(my_pizza.toppings)
print(my_pizza.price())

my_other_pizza: Pizza = my_pizza.make_new_pizza_add_toppings(2)