def solution(n):
    list= []
    while n > 0:
        list.append(n % 10)
        n = n //10
    return list

n = 1234
print(solution(n))

'''
def digit_reverse(n):
    return list(map(int, reversed(str(n))))'''