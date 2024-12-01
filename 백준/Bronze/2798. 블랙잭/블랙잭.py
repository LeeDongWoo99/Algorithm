num_input= list(map(int,input().split()))
N = num_input[0]
M = num_input[1]
lst = list(map(int, input().split()))
max_ans = 0
for i in range(0, N-2):
    for j in range(i+1, N-1):
        for z in range(j+1, N):
            ans = lst[i] + lst[j] + lst[z]
            if ans <= M and ans > max_ans:
                max_ans = ans
print(max_ans)

