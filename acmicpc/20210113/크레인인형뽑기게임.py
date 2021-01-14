board, moves = [[0, 0, 0, 0, 0], [0, 0, 1, 0, 3], [0, 2, 5, 0, 1], [4, 2, 4, 4, 2], [3, 5, 1, 3, 1]], [1, 5, 3, 5, 1, 2, 1, 4]

def print_board(board):
    for i in range(len(board)):
        for j in range(len(board)):
            print(board[i][j], end=' ')
        print("\n")

def solution(board, moves):
    stack = []
    answer = 0
    for i in moves:
        i = i - 1
        for j in range(len(board)):
            if board[j][i] > 0:
                stack.append(board[j][i])
                board[j][i] = 0
                if stack[-1:] == stack[-2:-1]:
                    del stack[-2:]
                    answer += 2
                break

    return answer

def anipang(stack):
    answer = 0
    if len(stack) < 2: pass
    elif stack[-2] == stack[-1]:
        del stack[-2:]
        answer +=2

    return answer

ans = solution(board, moves)
print(ans)
