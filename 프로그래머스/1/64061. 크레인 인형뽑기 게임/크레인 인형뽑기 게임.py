def solution(board, moves):
    box = []
    result = 0

    for move in moves:
        for row in board:
            if row[move - 1] != 0:
                doll = row[move - 1]
                row[move - 1] = 0
                if box and box[-1] == doll:
                    result += 2
                    box.pop()
                else:
                    box.append(doll)
                break

    return result
