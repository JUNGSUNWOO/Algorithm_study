'''
번호판 배열이 존재
for i in numbers동안 i에 해당하는 번호판에 손가락을 위치
answer에 i지나갈때마다 LorR기록
2,4,8,0인 경우의 수에서
default는 더 가까운 손가락 거리가 같으면 왼손잡이냐 오른손잡이냐에 따라 달라짐

'''


def solution(numbers, hand):
    answer = ''
    hand_point = [[0]*4, [0]*4,[0]*4]
    hand_point[0][3] = 1; hand_point[2][3] = 2

    for i in numbers :
        if i in [1,4,7]:
            if i == 1:
                answer += 'L'
                init_point(hand_point,1)
                hand_point[0][0] = 1
            if i == 4:
                answer += 'L'
                init_point(hand_point,1)
                hand_point[0][1] = 1
            if i == 7:
                answer += 'L'
                init_point(hand_point,1)
                hand_point[0][2] = 1
        elif i in [3,6,9]:
            if i == 3:
                answer += 'R'
                init_point(hand_point,2)
                hand_point[2][0] = 2
            if i == 6:
                answer += 'R'
                init_point(hand_point,2)
                hand_point[2][1] = 2
            if i == 9:
                answer += 'R'
                init_point(hand_point,2)
                hand_point[2][2] = 2
        elif i in [2,5,8,0]:
            [left] = find_point(hand_point, 1)
            [right] = find_point(hand_point, 2)
            if i == 2:
                point = [1,0]

                if length(left, point) < length(right,point) : answer +='L'; init_point(hand_point,1);hand_point[1][0] = 1
                elif length(left, point) == length(right,point) :
                    if hand == "right" : answer +='R'; init_point(hand_point,2);hand_point[1][0] = 2
                    else: answer+='L'; init_point(hand_point,1);hand_point[1][0] = 1
                else: answer+='R'; init_point(hand_point,2);hand_point[1][0] = 2
            if i == 5:
                point = [1,1]
                if length(left, point) < length(right,point) : answer +='L'; init_point(hand_point,1);hand_point[1][1] = 1
                elif length(left, point) == length(right,point) :
                    if hand == "right" : answer +='R'; init_point(hand_point,2);hand_point[1][1] = 2
                    else: answer+='L'; init_point(hand_point,1);hand_point[1][1] = 1
                else: answer+='R'; init_point(hand_point,2);hand_point[1][1] = 2
            if i == 8:
                point = [1,2]
                if length(left, point) < length(right,point) : answer +='L'; init_point(hand_point,1);hand_point[1][2] = 1
                elif length(left, point) == length(right,point) :
                    if hand == "right" : answer +='R'; init_point(hand_point,2);hand_point[1][2] = 2
                    else: answer+='L'; init_point(hand_point,1);hand_point[1][2] = 1
                else: answer+='R'; init_point(hand_point,2);hand_point[1][2] = 2
            if i == 0:
                point = [1,3]
                if length(left, point) < length(right,point) : answer +='L'; init_point(hand_point,1);hand_point[1][3] = 1
                elif length(left, point) == length(right,point) :
                    if hand == "right" : answer +='R'; init_point(hand_point,2);hand_point[1][3] = 2
                    else: answer+='L'; init_point(hand_point,1);hand_point[1][3] = 1
                else: answer+='R'; init_point(hand_point,2);hand_point[1][3] = 2

    return answer

def init_point(point, n):
    [[i,j]] = find_point(point, n)
    point[i][j] = 0

def find_point(point, n):
    return [[i,j] for i in range(len(point)) for j in range(len(point[i])) if point[i][j]==n]

def length(a,b):
    return abs(b[0] - a[0]) + abs(b[1]-a[1])

numbers = 	[1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]
hands = "right"

#"LRLLLRLLRRL"
print(solution(numbers, hands))