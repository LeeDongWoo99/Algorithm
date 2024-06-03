def solution(board, moves):
    basket = []
    result = 0
    for move in moves:
        for row in board:
            # 현재 행에서 크레인 이동 방향에 인형이 있을 경우
            if row[move-1] != 0:
                doll = row[move-1]
                row[move-1] = 0
                if basket and basket[-1] == doll:
                    result += 2
                    basket.pop()
                else:
                    basket.append(doll)
                break
            
    return result