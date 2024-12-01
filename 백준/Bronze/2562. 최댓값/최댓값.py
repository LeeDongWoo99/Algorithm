arr = []
for _ in range(9):
    arr.append(int(input()))

max_num = arr[0]
max_index = 0

for index in range(1, len(arr)):
    if max_num < arr[index]:
        max_num = arr[index]
        max_index = index
print(arr[max_index])
print(max_index + 1)