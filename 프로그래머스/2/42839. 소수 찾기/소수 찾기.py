from itertools import permutations

def solution(numbers):
    num = [x for x in numbers] # 문자열에 문자들을 쪼개서 리스트에 저장
    per = []
    ans = []
    
    for i in range(1, len(num) +1):
        per += permutations(num, i)
    lst = [int("". join (x)) for x in per]
    
    for n in lst:
        if n <= 1:
            continue
        if n == 2:
            ans.append(n)
        check = True
        for i in range(2, int(n ** 0.5) +1):
            if n % i == 0:
                check = False
                break
        if check:
            ans.append(n)
            
    return len(set(ans))