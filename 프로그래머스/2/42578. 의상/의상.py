from itertools import combinations

def solution(clothes):
    # 각 옷 종류를 키로 가지고 옷들의 리스트를 값으로 가지는 딕셔너리 생성
    clothes_dict = {}
    for item in clothes:
        cloth = item[0]
        cloth_type = item[1]
        if cloth_type in clothes_dict:
            clothes_dict[cloth_type].append(cloth)
        else:
            clothes_dict[cloth_type] = [cloth]
    
    # 각 옷 종류에 대해 옷을 선택하는 경우의 수 계산
    answer = 1
    for key in clothes_dict:
        answer *= (len(clothes_dict[key]) + 1)  # 해당 종류의 옷을 선택하지 않는 경우를 포함하기 위해 +1
    
    # 모든 옷을 입지 않은 경우의 수는 제외하므로 1을 빼준다.
    return answer - 1
