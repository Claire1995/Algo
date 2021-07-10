from collections import deque

n, k = list(map(int, input().split()))

def bfs(cur, time):
    visited = [0 for _ in range(100001)]
    if cur == k:
        print(time)
        return
    dd = deque()
    dd.append([cur, time])

    while dd:
        temp = dd.popleft()
        print(temp)
        cur = temp[0]
        time = temp[1]
        visited[cur] = 1

        if cur-1==k or cur+1==k or cur*2==k:
            print(time+1)
            return
        if cur-1 >=0 and cur-1<=100000 and visited[cur-1]==0:
            dd.append([cur-1, time+1])
        if cur+1>=0 and cur+1<=100000 and visited[cur+1]==0:
            dd.append([cur+1, time+1])
        if cur*2>=0 and cur*2<=100000 and visited[cur*2]==0:
            dd.append([cur*2, time+1])
    print(time)

bfs(n, 0)