s = "123456z"
def solution(s):
    num = "0123456789"
    answer = True
    if len(s) > 6 or len(s) < 4 or len(s) == 5 : answer = False
    else :
        for i in s :
            if i in num:
                answer = True
            else : answer = False; break

    return answer

res = solution(s)
print(res)

'''def alpha_string46(s):
    return s.isdigit() and len(s) in (4, 6)'''