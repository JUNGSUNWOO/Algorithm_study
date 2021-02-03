def solution2(d, budget):
    d.sort()
    cnt = 0
    for i in d:
        print(i, budget,cnt)
        budget -= i
        if budget >= 0: cnt += 1
    return cnt

d = [0.3,0.4,1.099]

budget = 1.8
print('\n')
res2 =solution2(d, budget)

print(res2)

'''
def solution(d, budget):
    d.sort()
    while budget < sum(d):
        d.pop()
    return len(d)
'''