from _collections import deque

field = [list(input()) for _ in range(12)]
dx, dy = [0, 1, 0, -1], [-1, 0, 1, 0]
#dx, dy = [1, 0, -1, 0], [0, -1, 0, 1]
visited = [[0 for _ in range(6)] for _ in range(12)]
def bfs(x, y):
    st = deque()
    st.append([x, y])
    visited[x][y] = 1
    color = field[x][y]
    print(color)
    localCnt = 1
    spotsForUpdate = [[x, y]]

    while st:
        temp = st.popleft()
        x = temp[0]
        y = temp[1]
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            print(nx, ny)
            if nx>=0 and nx<12 and ny>=0 and ny<6: 
                if visited[nx][ny] == 0:
                    if field[nx][ny] == color:
                        visited[nx][ny] =  1
                        st.append([nx, ny])
                        spotsForUpdate.append([nx, ny])
                        localCnt += 1
    if localCnt >= 4:
        for ix, iy in spotsForUpdate:
            field[ix][iy] = '.'
        print(True)
        return True
    else:
        print(False)
        return False

def forUpdate(x, y):
    while y>=0 and y<6 and x>=0 and x<11 and field[x][y] != '.' and field[x+1][y] == '.':
        field[x][y], field[x+1][y] = field[x+1][y], field[x][y]
        x = x+1

cascadeList = [True]
result = 0  
while True in cascadeList:
    print(cascadeList)
    result += 1
    visited = [[0 for _ in range(6)] for _ in range(12)]
    cascadeList.clear()
    for x in range(12):
        for y in range(6):
            if visited[x][y] == 0 and field[x][y] != '.':
                print('start bfs')
                cascadeList.append(bfs(x, y))
    #맵갱신
    for x in range(11, -1, -1):
        for y in range(6):
            forUpdate(x, y)
    print(field)
print(result-1)