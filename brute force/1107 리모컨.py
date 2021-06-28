n = int(input())
m = int(input())
out = []
if m>0:
    out = list(map(int, input().split()))
mini = max(len(str(n)), abs(100000-n))
digit = len(str(n))
theNum = 0
ans = 1000000

if n == 100:
    print(0)
else:
    for i in range(1000001):
        temp = str(i)
        isOut = False
        for t in temp:
            if int(t) in out:
                isOut = True
                break
        if isOut == False:
            digit = len(temp)
            if i==100:
                digit = 0
            mini = abs(n-i)
        else:
            mini = abs(100-n) 
            digit= 0
            
        if ans>mini+digit:
            ans = mini+digit
            print(temp)
    print(ans)
            
