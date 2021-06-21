n = int(input())
result = [[1] * n for _ in range(n)]
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
z = 2
cnt = n-1
x, y = 0, 0
idx = 0
while idx < (n * 2 - 1):
    for delta in range(len(dx)):
        for _ in range(cnt):
            x += dx[delta]
            y += dy[delta]
            result[x][y] = z
            z += 1
        idx += 1
        if idx == (n * 2 - 1):
            break
        if idx > 2 and idx % 2:
            cnt -= 1
for i in result:
    print(*i)