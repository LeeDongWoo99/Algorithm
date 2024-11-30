def solution(array):
    # 빈도수 계산용 딕셔너리
    freq = {}
    for num in array:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1

    # 최빈값 및 최대 빈도 계산
    max_occurrence = 0
    max_num = -1
    for num, count in freq.items():
        if count > max_occurrence:
            max_occurrence = count
            max_num = num
        elif count == max_occurrence:  # 최빈값이 여러 개일 경우
            max_num = -1

    return max_num
