n,k,p = map(int,input().split())

if n > 0:
    rankings = list(map(int,input().split()))

    now = 1
    same_cnt = 0
    for i in range(n):
        if k < rankings[i]:
            now += 1
        elif k == rankings[i]:
            same_cnt += 1
        else:
            break

    print(now if now + same_cnt < p+1 else -1)
else:
    print(1)