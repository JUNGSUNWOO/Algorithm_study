def solution(x, n):
    if x == 0: return [x for i in range(n)]
    else: return [x + i for i in range(0,n*x,x)]

def number_generator(x, n):
    # 함수를 완성하세요
    return [i * x + x for i in range(n)]