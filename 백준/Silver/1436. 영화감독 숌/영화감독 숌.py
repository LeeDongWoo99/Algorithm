N = int(input())
st = 666
count = 0
lst = []

while(True):
    if "666" in str(st):
        lst.append(st)
        count += 1
        if count == N:
            break
    st += 1


print(lst[N-1])