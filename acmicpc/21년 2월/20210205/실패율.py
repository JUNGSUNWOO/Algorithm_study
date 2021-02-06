def solution(N, stages):
    fail = dict()
    for i in range(1,N+2):
        fail[i] = 0
    user = len(stages)
    for i in stages:
        fail[i] += 1
    for (key, value) in fail.items():
        if user==0 : break
        fail[key] = value / user
        user -= value
    del fail[N+1]
    ans = sorted(fail.items(), key=(lambda x:x[1]), reverse=True)

    res = []
    for (x,y) in ans:
        res.append(x)
    return res

N = 4

stages = [4,4,4,4,4]

print(solution(N, stages))
'''
def solution(N, stages):
    result = {}
    denominator = len(stages)
    for stage in range(1, N+1):
        if denominator != 0:
            count = stages.count(stage)
            result[stage] = count / denominator
            denominator -= count
        else:
            result[stage] = 0
    return sorted(result, key=lambda x : result[x], reverse=True)'''