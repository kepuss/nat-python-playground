import re
string = "hello, my name is Peter, I am 26 years old"
words_pattern = '[a-z]+'
characters_pattern = ' +'


x = re.findall(words_pattern, string, flags=re.IGNORECASE)
y = re.findall(characters_pattern, string)

#x = re.find(' |, ', string)

print(x, y)