def solution(numbers, our_score, score_list):
    answer = []
    for i in range(len(numbers)):
        if our_score[i] == score_list[numbers[i]-1]:
            answer.append("Same")
        else:
            answer.append("Different")
    
    return answer

-------------------------------------------------------------------------
위에 풀이는 프로그래머스 특성상 한 줄만 수정해서 맞추면 정답이 되기 때문에 문제만 보고 다시 코딩을 했다.
    
def solution(numbers, our_score, score_list):
    result = []
    for i in range(len(numbers)):
        if our_score[i] == score_list[numbers[i]-1]:
            result.append("Same")
        else:
            result.append("Different")
    return result
      
numbers = [3, 4]
our_score = [85, 93]
score_list = [85, 92, 38, 93, 48, 85, 92, 56]

result = solution(numbers, our_score, score_list)
print(result)
