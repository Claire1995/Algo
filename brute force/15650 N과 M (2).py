n, m = list(map(int, input().split()))
arr = [True for i in range(n+1)]
answers = set()

def isDuplicated(ans):
    ans.sort()
    temp = ''
    for a in ans:
        temp += str(a)+' '
    temp = temp[:-1]
    if temp not in answers:
        print(temp)
        answers.add(temp)

def recurive(arr, ans):
    if len(ans) == m:
        isDuplicated(ans)
    else:
        for i in range(1, n+1):
            if arr[i] == False:
                continue
            arr[i] = False
            ans.append(i)
            recurive(arr, ans)
            ans.remove(i)
            arr[i] = True

for i in range(1, n+1):
    if arr[i] == False:
        continue
    arr[i] = False
    ans = [i]
    recurive(arr, ans)
    arr[i] = True