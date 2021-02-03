def solution(d, budget):
    d.sort()
    answer = 0
    for i in d:
        print(answer)
        budget -= i
        answer += 1
        if budget == 0 : print(answer);return answer
        if budget < 0 : print(answer-1);return answer-1

def solution2(d, budget):
    d.sort()
    cnt = 0
    for i in d:
        print(cnt)
        budget -= i
        if budget >= 0: cnt += 1
    return cnt

d = [-1,-2,-3,0.5,0.2,0.4,0,20]
budget = 1000000000
solution(d, budget)
print('\n')
solution2(d, budget)

'''
def solution(d, budget):
    d.sort()
    while budget < sum(d):
        d.pop()
    return len(d)
'''