import sys
input = sys.stdin.readline

def decimal(n):
    ans = 0
    for i in range(n+1, 2*n +1):
        check = True
        if i < 2:
            continue
        elif i == 2:
            ans +=1
            continue
        for j in range(2, int(i ** 0.5)+1):
            if i % j == 0:
                check = False
                break
        if check:
              ans +=1
    return ans

while True:
    n = int(input())
    if n == 0:
        break
    result = decimal(n)
    print(result)
             


        
            
            
            