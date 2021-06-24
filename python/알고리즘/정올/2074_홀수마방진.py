n = int(input())

arr = [[0] * n for _ in range(n)]
r = 0
c = n // 2
arr[r][c] = 1

cnt = 1
while cnt < n*n:
    if cnt % n == 0:
        r += 1
        if r >= n:
            r = 0
    else:
        r -= 1
        c -= 1
        if r < 0:
            r = n-1
        if c < 0:
            c = n-1
    cnt += 1
    arr[r][c] = cnt
for i in range(n):
    print(*arr[i])