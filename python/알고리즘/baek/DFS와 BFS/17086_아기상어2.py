
# 상, 우상, 우, 우하, 하, 좌하, 좌, 좌상.
dr = [-1, -1, 0, 1, 1, 1, 0, -1]
dc = [0, 1, 1, 1, 0, -1, -1, -1]

def check():
    visited = [[0] * m for _ in range(n)]
    for i in range(len(q)):
        r,c = q[i]
        visited[r][c] = 1
        area[r][c] = 0

    while q:
        cr,cc = q.pop(0)
        for i in range(8):
            nr = cr + dr[i]
            nc = cc + dc[i]
            if 0<=nr<n and 0<= nc < m and visited[nr][nc] == 0:
                q.append([nr,nc])
                visited[nr][nc] = 1
                area[nr][nc] = area[cr][cc] + 1


n,m = map(int,input().split())

area = [list(map(int,input().split())) for _ in range(n)]
# print(area)



q = []
for i in range(n):
    for j in range(m):
        if area[i][j]:
            q.append([i,j])

check()
# print(area)

result = 0
for i in range(n):
    for j in range(m):
        if area[i][j] > result:
            result = area[i][j]
print(result)