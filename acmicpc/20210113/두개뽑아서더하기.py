numbers = [2,1,3,4,1]

def solution(numbers):
    numbers.sort()

    max = numbers[-1]
    min = numbers[0]
    min_hat = numbers[1]
    max_hat = numbers[-2]

    table = make_table(max,max_hat,min,min_hat)

    answer = []

    for i in range(0, len(numbers)-1):
        for j in range(i+1, len(numbers)):
            table[numbers[i]+numbers[j]] = True
    for key, value in table.items():
        if value == True:
            answer.append(key)
    return answer

def make_table(max,max_hat, min,min_hat):
    biggest = max+max_hat
    smallest = min+min_hat
    new_dict = {}
    for i in range(smallest, biggest+1):
        new_dict[i] = False
    return new_dict

ans = solution(numbers)

print(ans)


'''
다른사람 풀이

def solution(numbers):
    answer = []
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            answer.append(numbers[i] + numbers[j])
    return sorted(list(set(answer)))
'''