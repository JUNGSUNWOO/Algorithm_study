'''
문제 설명
정수 배열 numbers가 주어집니다. numbers에서 서로 다른 인덱스에 있는 두 개의 수를 뽑아 더해서 만들 수 있는 모든 수를 배열에 오름차순으로 담아 return 하도록 solution 함수를 완성해주세요.

제한사항
numbers의 길이는 2 이상 100 이하입니다.
numbers의 모든 수는 0 이상 100 이하입니다.

'''
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