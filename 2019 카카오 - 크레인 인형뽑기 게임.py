from _collections import deque
def solution(board, moves):
    pocket = deque()
    n = len(board)
    result = 0
    
    for y in moves:
        useY = False
        for i in range(n):
            if useY == True:
                break
            if board[i][y-1] != 0:
                doll = board[i][y-1]
                board[i][y-1] = 0
                if pocket:
                    lastDoll = pocket.pop()
                    if lastDoll == doll:
                        result = result +2
                    else:
                        pocket.append(lastDoll)
                        pocket.append(doll)
                else:
                    pocket.append(doll)
                useY = True
    return result

