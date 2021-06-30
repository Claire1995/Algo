n = int(input())
arr = [i for i in range(1, n+1)]
arrReverse = sorted(arr, reverse=True)

def nextPer(arr):
    i = len(arr)-1
    #   오름 차순이 되는 부분 중 가장 큰 수
    while i>0 and arr[i-1]>=arr[i]:
        i -= 1

    if i<=0:
        return False

    j = len(arr)-1
    while arr[i-1]>=arr[j]:
        j -= 1

    #   swa
    arr[i-1], arr[j] = arr[j], arr[i-1]

    j = len(arr)-1
    #   rearrange to 
    while i<j:
        arr[i], arr[j] = arr[j], arr[i]
        i += 1
        j -= 1
    print(arr)
    return True

temp = ''
for a in arr:
    temp += str(a)+' '
temp = temp[:-1]
print(temp)

while 1:
    if not nextPer(arr):
        break
    temp = ''
    for a in arr:
        temp += str(a)+' '
    temp = temp[:-1]
    print(temp)

