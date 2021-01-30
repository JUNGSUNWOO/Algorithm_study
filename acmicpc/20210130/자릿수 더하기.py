def solution(n):
    sum = 0
    for i in str(n):
        sum += int(i)
    return sum

n=123
print(solution(n))

'''
def sum_digit(number):
    return sum([int(i) for i in str(number)])'''

'''
def sum_digit(number):
    if number < 10:
        return number;
    return (number % 10) + sum_digit(number // 10)'''