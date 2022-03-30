import re

expression = r"\b_[a-zA-Z0-9]+\b"
text = input()

result = re.findall(expression, text)

words_list = []

for word in result:
    words_list.append(word[1:])

print(",".join(words_list))

