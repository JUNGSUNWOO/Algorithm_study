def solution(arr):
    print(min(arr))
    arr.remove(min(arr))
    if arr == []:
        return [-1]
    return arr

arr=[10,3,2,1,1,1]
# print(solution(arr))
arr2 = [10]


def rm_small(mylist):
    return [i for i in mylist if i > min(mylist)] or [-1]

print(rm_small(arr2))
print(solution(arr))