def solution(n):
    tmp = 0
    while True:
        if tmp ** 2 == n:
            return (tmp+1) ** 2
        elif tmp **2 > n:
            return -1
        tmp += 1

print(solution(3))

'''
def nextSqure(n):
    return n == int(n**.5)**2 and int(n**.5+1)**2 or 'no' '''