def solution(s, n):
    result = ""
    for ch in s:
        if ch.islower():
            result += chr((ord(ch) - ord('a') + n) % 26 + ord('a'))
        elif ch.isupper():
            result += chr((ord(ch) - ord('A') + n) % 26 + ord('A'))
        else:
            result += ch
    return result