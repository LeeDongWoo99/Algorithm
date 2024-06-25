n = int(input())  # 사용자로부터 n 입력받기
cnt = 0  
num = 1  

while True:  
    if "666" in str(num):  
        cnt += 1  
    if n == cnt:  
        if n == 0: # 입력값을 0을 입력했을 때
            print(666) # 0번째 종말의 수인 666을 출력
        else:
            print(num)  
        break  
    num += 1  