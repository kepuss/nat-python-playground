import re

input_string = "The colors in my studyroom are blue, green, and yellow."
words_pattern = '[a-z]+'
words_pattern_int = '^\d{5}$'
characters_pattern = '[,\s]+'


def count_spaces_and_commas_in_astring(string, words_pattern, characters_pattern):

    x = re.findall(words_pattern, string, flags=re.IGNORECASE)
    y = re.findall(characters_pattern, string)
    if any(char.isdigit() for char in words_pattern):
        raise TypeError("No integers are allowed!")
    if not characters_pattern is '[,\s]+':
        raise ValueError("We're looking for commas and spaces only!")
    return [x, y]


try:
    print(count_spaces_and_commas_in_astring(
        input_string, words_pattern, characters_pattern))
except Exception as e:
    print("An error has occurred.", e)
