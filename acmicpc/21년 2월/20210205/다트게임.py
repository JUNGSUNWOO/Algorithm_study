import re

def solution(dartResult):
    num = re.findall('\d+', dartResult)
    str = re.findall('\D+', dartResult)
    score = [0] * 3
    for i in range(len(str)):
        if len(str[i]) != 2:
            str[i] = str[i] + '0'

    print(num, str)

    for i in range(len(num)):
        score[i] = int(num[i])
        if str[i][0] == "S":
            score[i] **= 1
        elif str[i][0] == "D":
            score[i] **= 2
        elif str[i][0] == "T":
            score[i] **= 3
        if str[i][1] == "*":
            score[i] *= 2
            if score[i-1]:
                score[i-1] *=2
        elif str[i][1] == "#":
            score[i] *= -1
    return sum(score)

dartResult = "1S2D*3T"
print(solution(dartResult))

'''
re 라이브러리 극한의 활용
import re


def solution(dartResult):
    bonus = {'S' : 1, 'D' : 2, 'T' : 3}
    option = {'' : 1, '*' : 2, '#' : -1}
    p = re.compile('(\d+)([SDT])([*#]?)')
    dart = p.findall(dartResult)
    for i in range(len(dart)):
        if dart[i][2] == '*' and i > 0:
            dart[i-1] *= 2
        dart[i] = int(dart[i][0]) ** bonus[dart[i][1]] * option[dart[i][2]]

    answer = sum(dart)
    return answer'''
