"""EX03 - Wordle!"""

__author__ = "730680410"

white_box: str = "\U00002B1C"
green_box: str = "\U0001F7E9"
yellow_box: str = "\U0001F7E8"


# Determines T/F to identify where the emojis need to go.
def contains_char(guess_word: str, char: int) -> bool:
    """Print T/F if letter is found anwhere in word"""
    assert len(char) == 1
    idx: int = 0
    while idx < len(guess_word):
        if guess_word[idx] == char:
            return True
        idx = idx + 1
    return False


# most important for emoji printing. needs to run smoothly with contains_char.
def emojified(input: str, code_word: str) -> str:
    """Print the correct corresponding box emoji"""
    assert len(input) == len(code_word)
    idx: int = 0
    emoji_store: str = ""
    while idx < len(input):
        if input[idx] == code_word[idx]:
            emoji_store += green_box
        elif contains_char(code_word, input[idx]):
            emoji_store += yellow_box
        else:
            emoji_store += white_box
        idx += 1
    return emoji_store


# simple but critical for the other functions to excute their jobs.
def input_guess(ex_len: int) -> str:
    """Gather user guess information"""
    guess_word = input(f"Enter a {ex_len} character word: ")
    while len(guess_word) != ex_len:
        guess_word = input(f"That wasn't {ex_len} chars! Try again: ")
    return guess_word


def main() -> None:
    """The entrypoint of the program and main game loop"""
    hidden: str = "codes"
    allowed_turns: int = 6
    guess_turn: int = 0
    game_win: bool = False
    # when working should allow for all functions to work together to build the game.
    while guess_turn < allowed_turns and not game_win:
        guess_turn += 1
        print(f"=== Turn {guess_turn}/{allowed_turns} ===")
        guess_word = input_guess(len(hidden))
        print(emojified(guess_word, hidden))
        if guess_word == hidden:
            game_win = True
    if game_win is True:
        print(f"You won in {guess_turn}/{allowed_turns} turns! ")
    else:
        print(f"X/{allowed_turns} - Sorry, Try again tomorrow! ")


# should run similarly enough to wordle if all functions blended well in main().
if __name__ == "__main__":
    main()