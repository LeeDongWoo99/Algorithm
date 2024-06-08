def solution(numbers, target):
    def dfs(idx, current_sum):
        if idx == len(numbers):
            if current_sum == target:
                return 1  # 현재까지의 합이 목표값과 일치하는 경우 1 반환
            else:
                return 0  # 현재까지의 합이 목표값과 일치하지 않는 경우 0 반환
        else:
            # 현재 숫자를 더하거나 빼는 경우의 결과를 모두 더해서 반환
            return dfs(idx + 1, current_sum + numbers[idx]) + dfs(idx + 1, current_sum - numbers[idx])

    # 최초의 인덱스와 현재 합인 0으로 시작하여 탐색 시작
    return dfs(0, 0)