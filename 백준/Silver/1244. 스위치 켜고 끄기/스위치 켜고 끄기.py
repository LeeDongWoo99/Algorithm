N = int(input())  # 스위치 개수
switch = [-1] + list(map(int, input().split()))  # 스위치 정보
students= int(input())  # 학생 수

def change(num):
    switch[num] = 1 - switch[num]  # 0이면 1, 1이면 0으로 변경

for _ in range(students): 
    sex, num = map(int, input().split())  # 학생 정보 입력 (성별, 번호)
    
    if sex == 1:  # 남학생 처리 (배수 변경)
        for i in range(num, N + 1, num):
            change(i)

    else:  # 여학생 처리 (대칭 변경)
        change(num)
        for k in range(N//2):
            if num + k > N or num - k < 1 : break
            if switch[num + k] == switch[num - k]:
                change(num + k)
                change(num - k)
            else:
                break

# 결과 출력 (20개씩 줄 바꿈)
for i in range(1, N+1):
    print(switch[i], end = " ")
    if i % 20 == 0 :
        print()