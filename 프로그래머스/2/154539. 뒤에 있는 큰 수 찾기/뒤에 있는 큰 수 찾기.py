def solution(numbers):
    answer = [-1] * len(numbers)  # 초기값은 -1로 설정
    stack = []  # 숫자의 인덱스를 저장할 스택
    for i in range(len(numbers)):
        while stack and numbers[stack[-1]] < numbers[i]:
            answer[stack.pop()] = numbers[i]  # 스택의 값이 현재 숫자보다 작으면 결과 리스트를 업데이트
        stack.append(i)  # 현재 숫자의 인덱스를 스택에 추가
    return answer
