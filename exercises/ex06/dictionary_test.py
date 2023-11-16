"""Testing Dicionary Functions."""

__author__ = "730680410"

from exercises.ex06.dictionary import invert, favorite_color, count, alphabetizer, update_attendance


def test_len_invert():
    """Testing to see if the lengths of both dictionaries are the same."""
    test_dict: dict[str, str] = {"horse": "land", "fish": "water", "bird": "air"}
    in_dict: dict[str, str] = {"land": "horse", "water": "fish", "air": "bird"}
    assert len(invert(test_dict)) == len(in_dict)


def test_invert_output():
    """Test to see if the returned dictionary has the correct information."""
    in_dict: dict[str, str] = {"horse": "land", "fish": "water", "bird": "air"}
    assert "water" in invert(in_dict)


def test_output_invert():
    """Test to see if invert displays the correct output."""
    test_dict: dict[str, str] = {"horse": "land", "fish": "water", "bird": "air"}
    in_dict: dict[str, str] = {"land": "horse", "water": "fish", "air": "bird"}
    assert invert(test_dict) == in_dict


def test_favorite_color_working():
    """Testing to see if the function performs correctly."""
    test_poll: dict[str, str] = {"John": "Blue", "Gabe": "Red", "Ryan": "Blue"}
    assert favorite_color(test_poll) == "Blue"


def test_poll_tie_favorite_color():
    """Test to see if the function displays the correct ouput if the poll is tied."""
    test_poll: dict[str, str] = {"John": "Blue", "Gabe": "Red"}
    assert favorite_color(test_poll) != "Red"


def test_blank_favorite_color():
    """Test to see if the function displays the correct output when given a blanck function."""
    test_poll: dict[str, str] = {}
    assert favorite_color(test_poll) is not None


def test_same_count():
    """Test to see if function counts correctly."""
    test_list: list[str] = ("truth", "courage", "wisdom", "strength")
    output: dict[str, int] = {'courage': 1, 'strength': 1, 'truth': 1, 'wisdom': 1}
    assert count(test_list) == output


def test_num_count():
    """Test to see if numbers work with the function."""
    test_list: list[str] = ("2", "4", "4")
    output: dict[str, int] = {"2": 1, "4": 2}
    assert count(test_list) == output


def test_blank_count_list():
    """Test to see that the function returns a blank dictionary."""
    test_list: list[str] = ()
    assert count(test_list) == {}


def test_num_alphabetizer():
    """Test to see if numbers work through the alphabetizer."""
    test_list: list[str] = ("100", "200", "150", "250")
    output: dict[str, list[str]] = {"1": ["100", "150"], "2": ["200", "250"]}
    assert alphabetizer(test_list) == output


def test_mixed_alphabetizer():
    """Test to see if the alphabetizer displays the correct output of mixed lists."""
    test_list: list[str] = ("1", "brown", "2", "crescent")
    output: dict[str, list[str]] = {"1": ["brown"], "2": ["crescent"]}
    assert alphabetizer(test_list) != output


def test_let_num_together_alphabetizer():
    """Test to see if list produces the correct dictionary."""
    test_list: list[str] = ("1Brown", "2Crescent", "3Staple")
    output: dict[str, list[str]] = {"1": ["Brown"], "2": ["Crescent"], "3": ["Staple"]}
    assert alphabetizer(test_list) != output


def test_rep_name_update_attendance():
    """Test to see if the function behaves correctly given repeated names."""
    test_log: dict[str, list[str]] = {"Monday": ["Jacob"]}
    assert update_attendance(test_log, "Monday", "Jacob") != {"Monday": ["Jacob"]}


def test_add_update_attendance():
    """Test to see if the function accurately updates the dictionary."""
    test_log: dict[str, list[str]] = {"Monday": ["Jacob"]}
    assert update_attendance(test_log, "Tuesday", "Jacob") == {"Monday": ["Jacob"], "Tuesday": ["Jacob"]}


def test_blank_update_attendance():
    """Test to see if the function has a correct output given a blank attendence log."""
    test_log: dict[str, list[str]] = {}
    assert update_attendance(test_log, "Monday", "Jacob") != {}