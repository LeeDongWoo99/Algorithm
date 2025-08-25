import re

def solution(s):
    words = re.split(r'(\s+)', s)
    result = []
    for word in words:
        if word.isspace():
            result.append(word)
        else:
            new_word = ""
            for i in range(len(word)):
                if i % 2 == 0:
                    new_word += word[i].upper()
                else:
                    new_word += word[i].lower()
            result.append(new_word)
    return "".join(result)

