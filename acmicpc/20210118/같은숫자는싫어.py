arr = [4, 4, 4, 3, 3]

def solution(arr):
    answer = []
    tmp = None
    for i in arr :
        if i != tmp:
            answer.append(i)
        tmp = i

    return answer

res = solution(arr)
print(res)


'''
def no_continuous(s):
    a = []
    for i in s:
        if a[-1:] == [i]: continue
        a.append(i)
    return a
'''