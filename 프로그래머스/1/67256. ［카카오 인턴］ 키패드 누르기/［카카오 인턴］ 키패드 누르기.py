def solution(numbers, hand):
    # 키패드를 2차원 배열로 정의합니다.
    keypad = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
        ['*', 0, '#']
    ]
    
    # 손의 현재 위치를 저장할 변수를 정의합니다. 시작 위치는 '*'와 '#'입니다.
    left_pos = (3, 0)
    right_pos = (3, 2)
    
    result = ""

    # 키패드에서 각 숫자의 위치를 저장하는 딕셔너리를 만듭니다.
    pos_dict = {keypad[row][col]: (row, col) for row in range(4) for col in range(3)}

    for num in numbers:
        if num in [1, 4, 7]:
            result += "L"
            left_pos = pos_dict[num]
        elif num in [3, 6, 9]:
            result += "R"
            right_pos = pos_dict[num]
        else:
            target_pos = pos_dict[num]
            left_dist = abs(left_pos[0] - target_pos[0]) + abs(left_pos[1] - target_pos[1])
            right_dist = abs(right_pos[0] - target_pos[0]) + abs(right_pos[1] - target_pos[1])
            
            if left_dist < right_dist:
                result += "L"
                left_pos = target_pos
            elif right_dist < left_dist:
                result += "R"
                right_pos = target_pos
            else:
                if hand == "left":
                    result += "L"
                    left_pos = target_pos
                else:
                    result += "R"
                    right_pos = target_pos

    return result
