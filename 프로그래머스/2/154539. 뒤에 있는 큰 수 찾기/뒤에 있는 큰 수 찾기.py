def solution(numbers):
    answer = [-1] * len(numbers)  # 초기값은 -1로 설정
    stack = []  # 숫자의 인덱스를 저장할 스택
    for i in range(len(numbers)):
        while stack and numbers[stack[-1]] < numbers[i]:
            answer[stack.pop()] = numbers[i]  # 스택의 값이 현재 숫자보다 작으면 결과 리스트를 업데이트
        stack.append(i)  # 현재 숫자의 인덱스를 스택에 추가
    return answer

-------------------------------------------풀이----------------------------------------
배열의 각 원소들에 대해 뒤에 있는 숫자 중에서 자신 보다 크면서 가까이 있는 수를 뒷 큰수라고 한다.
이 문제는 뒷 숫자가 앞에 숫자랑 같거나 큰 숫자가 뒷 수자보다 멀리 있어도 stack을 통해 전부 비교해서 업데이트 하는게 핵심이다.
numbers	            result
[2, 3, 3, 5]	    [3, 5, 5, -1]
[9, 1, 5, 3, 6, 2]	[-1, 5, 6, 6, -1, -1]
    
입출력 예제 1을 보면 처음에는 "while stack and numbers[stack[-1]] < numbers[i]:" 조건에 의해 stack이 null이기 때문에 while 문이 동작하지 않고 빠져나와 현재 숫자의 인덱스를 
stack에 추가한다. (while 문 조건에 해당하면 조건이 해당하지 않을 때까지 루프가 돌아가고 빠져나가게 된다.
    ㄴ이 조건문을 통해 뒤에 있는 숫자가 작아도 현재 숫자의 인덱스를 stack에 넣고 더 뒤에 있는 큰 숫자를 찾고 비교할 수 있다. 
그 후 for문 루프가 돌아 i=1이 되고 numbers[stack[-1]](stack에 최근에 들어가 값:0)과 numbers[i]를 비교한다. 즉, numbers[0] < numbers[1]이다. 그러면 뒷 큰수에 해당되고 stack에 
가장 마지막 항목(최근에 들어온 값)이 제거되고 반환되어 answer[]인덱스에 들어가고 뒷 큰수가 그 자리에 들어가게 된다. answer[3, -1, -1, -1] 
그 후 stack에 값이 없기 때문에 while문을 나오고 stack에 1값을 넣는다.
i가 2가 되고 stack[-1] 값은 1이기 때문에 numbers[1] < numbers[2]가 되는데 두 숫자가 같음으로 stack에 2를 넣고 for 루프가 돌아간다.
i가 3이 되고 stack에는 [1,2] 값이 들어 있다. 조건문에 따라 비교했을 때 numbers[3] 값은 5이기 때문에 뒷 큰수에 해당되고 answer[2]에 5를 넣고, while 조건문에 stack이 있고 stack[-1] 값이
1이고 numbers[3] 값이 더 큼으로써 anser[1]에도 numbers[3] 값이 들어가게 된다.
그래서 answer[3, 5, 5, -1] 값이 된다.

뒤에 있는 숫자가 같거나 작어도 큰 숫자가 그 뒤에 있을 경우 for 루프가 돌면서 앞에 작았었던 숫자들에 인덱스를 stack에 보관하고 있어 최근에 들어온것부터 하나씩 비교 하기 때문에 
전체적으로 비교가 가능하다.
