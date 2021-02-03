
def solution(n, m):
    gcd = 1
    n_cd = []
    for i in range(1,n//2+1):
        if n % i ==0:n_cd.append(i)

    if m % n == 0: gcd = n
    else:
        for i in range(len(n_cd)-1,0,-1):
            if m % n_cd[i] == 0:
                gcd = n_cd[i]; break

    m = m // gcd; n = n // gcd
    lcm = m*n*gcd
    return [gcd, lcm]

n = 14
m= 32
print(solution(n,m))

'''
def gcdlcm(a, b):
    c, d = max(a, b), min(a, b)
    t = 1
    while t > 0:
        t = c % d 큰수에서 작은수를 나눈 나머지
        c, d = d, t c=d, d=t
    answer = [c, int(a*b/c)]

    return answer'''

# 14, 32
# 32 % 14 = 4
# 14 % 4 = 2
# 4 % 2 = 0
# answer = c=2, 14*32/2
# //최대공약수 최소공배수를 구하는 유클리드 호제법..