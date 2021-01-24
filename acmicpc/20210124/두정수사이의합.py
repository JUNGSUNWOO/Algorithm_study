a = 5
b = 3

def solution(a, b):
    answer = 0
    if a > b:
        max = a; min = b
    else :
        max = b; min = a
    for i in range(min, max+1):
        answer += i

    return answer


res = solution(a, b)
print(res)


'''
def adder(a, b):
    if a > b: a, b = b, a

    return sum(range(a,b+1))
    '''