def solution(dartResult):
    # 각 다트 횟수별 계산된 점수를 저장할 변수 초기화
    score = []
    # 각 횟수를 체크하기 위한 변수 초기화
    chk = -1  # -1로 초기화하여 첫 다트부터 시작

    i = 0
    while i < len(dartResult):
        # 숫자인 경우 처리
        if dartResult[i].isdigit():
            # 두 자리 숫자인 경우 처리
            if i + 1 < len(dartResult) and dartResult[i + 1].isdigit():
                ans = int(dartResult[i:i+2])
                i += 1  # 두 자리 숫자를 처리했으므로 인덱스를 한 번 더 증가시킴
            else:
                ans = int(dartResult[i])
            chk += 1
            score.append(ans)
        # 문자인 경우 처리
        elif dartResult[i].isalpha():
            if dartResult[i] == "S":
                score[chk] **= 1
            elif dartResult[i] == "D":
                score[chk] **= 2
            elif dartResult[i] == "T":
                score[chk] **= 3
        # 옵션인 경우 처리
        else:
            if dartResult[i] == "*":
                score[chk] *= 2
                if chk > 0:
                    score[chk-1] *= 2
            elif dartResult[i] == "#":
                score[chk] *= -1
        i += 1

    # 중첩 효과 적용 (추가)
    for j in range(len(score)):
        if dartResult[j] == "*":
            if j > 0 and dartResult[j-2] == "*":
                score[j] *= 2  # 중첩된 스타상은 4배
            elif j > 0 and dartResult[j-2] == "#":
                score[j] *= -2  # 중첩된 아차상은 -2배
        elif dartResult[j] == "#":
            if j > 0 and dartResult[j-2] == "*":
                score[j] *= -2  # 중첩된 스타상은 -2배
            elif j > 0 and dartResult[j-2] == "#":
                score[j] *= 2  # 중첩된 아차상은 4배
    result = sum(score)
    return result
