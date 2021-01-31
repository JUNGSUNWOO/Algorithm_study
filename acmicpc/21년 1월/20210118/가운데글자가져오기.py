s = 'wefr'

def solution(s):

    return s[(len(s)-1)//2:len(s)//2+1]
    # if len(s) % 2 == 0:
    #     answer = s[len(s)//2-1:len(s)//2+1]
    # else :
    #     answer = s[len(s)//2]
    # return answer

res = solution(s)
print(res)

'''
def string_middle(str):
    # 함수를 완성하세요

    return str[(len(str)-1)//2:len(str)//2+1]

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(string_middle("power"))
'''