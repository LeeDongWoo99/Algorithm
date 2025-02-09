from itertools import permutations

def is_prime(num):
    if num < 2:
        return False
    if num == 2:
        return True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


def solution(numbers):
    num = [ch for ch in numbers] # 문자열에 있는 숫자 요소들을 나눔
    per = set()
    ans = 0
    
    for i in range(1, len(numbers) + 1):
        for p in permutations(num, i):
            per.add(int("".join(p)))
                    
    for nm in per:
        if is_prime(nm):
            ans += 1
        
    return ans