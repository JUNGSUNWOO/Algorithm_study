n = 3
lost = [1,2]
reserve = [2,3]

def solution(n, lost, reserve):
    new_lost = list(set(lost) - set(reserve))
    new_reserve = list(set(reserve) - set(lost))
    print(new_lost, new_reserve)

    answer = n - len(new_lost)
    for i in new_lost:
        if i - 1 in new_reserve:
            new_reserve.remove(i-1)
            answer += 1
        elif i + 1 in new_reserve:
            new_reserve.remove(i+1)
            answer += 1

    return answer

ans = solution(n,lost,reserve)
print("ans", ans)

'''
def solution(n, lost, reserve):
    _reserve = [r for r in reserve if r not in lost]
    _lost = [l for l in lost if l not in reserve]
    for r in _reserve:
        f = r - 1
        b = r + 1
        if f in _lost:
            _lost.remove(f)
        elif b in _lost:
            _lost.remove(b)
    return n - len(_lost)'''