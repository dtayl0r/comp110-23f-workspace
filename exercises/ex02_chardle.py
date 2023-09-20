secretword: str = "python"
guessword = input("What is your 6-letter guess? ")
if guessword != secretword:
    while len(guessword) != 6:
        guessword = input("That was not 6 letters! Try Again: ")
if guessword == secretword:
    print("Woo! You got it! ")
else:
    print("Not quite. Play again soon! ")