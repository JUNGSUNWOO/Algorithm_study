participant, completion = ["mislav", "stanko", "mislav", "ana"], ["stanko", "ana", "mislav"]
def solution(participant, completion):
    for comp in completion:
        if comp in participant:
            participant.remove(comp)
    answer = ''.join(participant)

    return answer

res = solution(participant,completion)
print(res)