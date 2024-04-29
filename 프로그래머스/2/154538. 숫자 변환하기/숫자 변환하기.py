def solution(x, y, n):
    if x >= y:
        return 0
    
    # dp[i]는 숫자 i를 y로 변환하는 최소 연산 횟수를 저장하는 배열
    dp = [float('inf')] * (y + 1)
    dp[x] = 0  # 초기값 설정
    
    for i in range(x, y + 1):
        # 현재 숫자에서 n을 더하는 경우
        if i + n <= y:
            dp[i + n] = min(dp[i + n], dp[i] + 1)
        
        # 현재 숫자에 2를 곱하는 경우
        if i * 2 <= y:
            dp[i * 2] = min(dp[i * 2], dp[i] + 1)
        
        # 현재 숫자에 3을 곱하는 경우
        if i * 3 <= y:
            dp[i * 3] = min(dp[i * 3], dp[i] + 1)
    
    # 최종 결과 반환
    return dp[y] if dp[y] != float('inf') else -1