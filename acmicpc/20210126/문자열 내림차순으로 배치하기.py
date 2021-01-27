s = "Zbcdefg"
def solution(s):
    return "".join(sorted(s, reverse=True))
print(solution(s))

'''
def solution(s):
    return ''.join(sorted(s, reverse=True))'''