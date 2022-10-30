def makeLine(cnt, x, y):
    global answer
    if cnt >= answer:
        return
    
    for i in range(n):
        check = i
        for j in range(h):
            if arr[j][check]:
                check += 1
            elif check > 0 and arr[j][check-1]:
                check -= 1
        if check != i:
            break
    else:
        answer = min(answer, cnt)
        return
    
    if cnt == 3:
        return

    for i in range(x,h):
        k = y if i == x else 0
        for j in range(k, n-1):
            if arr[i][j] == 0:
                arr[i][j] = 1
                makeLine(cnt+1,i,j+2)
                arr[i][j] = 0


n,m,h = map(int,input().split())

arr = [[0] * n for _ in range(h)]

for _ in range(m):
    a,b = map(int,input().split())
    # 가로선 왼쪽 기준 1로 그려주기.
    arr[a-1][b-1] = 1

answer = 4
makeLine(0,0,0) 
print(answer if answer <= 3 else -1)