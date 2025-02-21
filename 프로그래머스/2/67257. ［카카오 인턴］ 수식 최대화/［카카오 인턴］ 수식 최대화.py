import re
from itertools import permutations

def solution(expression):
    tokens = re.split(r'(\D)', expression)
    numbers = list(map(int, tokens[::2]))
    ops = tokens[1::2]
    
    max_result = 0
    # 2️⃣ 모든 연산자 우선순위 경우의 수 탐색
    for op_order in permutations(['+', '-', '*']):  
        num_copy = numbers[:]  # 숫자 복사본
        op_copy = ops[:]  # 연산자 복사본

        # 3️⃣ 현재 연산자 우선순위대로 반복적으로 연산 수행
        for op in op_order:  
            while op in op_copy:  # 해당 연산자가 있을 때만 처리
                idx = op_copy.index(op)  # 연산자 위치 찾기

                # 계산 수행
                if op == '+':
                    result = num_copy[idx] + num_copy[idx + 1]
                elif op == '-':
                    result = num_copy[idx] - num_copy[idx + 1]
                elif op == '*':
                    result = num_copy[idx] * num_copy[idx + 1]

                # 리스트 업데이트 (연산자 및 숫자 제거 후 결과 삽입)
                num_copy[idx] = result
                del num_copy[idx + 1]  # 사용한 숫자 제거
                del op_copy[idx]  # 사용한 연산자 제거

        # 4️⃣ 최종 결과값 갱신
        max_result = max(max_result, abs(num_copy[0]))

    return max_result