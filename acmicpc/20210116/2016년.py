
def solution(a, b):
    month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    day = ["MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"]
    tmp =0
    for i in range(a-1):
        tmp += month[i]
    tmp += b
    answer = tmp % 7 - 4
    return day[answer]

solution(5, 24)

'''
def getDayName(a,b):
    months = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    days = ['FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED', 'THU']
    return days[(sum(months[:a-1])+b-1)%7]'''