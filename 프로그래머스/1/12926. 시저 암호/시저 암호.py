def solution(s, n):
    low = "abcdefghijklmnopqrstuvwxyz" # 
    up = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    answer = ''
    for ch in s:
        if ch.islower():
            ind = (low.index(ch)+n) % 26
            answer += low[ind] 
        elif ch.isupper():
            ind = (up.index(ch)+n) % 26
            answer += up[ind]
        else: # 공백일 경우 공백 추가
            answer += " "
    return answer