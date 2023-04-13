from ex8 import count_spaces_and_commas_in_string
import pytest


def test_count_spaces_and_commas_in_string():
    input_string = "The colors in my studyroom are blue, green, and yellow."
    words_pattern = '[a-z]+'
    characters_pattern = '[,\s]+'
    assert count_spaces_and_commas_in_string(input_string, words_pattern, characters_pattern) == [['The', 'colors', 'in', 'my', 'studyroom', 'are', 'blue', 'green', 'and', 'yellow'], [' ', ' ', ' ', ' ', ' ', ' ', ', ', ', ', ' ']]

