import re

input_string = "The colors in my studyroom are blue, green, and yellow."
words_pattern = '[a-z]+'
characters_pattern = r'[,\s]+'


def split_string_into_words_and_separators(string, words_pattern, characters_pattern):

    characters_pattern_validator = r'[,\s]+'
    x = re.findall(words_pattern, string, flags=re.IGNORECASE)
    y = re.findall(characters_pattern, string)
    if any(char.isdigit() for char in words_pattern):
        raise TypeError("No integers are allowed!")
    if not characters_pattern == characters_pattern_validator:
        raise ValueError("We should be looking for commas and spaces only!")
    return [x, y]


try:
    print(split_string_into_words_and_separators(
        input_string, words_pattern, characters_pattern))
except Exception as e:
    print("An error has occurred.", e)
