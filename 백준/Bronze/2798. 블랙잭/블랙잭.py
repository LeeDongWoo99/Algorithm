import itertools

#총 카드의 수
n, m = input().split()
# 카드의 숫자
data = list(map(int, input().split()))
# while True:
#     if n == len(data):
nCr = itertools.combinations(data, 3)
result = 0
coc = []
for i in nCr:
    if sum(i) <= int(m):
        coc.append(sum(i))

coc.sort(reverse=True)
print(coc[0])
    
  
  