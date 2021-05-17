class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        
        m = len(board)
        n = len(board[0])
        dx = [-1, 0, 1, -1, 1, -1, 0, 1]
        dy = [-1, -1, -1, 0, 0, 1, 1, 1]
        newB = [[2 for _ in range(n)] for _ in range(m)]
        for y in range(m):
            temp = []
            for x in range(n):
                print(y)
                print(x)
                cur = board[y][x]
                alive = 0
                for i in range(8):
                    ny = y+dy[i]
                    nx = x+dx[i]
                    if 0<=ny<m and 0<=nx<n:
                        if board[ny][nx] == 1:
                            alive += 1
                            
                if board[y][x] == 0 and alive == 3:
                    newB[y][x] = 1
                else:
                    newB[y][x] = 0
                
                if board[y][x] == 1:
                    if alive<2:
                        newB[y][x] = 0
                    elif 2<=alive<4:
                        newB[y][x] = 1
                    else:
                        newB[y][x] = 0
            
        return print(newB)

Solution.gameOfLife(0, [[0,1,0],[0,0,1],[1,1,1],[0,0,0]])
                
                