def solution(numbers, hand):
    result = ""
    left_pos = (3, 0)  # '*'의 초기 위치
    right_pos = (3, 2)  # '#'의 초기 위치
    hand = "L" if hand == "left" else "R"

    # 키패드의 좌표 정의
    keypad_pos = {
        1: (0, 0), 2: (0, 1), 3: (0, 2),
        4: (1, 0), 5: (1, 1), 6: (1, 2),
        7: (2, 0), 8: (2, 1), 9: (2, 2),
        0: (3, 1)
    }

    for num in numbers:
        if num in [1, 4, 7]:
            result += "L"
            left_pos = keypad_pos[num]
        elif num in [3, 6, 9]:
            result += "R"
            right_pos = keypad_pos[num]
        else:
            target_pos = keypad_pos[num]
            left_dist = abs(left_pos[0] - target_pos[0]) + abs(left_pos[1] - target_pos[1])
            right_dist = abs(right_pos[0] - target_pos[0]) + abs(right_pos[1] - target_pos[1])

            if left_dist < right_dist:
                result += "L"
                left_pos = target_pos
            elif right_dist < left_dist:
                result += "R"
                right_pos = target_pos
            else:
                if hand == "L":
                    result += "L"
                    left_pos = target_pos
                else:
                    result += "R"
                    right_pos = target_pos

    return result
