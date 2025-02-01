def solution(lottos, win_nums):
    zero_count = lottos.count(0) # 0의 개수
    check_count = 0
    
    rank = {6 : 1,
            5 : 2,
            4 : 3,
            3 : 4,
            2 : 5,
            1 : 6,
            0 : 6}
    
    for num in lottos:
        if num in win_nums:
            check_count += 1
            
    max_count = check_count + zero_count
    min_count = check_count
    
    return [rank[max_count], rank[min_count]]