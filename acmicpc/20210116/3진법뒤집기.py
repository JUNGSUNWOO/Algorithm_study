n = 45
def find_3(n):
    i  = 0
    while True:
        if 3 ** i > n: break
        i += 1
    return i - 1
def make_hat(n):
    hat = [0] * (find_3(n)+1)
    while True:
        hat[find_3(n)] += 1
        n -= 3 ** find_3(n)
        if n < 3:
            for i in range(0, n):
                hat[0] += 1
            break
    return hat

def reverse_hat(hat):
    hat.reverse()
    return hat

def make_10(hat):
    answer = 0
    cnt = 0
    for i in hat:
        answer += i * (3 ** cnt)
        cnt += 1
    return answer

def solution(n):
    hat = make_hat(n)
    hat = reverse_hat(hat)
    answer = make_10(hat)
    return answer

res = solution(n)
print(res)


'''
def solution(n):
    answer = 0
    cnt = 1
    a = ''
    while n>0:
        a+=str(n%3)
        n = n//3
    print(a)
    for b in range(len(a),0,-1):
        answer += (int(a[b-1])*cnt)
        cnt *= 3
    return answer
'''