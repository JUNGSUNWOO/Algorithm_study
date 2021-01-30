# def solution(s, n):
#     new = list(map(lambda i:chr(ord(i)+n),s))
#     answer = ''.join(new)
#     return answer

def solution(s,n):
    new_list = []
    for i in s:
        if ord(i) == 32:
            new_i = 32
            new_list.append(chr(new_i))
        else :
            new_i = ord(i) + n
            if ord(i) <= 90 and new_i > 90:
                new_i = new_i - 90 + 64
            elif new_i > 122:
                new_i = new_i - 122 + 96

            new_list.append(chr(new_i))

    return ''.join(new_list)

s = "a bCD"
n = 2
print(solution(s,n))

#A-Z 65-90 a-z 97-122

'''def caesar(s, n):
    s = list(s)
    for i in range(len(s)):
        if s[i].isupper():
            s[i]=chr((ord(s[i])-ord('A')+ n)%26+ord('A'))
        elif s[i].islower():
            s[i]=chr((ord(s[i])-ord('a')+ n)%26+ord('a'))

    return "".join(s)'''