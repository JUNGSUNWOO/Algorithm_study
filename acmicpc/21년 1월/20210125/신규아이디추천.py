id = "z-+.^"
id2 = "...!@BaT#*..y.abcdefghijklm"
id3 = "=.="
id4 = "......b...."
id5 = "b........."

def solution(new_id):
    punctuation = "!#$%&'()*+,/:;<=>?@[\]^`{|}~"
    new_id = new_id.lower()
    for i in punctuation:
        new_id = new_id.replace(i, "")

    while(new_id.find("..") != -1):
        new_id = new_id.replace("..", ".")

    if len(new_id) >= 1:
        if new_id[0] == '.':
            new_id = new_id[1:]
    if len(new_id) >= 1:
        if new_id[-1] == ".":
            new_id = new_id[:-1]
    if len(new_id) == 0:
        new_id = "a"
    if len(new_id) >= 16:
        new_id = new_id[:15]
        if new_id[-1] == '.':
            new_id = new_id[:-1]

    if len(new_id) <= 2:
        new_id = new_id + new_id[-1] * 3
        new_id = new_id[:3]
    return new_id

# res = solution(id)
# print("res",res)
#
res2 = solution(id2)
print("res2",res2)

# res3 = solution(id3)
# print("res3",res3)
#
# res4 = solution(id4)
# print("res4", res4)

# res5 = solution(id5)
# print("res5", res5)

'''
import re

def solution(new_id):
    st = new_id
    st = st.lower()
    st = re.sub('[^a-z0-9\-_.]', '', st)
    st = re.sub('\.+', '.', st)
    st = re.sub('^[.]|[.]$', '', st)
    st = 'a' if len(st) == 0 else st[:15]
    st = re.sub('^[.]|[.]$', '', st)
    st = st if len(st) > 2 else st + "".join([st[-1] for i in range(3-len(st))])
    return st'''


#라이브러릴르 활용하는것..