def solution(board, moves):
    result = 0
    basket = []
    for move in moves:
        for row in board:
            if row[move-1] != 0:
                doll = row[move-1]
                row[move-1] = 0
                if basket and basket[-1] == doll:
                    result +=2
                    basket.pop()
                else:
                    basket.append(doll)
                break
    return result