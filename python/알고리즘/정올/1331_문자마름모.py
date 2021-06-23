n = int(input())
k = 65
arr = [[' '] * (2*n - 1) for _ in range(2*n-1)]
r = -1
c = n
m = n
while m > 0:
    # 왼쪽 아래로
    for i in range(m):
        if k == 91:
            k = 65
        r += 1
        c -= 1
        arr[r][c] = chr(k)
        k += 1
    m -= 1
    # 오른쪽 아래로
    for i in range(m):
        if k == 91:
            k = 65
        r += 1
        c += 1
        arr[r][c] = chr(k)
        k += 1
    # 오른쪽 위로
    for i in range(m):
        if k == 91:
            k = 65
        r -= 1
        c += 1
        arr[r][c] = chr(k)
        k += 1
    m -= 1
    # 왼쪽 위
    for i in range(m):
        if k == 91:
            k = 65
        r -= 1
        c -= 1
        arr[r][c] = chr(k)
        k += 1
    r -= 1
    m += 1
for i in range(2*n-1):
    print(*arr[i])