def solution(board, skill):
    N = len(board)
    M = len(board[0])
    
    # 변화량을 기록할 누적 합 배열
    diff = [[0] * (M + 1) for _ in range(N + 1)]

    # skill 처리 (변화량 기록)
    for t, r1, c1, r2, c2, degree in skill:
        if t == 1:  # 공격
            degree = -degree
        # 좌측 상단에 변화량 추가
        diff[r1][c1] += degree
        # 우측 하단 다음 칸에 변화량 제거
        diff[r2 + 1][c2 + 1] += degree
        # 우측 상단에 변화량 제거
        diff[r1][c2 + 1] -= degree
        # 좌측 하단에 변화량 추가
        diff[r2 + 1][c1] -= degree

    # 누적 합 적용 (행 방향)
    for i in range(N):
        for j in range(M):
            diff[i][j + 1] += diff[i][j]

    # 누적 합 적용 (열 방향)
    for j in range(M):
        for i in range(N):
            diff[i + 1][j] += diff[i][j]

    # 최종 board에 diff를 적용하여 결과 계산
    answer = 0
    for i in range(N):
        for j in range(M):
            board[i][j] += diff[i][j]
            if board[i][j] > 0:
                answer += 1

    return answer
