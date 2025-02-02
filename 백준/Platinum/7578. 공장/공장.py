import sys

input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

position = {value: index for index, value in enumerate(B)}
A_mapped = [position[value] for value in A]

def merge_sort(arr):
    if len(arr) < 2:
        return arr, 0

    mid = len(arr) // 2
    left, left_inv = merge_sort(arr[:mid])
    right, right_inv = merge_sort(arr[mid:])

    merged, split_inv = merge(left, right)

    return merged, left_inv + right_inv + split_inv


def merge(left, right):
    result = []
    i = j = inv_count = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            inv_count += len(left) - i  
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result, inv_count

_, answer = merge_sort(A_mapped)
print(answer)