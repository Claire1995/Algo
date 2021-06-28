n, m = list(map(int, input().split()))
arr = [True for i in range(n+1)]

def recurive(arr, ans):
    if len(ans) == m+(m-1):
        print(ans)
    else:
        for i in range(1, n+1):
            if arr[i] == False:
                continue
            arr[i] = False
            recurive(arr, ans+' '+str(i))
            arr[i] = True

for i in range(1, n+1):
    if arr[i] == False:
        continue
    arr[i] = False
    recurive(arr, str(i))
    arr[i] = True