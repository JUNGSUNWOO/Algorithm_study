def solution(s):
    new_s = []
    for i in s:
        if i == " ":
            c = 0
            new_s.append(i)
        else :
            print(c)
            if c % 2 ==0:
                new_s.append(i.uppeer())
            else:
                new_s.append(i.lower())
            c += 1
    print(new_s)
    return ''.join(new_s)

s = "  Hello   eVeryone 123   "
print(solution(s))


'''
def toWeirdCase(s):
    return " ".join(map(lambda x: "".join([a.lower() if i % 2 else a.upper() for i, a in enumerate(x)]), s.split(" ")))'''