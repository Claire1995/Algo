import copy

########## 초기 셋팅
dd = [[0, 0], [-1, 0], [1, 0], [0, -1], [0, 1]]
n, m ,k = map(int, input().split())
sea = [list(map(int, input().split())) for _ in range(n)] # 상어 위치 지도
sharks = dict() # 상어 별 현재 위치
deadSharks = []
smell = [[[0, 0] for _ in range(n)] for _ in range(n)] # 냄새 지도
for i in range(n):
    for j in range(n):
        if sea[i][j] != 0:
            smell[i][j] = [sea[i][j], 4]
            sharks[sea[i][j]] = [i, j]
direction = list() # 초기 상어 방향
direction.append(0)
for i in list(map(int, input().split())):
    direction.append(i)
preference = dict() # 방향우선순위 = 현재방향: 우선순위
for i in range(1, m+1):
    temp = []
    for _ in range(4):
        temp.append(list(map(int, input().split())))
    preference[i] = temp

def move(shark, curX, curY):
    global smell, copySea, copySmell, sharks, deadSharks

    # 1. 다음 칸 위치 계산
    newXY = list()
    for idx in preference[shark][direction[shark]-1]:
        newX, newY = curX+dd[idx][1], curY+dd[idx][0]
        if newX>=0 and newX<n and newY>=0 and newY<n:
            newXY.append((newY, newX, idx))

    newX, newY = curX, curY
    isChosen = False
    for y, x, idx in newXY:
        if smell[y][x][1]==0: # 냄새 없는 칸
            direction[shark] = idx    # 현재 방향 갱신
            isChosen = True
            newX, newY = x, y
            break
        
    if isChosen == False:
        for y, x, idx in newXY:
            if smell[y][x][0]==shark: # 자기 냄새 칸
                direction[shark] = idx    # 현재 방향 갱신
                newX, newY = x, y
                break

    # 2. 만난 상어가 있는지?
    otherShark = copySea[newY][newX]
    if otherShark==0 or otherShark>shark: #빈자리이거나 갱신되지 않은 옛날애
        copySea[newY][newX] = shark #그자리는 내자리닷
        copySea[curY][curX] = 0
        sharks[shark] = [newY, newX]
    elif otherShark<shark: #나보다 강한 상어인 경우 2<4
        copySea[curY][curX] = 0
        del sharks[shark] # 나는 쫓겨난다,, 1 2 3 
        deadSharks.append(shark)

def updateSmell():
    for i in range(n):
        for j in range(n):
            if copySmell[i][j][0]!=0:
                curSmell = copySmell[i][j][1]
                if curSmell==1:
                    copySmell[i][j][0] = 0
                copySmell[i][j][1] = curSmell-1
    
    print("shark: ", sharks)
    for shark in sharks:
        newY, newX = sharks[shark]
        copySmell[newY][newX][0] = shark
        copySmell[newY][newX][1] = 4

def checkRemains():
    for shark in sharks:
        if shark != 1:
            return True
    return False

############ 로직 시작
t = 1
while t<1001:
    copySea = copy.deepcopy(sea) # copy vs deepcopy !!
    copySmell = copy.deepcopy(smell)
    
    for shark in range(1, m+1):
        if shark in sharks:
            move(shark, sharks[shark][1], sharks[shark][0])
        else:
            continue

    updateSmell()

    if checkRemains()==False:
        break
    t += 1
    print("copySea: ", copySea)
    print("copySmell: ", copySmell)
    sea = copy.deepcopy(copySea)
    smell = copy.deepcopy(copySmell)

if t>1000:
    t = -1
print("final t: ", t)
