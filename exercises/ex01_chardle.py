"""EX01 - Chardle - A cute step toward Wordle."""

__author__ = "730680410"

guessword = input("Enter a 5-character word: ")
if len(guessword) != 5:
    print("Error: Word must contain 5 charaters.")
    exit()
letter = input("Enter a single character: ")
if len(letter) != 1:
    print("Error: Character must be a single character.")
    exit()
print("Searching for " + letter + " in " + guessword)
count = 0
if letter == guessword[0]:
    print(letter + " found at index " + str(0))
    count = count + 1
if letter == guessword[1]:
    print(letter + " found at index " + str(1))
    count = count + 1
if letter == guessword[2]:
    print(letter + " found at index " + str(2))
    count = count + 1
if letter == guessword[3]:
    print(letter + " found at index " + str(3))
    count = count + 1
if letter == guessword[4]:
    print(letter + " found at index " + str(4))
    count = count + 1
instance = count
if instance != 1:
    print(str(instance) + " instances of " + letter + " found in " + guessword)
else:
    print(str(instance) + " instance of " + letter + " found in " + guessword)
if instance == int(0):
    print("No instances of " + letter + " found in " + guessword)