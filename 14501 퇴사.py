n = int(input())
summary = [-1 for _ in range(n+1)]
tt = [0]
pp = [0]
for _ in range(n):
    t, p = map(int, input().split())
    tt.append(t)
    pp.append(p)
print("tt: ", tt)
print("pp: ", pp)
def bestAt(day):
    print("day: ", day)
    if summary[day] == -1:
        for next in range(day+tt[day], n+1):
            print("for문")
            if summary[next] == -1:
                bestAt(next)
        if n-day+1>=tt[day]: #상담 가능
            print("상담가능")
            print(day)
            print(n-day)
            print(tt[day])
            print("for max: ", summary[day+tt[day]: n+1])
            temp = summary[day+tt[day]: n+1]
            if not temp:
                summary[day] = pp[day]
            else: 
                summary[day] = pp[day] + max(summary[day+tt[day]: n+1])  
            print("Result summary: ", summary)
        else:
            print("상담불가")
            summary[day] = 0 #상담 불가

for i in range(1, n+1):
    bestAt(i)
print("summary: ", summary)
print(max(summary))