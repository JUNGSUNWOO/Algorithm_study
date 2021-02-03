def solution(n, arr1, arr2):
    ans = []
    for i in range(len(arr1)):
        ans.append(format(arr1[i] | arr2[i],'0'+str(n)+'b'))
        # ans.append(bin(arr1[i]) | bin(arr2[i]))
    for i in range(len(ans)):
        ans[i] = ans[i].replace("1", "#")
        ans[i] = ans[i].replace("0", " ")
    return ans
n = 5
arr1 = [9, 20, 28, 18, 11]
arr2 = [30, 1, 21, 17, 28]
print(solution(n,arr1,arr2))