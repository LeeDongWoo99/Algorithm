def solution(s):
    answer = []

    if len(s) == 1:
        return 1

    for step in range(1, len(s)//2 + 1):
        result = ''
        tmp = s[:step]
        cnt = 1
        for j in range(step, len(s), step):
            if tmp == s[j : j + step]:
                cnt += 1
            else:
                if cnt > 1:
                    result += str(cnt) + tmp
                else:
                    result += tmp
                cnt = 1
                tmp = s[j:j + step]
        if cnt > 1:
            result += str(cnt) + tmp
        else:
            result += tmp
        answer.append(len(result))
    return min(answer)