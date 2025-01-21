def solution(progresses, speeds):
    ans = []
    trial = 0
    count = 0
    while len(progresses) > 0:
        if progresses[0] + speeds[0] * trial >= 100:
            count += 1
            progresses.pop(0)
            speeds.pop(0)
        else:
            if count > 0:
                ans.append(count)
                count = 0
            trial += 1
    ans.append(count)
    return ans