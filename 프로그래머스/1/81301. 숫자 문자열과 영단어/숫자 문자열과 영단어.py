def solution(s):
    # 각 숫자에 대한 단어
    num = {"zero":"0","one":"1","two":"2","three":"3","four":"4","five":"5","six":"6",
           "seven":"7","eight":"8", "nine":"9"}
    for key in num:
        s = s.replace(key, num[key])
    return int(s)