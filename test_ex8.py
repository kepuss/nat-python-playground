from ex8 import split_string_into_words_and_separators
import pytest

# def test_count_spaces_and_commas_in_string():
#     input_string = "Hello, world!"
#     words_pattern = '[a-z]+'
#     characters_pattern = '[,\s]+'
#     expected_output = (['Hello', 'world'], [', '])
#     assert count_spaces_and_commas_in_string(input_string, words_pattern, characters_pattern) == expected_output

def test_split_string_into_words_and_separators_matches_expected_output():
    input_string = "The colors in my studyroom are blue, green, and yellow."
    words_pattern = '[a-z]+'
    characters_pattern = r'[,\s]+'
    expected_output = [['The', 'colors', 'in', 'my', 'studyroom', 'are', 'blue', 'green', 'and', 'yellow'], [' ', ' ', ' ', ' ', ' ', ' ', ', ', ', ', ' ']]
    assert split_string_into_words_and_separators(input_string, words_pattern, characters_pattern) == expected_output


def test_split_string_into_words_and_separators_raises_TypeError_for_integer_in_words_pattern():
    with pytest.raises(TypeError):
        input_string = "The colors in my studyroom are blue, green, and yellow."
        words_pattern = '[1-9]|10'
        characters_pattern = r'[,\s]+'
        split_string_into_words_and_separators(input_string, words_pattern, characters_pattern)

def test_split_string_into_words_and_separators_raises_ValueError_for_other_separators():
    with pytest.raises(ValueError):
        input_string = "The colors in my studyroom are blue, green, and yellow."
        words_pattern = '[a-z]+'
        characters_pattern = r'[;\s]+'
        split_string_into_words_and_separators(input_string, words_pattern, characters_pattern)