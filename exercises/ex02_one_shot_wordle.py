"""EX02 - One Shot Wordle"""

__author__ = 730680410

secret_word: str = "python"
lsecret_word: str = str(len(secret_word))
white_box: str = "\U00002B1C"
green_box: str = "\U0001F7E9"
yellow_box: str = "\U0001F7E8"
emoji_store: str = ""
guess_word = input(f"What is your {lsecret_word}-letter guess? ")
guess_idx: int = 0
while len(guess_word) != len(secret_word):
     guess_word = input(f"That was not {lsecret_word} letters! Try Again: ")
#Checking to see if the length of the user input is the same as the length of the hidden word
#if it is not the same length it will keep asking until an input satifies the statement
while guess_idx < len(secret_word):
#looping to see which emoji goes to the corresponding letter
    if guess_word[guess_idx] == secret_word[guess_idx]:
        emoji_store = emoji_store + green_box
    elif guess_word[guess_idx] != secret_word[guess_idx]:
        letter: int = 0
        wrong_position = False
        while wrong_position is False and letter < len(secret_word):
#when the indexes of the input and the hidden word arent equal; loop to find if the letter is in the wrong position
            if guess_word[guess_idx] == secret_word[letter]:
                wrong_position = True
            else:
                letter = letter + 1
        if wrong_position is True:
            emoji_store = emoji_store + yellow_box
#if the letter is in the wrong position, you should get a yellow box
        if wrong_position is False:
            emoji_store = emoji_store + white_box
#if the letter is not in the word at all, you should get a white box
    guess_idx = guess_idx + 1

print(emoji_store)

if guess_word == secret_word:
    print("Woo! You got it! ")
else:
    print("Not quite. Play again soon! ")