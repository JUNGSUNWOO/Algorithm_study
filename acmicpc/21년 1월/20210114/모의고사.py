stu_1 = [1, 2, 3, 4, 5]
stu_2 = [2, 1, 2, 3, 2, 4, 2, 5]
stu_3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

answers = [1, 2, 3, 4, 5]
def solution(answers):
    answer = []
    i, s_1, s_2, s_3 = 0, 0, 0, 0
    res_1, res_2, res_3 = 0, 0, 0
    while i < len(answers):
        if answers[i] == stu_1[s_1]:
            res_1 += 1
        if answers[i] == stu_2[s_2]:
            res_2 += 1
        if answers[i] == stu_3[s_3]:
            res_3 += 1
        i += 1

        s_1 += 1
        if s_1 >= len(stu_1) :
            s_1 = 0
        s_2 += 1
        if s_2 >= len(stu_2) :
            s_2 = 0
        s_3 += 1
        if s_3 >= len(stu_3) :
            s_3 = 0
    list = [[1,res_1], [2,res_2], [3,res_3]]
    list.sort(key = lambda x:x[1])
    answer.append(list[-1][0])
    for j in range(len(list)-2, -1, -1):
        if list[j][1] != list[j+1][1]: break
        answer.append(list[j][0])
    answer.sort()

    return answer

res = solution(answers)
print(res)
'''다른사람 풀이
def solution(answers):
    pattern1 = [1,2,3,4,5]
    pattern2 = [2,1,2,3,2,4,2,5]
    pattern3 = [3,3,1,1,2,2,4,4,5,5]
    score = [0, 0, 0]
    result = []

    for idx, answer in enumerate(answers):
        if answer == pattern1[idx%len(pattern1)]:
            score[0] += 1
        if answer == pattern2[idx%len(pattern2)]:
            score[1] += 1
        if answer == pattern3[idx%len(pattern3)]:
            score[2] += 1

    for idx, s in enumerate(score):
        if s == max(score):
            result.append(idx+1)

    return result
'''