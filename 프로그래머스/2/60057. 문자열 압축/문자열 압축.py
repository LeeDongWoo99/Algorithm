def solution(s):
    answer = []

    if len(s) == 1:
        return 1

    for step in range(1, len(s) // 2 + 1):
        result = ''
        prev = s[: step]
        count = 1
        for j in range(step, len(s), step):
            if prev == s[j: j + step]:
                count += 1
            else:
                if count > 1:
                    result += str(count) + prev
                else:
                    result += prev
                count = 1
                prev = s[j: j + step]
        if count > 1:
            result += str(count) + prev
        else:
            result += prev
        answer.append(len(result))
    return min(answer)