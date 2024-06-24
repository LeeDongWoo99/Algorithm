from itertools import permutations

def solution(numbers):
    num = [ch for ch in numbers] # 문자열 numbers의 각 문자를 리스트 num에 담는다.
    ans = [] # 결과를 저장할 리스트
    per = [] # num에 있는 요를 기준으로 만들 수 있는 모든 숫자 조합 생성을 저장할 리스트
    
    for i in range(1, len(num) + 1): # 1 ~ 문자열 길이 만큼 반복
        per+= list(permutations(num, i)) # num의 각 요소들로 길이가 i인 모든 순열을 생성하여 per 리스트에 추가
    lst = [int(("").join(p)) for p in per] # 각 순열을 문자열로 합친 후 정수로 변환하여 lst 리스트에 저장
    
    for n in lst:                            
        if n < 2:# 0, 1 일 경우 소수가 아니기 때문에, 다음 문자열로 넘어간다.             
            continue
        if n == 2:
            ans.append(n)
        check = True # check 값 초기화           
        for i in range(2,int(n**0.5) + 1): # 2 ~ n의 제곱근 +1 까지 반복
            if n % i == 0: # n이 소수인지 확인                      
                check = False
                break
        if check: # n이 소수일 경우
            ans.append(n) # 결과값에 n을 추가                      

    return len(set(ans)) # 결과값에 저장되어 있는 요소의 개수 출력