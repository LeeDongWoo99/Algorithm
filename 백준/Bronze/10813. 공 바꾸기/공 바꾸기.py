N, M = map(int,input().split()) #바구니의 개수
data = []
for i in range(1,N+1):
	data.append(i)
while M > 0:
	n1, n2 =  map(int,input().split())
	u1 = data[n1-1]
	u2 = data[n2-1]
	data[n1-1]=u2
	data[n2-1]=u1
	M= M-1
for i in range(N):
	print(data[i],end=" ")
	
