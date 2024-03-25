a = int(input())
c = int(input())

b_square = c*c - a*a
print(b_square)

############################################################################
직각삼각형의 한 변의 길이를 나타내는 정수 a와 빗변의 길이를 나타내는 정수 c가 주어질 때, 다른 한 변의 길이 b를 출력하도록 코드를 완성해 주세요.

a = int(input())
c = int(input())

b_square = c * c - a * a
for b in range(1, b_square + 1):
  if b * b == b_square:
    print(b)


-------------------다른 방법(GPT)---------------------
a = int(input())
c = int(input())

b_square = c * c - a * a
b = int(b_square ** 0.5)  # 빗변의 제곱에서 한 변의 제곱을 빼서 제곱근을 취합니다.

print(b)

0.5를 거듭제곱하는 것은 제곱근을 계산하는 것이며, 해당 수의 0.5 승을 취한 값을 의미한다.

