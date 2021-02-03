def solution(arr1, arr2):
    print(arr1, arr1[0])

    answer = []
    for cnt in range(len(arr1)):
        list = []
        for i, j in zip(arr1[cnt], arr2[cnt]):
            list.append(i+j)
        answer.append(list)
    return answer
arr1 = [[1,2,3]]
arr2 = [[2,3,4]]
print(solution(arr1,arr2))

'''
def sumMatrix(A,B):
    answer = [[c + d for c, d in zip(a, b)] for a, b in zip(A,B)]
    return answer'''