def solution(x):
    res = split_x(x)
    if x % sum(res) == 0: answer = True
    else : answer = False
    return answer

def split_x(x):
    list =[]
    while x > 0:
        list.append(x % 10)
        x = x // 10
    return list

solution(1008)

'''
def Harshad(n):
    # n은 하샤드 수 인가요?
    return n % sum([int(c) for c in str(n)]) == 0'''