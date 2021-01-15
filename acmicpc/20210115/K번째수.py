array = [1,5,2,6,3,7,4]
commands= [[2, 5, 3], [4, 4, 1], [1, 7, 3]]


def solution(array, commands):
    answer = []
    for (start, end, sel) in commands:
        new_array = array[start-1:end]
        new_array.sort()
        answer.append(new_array[sel-1])
    return answer

res = solution(array, commands)
print(res)

'''
def solution(array, commands):
    return list(map(lambda x:sorted(array[x[0]-1:x[1]])[x[2]-1], commands))
'''

#map? lambda x:? 공부해야 할 듯