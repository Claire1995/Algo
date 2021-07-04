n, m = list(map(int, input().split()))
nodes = [[] for _ in range(n+1)]
answer = 0

for _ in range(m):
    n1, n2 = list(map(int, input().split()))
    nodes[n1].append(n2)
    nodes[n2].append(n1)

def dfs(cur, cnt, visited, s):
    print("cnt: ", cnt)
    global answer
    if cnt>=5:
        answer = 1
        return
    
    hasNext = False
    for next in nodes[cur]:
        if visited[next] == 0:
            hasNext = True
            visited[next] = 1
            dfs(next, cnt+1, visited, s+str(next))
            visited[next] = 0
            
    if hasNext == False:
        if cnt>=5:
            answer = 1
    return

for i in range(n):
    if answer == 1:
        print(answer)
        break
    visited = [0 for _ in range(n+1)]
    visited[i] = 1
    ans = dfs(i, 1, visited, str(i))
    
if answer == 0:
    print(answer)

