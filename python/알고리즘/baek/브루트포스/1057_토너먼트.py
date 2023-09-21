n, kim, lim = map(int,input().split())

cnt = 1
while True:
    if abs(kim - lim) == 1 and kim // 2 != lim // 2:
        break

    if kim % 2:
        kim = kim // 2 + 1
    else:
        kim = kim // 2

    if lim % 2:
        lim = lim // 2 + 1
    else:
        lim = lim // 2
    cnt += 1
print(cnt)