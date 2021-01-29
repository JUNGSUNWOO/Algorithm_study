def solution(s):
    return int(s)

s = "-1234"
print(solution(s))

'''
def strToInt(str):
    result = 0

    for idx, number in enumerate(str[::-1]):
        if number == '-':
            result *= -1
        else:
            result += int(number) * (10 ** idx)

    return result'''