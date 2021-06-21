e, s, m = list(map(int, input().split()))
ans = 0
ie = 0
ss = 0
im = 0
print(e, s, m)
while 1:
    print(ie, ss, im)
    if ie==e and ss==s and im==m:
        print(ans)
        break
    ans += 1
    if ie>=15:
        ie = 1
    else:
        ie += 1
    
    if ss>=28:
        ss = 1
    else:
        ss += 1
    
    if im>=19:
        im = 1
    else:
        im += 1