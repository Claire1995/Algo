# 현재 위치를 청소한다.
# 현재 위치에서 현재 방향을 기준으로 왼쪽방향부터 차례대로 탐색을 진행한다.
# 왼쪽 방향에 아직 청소하지 않은 공간이 존재한다면, 그 방향으로 회전한 다음 한 칸을 전진하고 1번부터 진행한다.
# 왼쪽 방향에 청소할 공간이 없다면, 그 방향으로  회전하고 2번으로 돌아간다.
# 네 방향 모두 청소가 이미 되어있거나 벽인 경우에는, 바라보는 방향을 유지한 채로 한 칸 후진을 하고 2번으로 돌아간다.
# 네 방향 모두 청소가 이미 되어있거나 벽이면서, 뒤쪽 방향이 벽이라 후진도 할 수 없는 경우에는 작동을 멈춘다.

from collections import deque

n, m = list(map(int, input().split()))
r, c, d = list(map(int, input().split()))
room = [] #빈칸0 벽1 청소함2
count = 0
direction = [[3, 2, 1, 0], [0, 3, 2, 1], [1, 0, 3, 2], [2, 1, 0, 3]]
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]
bx = [0, -1, 0, 1]
by = [1, 0, -1, 0]

for i in range(n):
    room.append(list(map(int, input().split())))

def dfs(cell):
    global count
    q = deque()
    q.append(cell)

    while q:
        stucked = False
        temp = q.popleft()
        y = temp[0]
        x = temp[1]
        d = temp[2]
        
        if room[y][x] == 0:
            count = count + 1
            room[y][x] = 2 # 현재 위치를 청소한다.
        print("room[y][x]: ", room[y][x])

        # 현재 위치에서 현재 방향을 기준으로 왼쪽방향부터 차례대로 탐색을 진행한다.
        while 1 :
            cleaned = False
            for dd in direction[d]:
                nx = x+dx[dd]
                ny = y+dy[dd]
                if nx>=0 and nx<m and ny>=0 and ny<n:
                    if room[ny][nx] == 0: # 왼쪽 방향에 아직 청소하지 않은 공간이 존재한다면,
                        cleaned = True
                        q.append([ny, nx, dd])
                        print("왼쪽에 있음")
                        break
            if cleaned == True:
                break

            if cleaned == False: # 네 방향 모두 청소가 이미 되어있거나 벽인 경우에는
                nx = x+bx[d]
                ny = y+by[d]
                if nx<0 or nx>=m or ny<0 or ny>=n or room[ny][nx]==1: #후진도 못함
                    print("갇힘")
                    stucked = True
                    break
                else:
                    #후진
                    print("후진")
                    x = nx
                    y = ny

        if stucked == True:
            return count
            
                
print(room[r][c])
print(dfs([r, c, d]))
