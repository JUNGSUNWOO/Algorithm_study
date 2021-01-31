strings = ["sun", "bed", "car"]
n = 2
def solution(strings, n):
    strings.sort()
    strings = sorted(strings, key = lambda str:str[n])
    answer = strings
    return answer

res = solution(strings, n)
print(res)

'''
def strange_sort(strings, n):
    return sorted(strings, key=lambda x: x[n])'''