from _collections import deque

n = int(input())
a, b = map(int, input().split()) # input -> split -> int
m = int(input())
relation = [[0 for i in range(101)] for j in range(101)] # for문으로 이중리스트 선언
for _ in range(m):
    x, y = map(int, input().split())
    relation[x][y] = 1
    relation[y][x] = 1

visit = [0 for i in range(101)] #노드의 방문 - > 이중맵 방문 visit도 이중맵

def dfs(a, b):
    st = deque()                                            #1. deque생성                          
    st.append(a)                                            #2. root 삽입
    visit[a] = 1                                            #3. root의 방문여부 
    while st:                                               #4. deque가 빌때까지 반복
        temp = st.popleft()                                 #5. 하나 뽑는다
        for i in range(0, len(visit)):                      #6. 다음 단계 후보들 : 동서남북 / 관계노드 등 
            if relation[temp][i] == 1 and visit[i]==0:      #7. 다음 단계 조건 - "방문하지 않은 곳"
                visit[i] = visit[temp]+1                    #8. 방문 표시 및 단계 카운트 : visit 덮어 씌우기 / count 하기
                st.append(i)                                #9. 후보 삽입

dfs(a, b)                                                   #10. dfs 호출 : 모든 노드를 다 방문 / 한 노드의 조건만 한다                                                     
print(visit[b]-1 if visit[b] != 0 or visit[b] != 1 else -1)