arr= [3,2,6]
divisior = 10

def solution(arr, divisor):
    answer = []
    for i in arr:
        if i % divisor == 0:
            answer.append(i)
    answer.sort()
    if len(answer) == 0:
        answer = -1
    return answer


res = solution(arr, divisior)
print(res)

'''
def solution(arr, divisor): return sorted([n for n in arr if n%divisor == 0]) or [-1]
'''