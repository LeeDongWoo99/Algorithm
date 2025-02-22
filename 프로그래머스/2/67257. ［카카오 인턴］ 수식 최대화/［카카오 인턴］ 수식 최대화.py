import re
from itertools import permutations

def solution(expression):
    tokens = re.split(r'(\D)', expression)
    numbers = list(map(int, tokens[::2]))  # 숫자들
    ops = tokens[1::2]  # 연산자들
    
    max_result = 0  # 최대값 저장

    for op_order in permutations(['+', '-', '*']):  # 연산자 순서에 대해 반복
        nums = numbers[:]  # 원본 리스트 그대로 사용
        ops_copy = ops[:]  # 연산자 리스트 그대로 사용

        for op in op_order:  # 각 연산자 순서대로 처리
            while op in ops_copy:  # 해당 연산자가 있을 때만 처리
                idx = ops_copy.index(op)  # 연산자 위치 찾기

                # 계산 수행
                if op == '+':
                    result = nums[idx] + nums[idx + 1]
                elif op == '-':
                    result = nums[idx] - nums[idx + 1]
                elif op == '*':
                    result = nums[idx] * nums[idx + 1]

                # 리스트 업데이트 (연산자 및 숫자 제거 후 결과 삽입)
                nums[idx] = result
                del nums[idx + 1]  # 사용한 숫자 제거
                del ops_copy[idx]  # 사용한 연산자 제거

        max_result = max(max_result, abs(nums[0]))  # 계산된 결과 중 최대값을 저장

    return max_result
