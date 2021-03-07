n, k = tuple(map(int, input().split()))
aa = list(map(int, input().split()))
robots = [0 for _ in range(n)]
step = 0
zeroCount = 0


while(1):
    # 1. 벨트 회전 (내구도만 회전)
    last = aa[n*2-1]
    for i in range(n*2-1, -1, -1):
        if i == 0:
            aa[i] = last
            robots[0] = 0
        else:
            aa[i] = aa[i-1]
        if 0<i<= n-1:
            robots[i] = robots[i-1]

    
    print("just updates: ", aa)

    robots[n-1] = 0
    # 2. 로봇이 갈 수 있는 자리인지 확인
    for i in range(n-1, -1, -1):
        if robots[i] == 1:
            if aa[i+1]>0 and robots[i+1]==0:
                robots[i] = 0
                robots[i+1] = 1
                aa[i+1] = aa[i+1]-1
                if aa[i+1]==0:
                    zeroCount = zeroCount +1
    

    # 3. 맨 처음에 로봇 올릴수 있으면 올린다
    if aa[0]>0 and robots[0]==0:
        robots[0] = 1
        aa[0] = aa[0]-1
        if aa[0]==0:
            zeroCount = zeroCount +1

    # 4. 단계 갱신
    step = step + 1

    # 5. zeroCount > k ?
    print("aa: ", aa)
    print("robots: ", robots)
    print("zeroCount: ", zeroCount)

    if zeroCount >= k:
        print("step: ", step)
        break
