"""Practice with Dictionaries"""

#Making dictionary in class
ice_cream: dict[str, int] = {"Chocolate": 12, "Vanilla": 8, "Strawberry": 5}
print("Made my dictionary:")
print(ice_cream)

#How to add key-value pair to dictionary.
ice_cream["Mint"] = 3
print("After adding mint:")
print(ice_cream)

#how to remove key-value pair from dictionary
ice_cream.pop("Mint")
print("Removing Mint:")
print(ice_cream)

#Accessing value with key term
print(f"There are {ice_cream['Chocolate']} orders of chocolate")

#Changing a value with key term
ice_cream["Vanilla"] += 2

#After changing the vanilla's value
print("After changing value of Vanilla:")
print(ice_cream)

#Finding the length of a dicionary
print(f"There are {len(ice_cream)} key-value pairs.")

#Checking to see if a key is in a dictionary
print("Is strawberry in ice_cream?")
print("Strawberry" in ice_cream)
print("Is mint in ice_cream?")
print("Mint" in ice_cream)

#Using with a conditional
if "Mint" in ice_cream:
    print(f"There are {ice_cream['Mint']} orders of mint.")
else:
    print("There are no orders of mint.")

#Loop through and print out every flavor and its number of orders
for key in ice_cream:
    #print "<flavor> has <num_orders> orders"
    print(f"{key} has {ice_cream[key]} orders.")