def solution(s):
    st = s.split(" ")
    new_words = []
    for word in st:
        new_word = ''
        for i in range(len(word)):
            # 짝수인 경우
            if i % 2 == 0:
                new_word += word[i].upper()
            # 홀수인 경우
            else:
                new_word += word[i].lower()
        new_words.append(new_word)
    return ' '.join(new_words)
