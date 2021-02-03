def solution(num):
    print(num, solution.count)

    if solution.count > 500: return -1
    if num == 1 : return solution.count
    if num % 2 ==0: solution.count+=1; return solution(num//2)
    if num % 2 != 0:solution.count+=1;return solution(num*3+1)
    return solution(num)

solution.count = 0 #python에서 static variable사용하기

num = 6
print(solution(num))

'''
def collatz(num):
    for i in range(500):
        num = num / 2 if num % 2 == 0 else num*3 + 1
        if num == 1:
            return i + 1
    return -1'''