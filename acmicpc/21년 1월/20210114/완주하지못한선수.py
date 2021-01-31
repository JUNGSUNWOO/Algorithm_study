participant, completion = ["mislav", "stanko", "mislav", "ana"], ["stanko", "ana", "mislav"]

def solution(participant, completion):
    answer = ''
    par_table = part_table(participant)
    for i in completion:
        par_table[i] -= 1
    for key, value in par_table.items():
        if value != 0:
            answer += key
    return answer

def part_table(participant):
    participant_table = {}
    for i in participant:
        participant_table[i] = 0
    for i in participant:
        participant_table[i] += 1
    return participant_table


res = solution(participant,completion)
print(res)

'''
다른사람코드
import collections


def solution(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)
    return list(answer.keys())[0]'''