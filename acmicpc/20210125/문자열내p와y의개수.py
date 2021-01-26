s = "pPoooyY"
def solution(s):
    answer = True
    s = s.lower()
    s_cnt = 0
    p_cnt = 0
    for i in s:
        if i == 'y':
            s_cnt+=1
        if i == 'p':
            p_cnt +=1
    if s_cnt == p_cnt:
        answer = True
    else :
        answer = False

    return answer

res = solution(s)
print(res)

'''
def numPY(s):
    # 함수를 완성하세요
    return s.lower().count('p') == s.lower().count('y')'''