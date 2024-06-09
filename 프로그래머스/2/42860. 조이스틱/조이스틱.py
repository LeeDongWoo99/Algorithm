def solution(name):
    size = len(name)
    alpha = {
        'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7, 'I': 8, 'J': 9, 
        'K': 10, 'L': 11, 'M': 12, 'N': 13, 'O': 12, 'P': 11, 'Q': 10, 'R': 9, 'S': 8, 
        'T': 7, 'U': 6, 'V': 5, 'W': 4, 'X': 3, 'Y': 2, 'Z': 1
    }

    # 각 자리의 알파벳 변경 비용을 계산
    ans = 0
    for char in name:
        ans += alpha[char]

    # 최소 커서 이동 횟수 계산
    min_moves = size - 1

    for i in range(size):
        next_index = i + 1
        while next_index < size and name[next_index] == 'A':
            next_index += 1
        
        distance = min(i, size - next_index)
        min_moves = min(min_moves, i + size - next_index + distance)
    
    return ans + min_moves

# 테스트 케이스
print(solution("JEROEN"))  # 예시 출력: 56
print(solution("JAN"))     # 예시 출력: 23
print(solution("JALL"))    # 추가 테스트 케이스
