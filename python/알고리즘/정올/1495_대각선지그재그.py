n = int(input())

k = 0
cnt = 1

r = c = 0
arr = [[0] * n for _ in range(n)]
x = 0
dr = [1, -1]
dc = [-1, 1]
    # 위쪽 절반

for i in range(1,n+1):
    arr[r][c] = cnt
    
    for j in range(i):
        print(i,r,c)
        r = r + dr[x]
        c = c + dc[x]
        cnt += 1
        arr[r][c] = cnt
    
    if i % 2 == 0:
        if i == n:
            r += 1
        else:
            c += 1
        x = 0
    
    else:
        if i == n:
            c += 1
        else:
            r += 1
        x = 1
    
for i in range(n-1,-1,-1):
    arr[r][c] = cnt
    for j in range(i):
        r = r + dr[x]
        c = c + dc[x]
        cnt += 1
        arr[r][c] = cnt
    if i % 2 == 0:
        r += 1
        x = 0
    else:
        c += 1
        x = 1

for i in range(n):
    print(*arr[i])


    # 아래쪽 절반


