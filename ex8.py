import re
string = "The colors in my studyroom are blue, green, and yellow."
words_pattern = '[a-z]+'
characters_pattern = "[,\s]+"


x = re.findall(words_pattern, string, flags=re.IGNORECASE)
y = re.findall(characters_pattern, string)

print([x, y])