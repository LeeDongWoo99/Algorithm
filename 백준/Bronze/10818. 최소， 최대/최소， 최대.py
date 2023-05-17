n = int(input())
while True:
    numbers = list(map(int,input().split()))
    if len(numbers) == n:
        print(min(numbers), max(numbers))
        break
    else:
        print(f"정수의 개수는 {n} 리스트의 개수는 {len(numbers)} 이다.")
        print("정수의 갯수와 리스트의 객수가 맞지 않습니다. 다시 입력하세요:")
        continue

    