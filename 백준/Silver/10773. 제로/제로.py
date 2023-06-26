n = int(input())

li = []

for i in range(n):
	m = int(input())
	if m == 0:
		li.pop()
	else :
		li.append(m)

print(sum(li))
	
