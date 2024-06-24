from itertools import permutations

def solution(numbers):
    ans = []
    num = [ch for ch in numbers]
    per = []
    
    for i in range(1, len(num) + 1):
        per+= list(permutations(num, i))
    lst = [int(("").join(p)) for p in per]
    
    for n in lst:                            
        if n < 2:             
            continue
        check = True            
        for i in range(2,int(n**0.5) + 1):        
            if n % i == 0:                       
                check = False
                break
        if check:
            ans.append(n)                      

    return len(set(ans))    