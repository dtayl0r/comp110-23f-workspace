"""EX06 - Dictionary Functions."""

__author__ = "730680410"


# Function inverts key-value pairs in dictionary.
def invert(og_dict: dict[str, str]) -> dict[str, str]:
    """Given a dict, invert the keys and values then return the new dict."""
    new_dict: dict[str, str] = {}
    for x, value in og_dict.items():
        # If statement is supposed to find if key is used twice in dictionary.
        if value in new_dict:
            raise KeyError("key appears twice in dictionary.")
        new_dict[value] = x
    return new_dict


def favorite_color(color_poll: dict[str, str]) -> str:
    """Given a string tell the highest value in the dictionary."""
    score_board: dict[str, int] = {}
    # The goal is to find a way to update the value every time it appears in the dictionary
    for name in color_poll:
        color = color_poll[name]
        if color in score_board:
            score_board[color] += 1
        else:
            score_board[color] = 1
    max_key: str = ""
    max_elem: int = 0
    for key in score_board:
        if score_board[key] > max_elem:
            max_key = key
            max_elem = score_board[key]
    return max_key


def count(count_list: list[str]) -> dict[str, int]:
    """Counting how many times a word is in a list."""
    # Empty dictionary to use for counting.
    count_dict: dict[str, int] = {}
    for elem in count_list:
        if elem in count_dict:
            count_dict[elem] += 1
        else:
            count_dict[elem] = 1
    return count_dict


def alphabetizer(initial_list: list[str]) -> dict[str, list[str]]:
    """Sorting a dictionary alphabetically using the keys."""
    alpha_dict: dict[str, list[str]] = {}
    for word in initial_list:
        first_letter = word[0]
        # Adding a list as a value for the dictionary.
        if first_letter not in alpha_dict:
            alpha_dict[first_letter] = []
        alpha_dict[first_letter].append(word)
    for key in alpha_dict:
        alpha_dict[key].sort(key=str)
    return alpha_dict


def update_attendance(attendence_log: dict[str, list[str]], day: str, student: str) -> dict[str, list[str]]:
    """Update a dictionary of attendence."""
    if day in attendence_log:
        if student not in attendence_log[day]:
            attendence_log[day].append(student)
    else:
        attendence_log[day] = [student]
    return attendence_log
