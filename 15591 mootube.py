from _collections import deque

# input 셋팅
n, q = map(int, input().split())
relation = [[0 for _ in range(n+1)] for _ in range(n+1)]
history = [list() for _ in range(n+1)]

usadoList = list()
usado = list()
node = set()
for _ in range(n-1):
    x, y, z = map(int, input().split())
    usado.append(z)
    node.add(x)
    node.add(y)
    relation[y][x] = z
    relation[x][y] = z

#그래프 로직
def isLastNode(nx):
    for i in range(n+1):
        if relation[nx][i] != 0 and visited[nx][i] == 0:
            return False
    return True

def bfs(y, x, k):
    usadoHist = list()
    st = deque()
    st.append([y, x])
    visited[y][x] = 1
    visited[x][y] = 1
    usadoHist.append(relation[y][x])
    usadoList.append(relation[y][x])
    while st:
        temp = st.popleft()
        nx = temp[0]
        
        for i in range(n+1):
            if relation[i][nx] != 0 and relation[i][nx] >= k and visited[i][nx] == 0:
                ny = i
                st.append([ny, nx])
                visited[ny][nx] = 1
                visited[nx][ny] = 1
                usadoHist.append(relation[ny][nx])
                if isLastNode(ny):
                    # 현재가 마지막 노드일 때
                    usadoList.append(min(usadoHist))
                    usadoHist.pop()
                else :
                    # 현재가 마지막 노드 아닐 때
                    usadoList.append(relation[ny][nx])
    return (usadoList)


#메인 로직
resultList = list()
answerList = list()
for _ in range(q):
    visited = [[0 for _ in range(n+1)] for _ in range(n+1)]
    resultList.clear()
    k, v = map(int, input().split())

    if k > max(usado):
        answerList.append(0)
        continue
    elif history[v]:
        a = len([x for x in history[v] if x >= k])
        answerList.append(a)        
    else:
        for i in node:
            if relation[i][v] != 0 and relation[i][v] >= k and visited[i][v] == 0:
                usadoList.clear()
                result = bfs(i, v, k)
                history[v].extend(result) 
                for j in result:
                    if j >= k:
                        resultList.append(j)
        answerList.append(len(resultList))

for a in answerList:
    print(a)