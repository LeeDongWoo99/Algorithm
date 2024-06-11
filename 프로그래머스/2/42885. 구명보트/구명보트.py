def solution(people, limit):
    # 내림차순으로 정렬
    people.sort(reverse=True)
    # 가장 가벼운 사람을 가리키는 포인터
    left = 0
    # 가장 무거운 사람을 가리키는 포인터
    right = len(people) - 1
    # 필요한 구명보트의 수
    result = 0

    # 두 포인터가 서로 교차할 때까지 반복합니다.
    while left <= right:
        # 가장 가벼운 사람과 가장 무거운 사람의 무게 합이 제한 이내라면
        if people[left] + people[right] <= limit:
            # 가벼운 사람도 보트에 탑니다.
            right -= 1
        # 무거운 사람은 항상 보트에 탑니다.
        left += 1
        # 보트 하나 추가
        result += 1

    return result