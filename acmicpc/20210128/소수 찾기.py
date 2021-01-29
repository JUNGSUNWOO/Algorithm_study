# def solution(n):
#     answer = 1
#     for i in range(3,n+1):
#         tmp = True
#         for j in range(2, i):
#             if i % j == 0:
#                 tmp = False
#                 break
#         if tmp == True :
#             answer +=1
#     return answer
#
def solution(n):
    if n <=1 : return
    array = [True]*(n+1)
    array[0], array[1] = False, False
    for i in range(2, int(n**0.5)+1):
        if array[i] :
            for j in range(i+i, n+1, i):
                array[j] = False
    print(array)
    return array.count(True)
    # return answer
n = 10
print(solution(n))

#에라토스테네스의 체에 대한 이해를 한 풀이
#2-n+1까지의 집합을 만듬
#for 문으로 2-n+1까지 한바퀴 돌면서
#i 가 num에 도달하면 num에서 차집합으로 2*i 부터 n+1까지 i++만큼을 빼준다
'''
def solution(n):
    num=set(range(2,n+1))

    for i in range(2,n+1):
        if i in num:
            num-=set(range(2*i,n+1,i))
    return len(num)
'''