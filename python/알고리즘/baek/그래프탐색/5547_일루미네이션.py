from sys import stdin
input = stdin.readline

dr_odd = [-1, -1, 0, 1, 1, 0]
dc_odd = [-1, 0, 1, 0, -1, -1]
dr_even = [-1, -1, 0, 1, 1, 0]
dc_even = [0, 1, 1, 1, 0, -1]


def outside(r, c):
    q = [[r, c]]
    while q:
        cr, cc = q.pop(0)
        for i in range(6):
            if cr % 2:
                nr = cr + dr_odd[i]
                nc = cc + dc_odd[i]
            else:
                nr = cr + dr_even[i]
                nc = cc + dc_even[i]
            if 0 <= nr < h and 0 <= nc < w and home[nr][nc] == 0 and visited[nr][nc] == 0:
                visited[nr][nc] = 1
                q.append([nr, nc])

def calc(r,c):
    global result
    q = [[r,c]]
    visited[r][c] = 1
    while q:
        cr,cc = q.pop(0)
        for i in range(6):
            if cr % 2:
                nr = cr + dr_odd[i]
                nc = cc + dc_odd[i]
            else:
                nr = cr + dr_even[i]
                nc = cc + dc_even[i]
            if 0 <= nr < h and 0 <= nc < w and home[nr][nc] == 1:
                if visited[nr][nc] == 0:
                    visited[nr][nc] = 1
                    q.append([nr,nc])
            else:
                result += 1


w, h = map(int, input().split())

home = [list(map(int, input().split())) for _ in range(h)]
visited = [[0 for _ in range(w)] for _ in range(h)]
# 테두리 검사
for i in range(h):
    for j in range(w):
        if (i == 0 or i == h-1 or j == 0 or j == w-1) and home[i][j] == 0 and visited[i][j] == 0:
            visited[i][j] = 1
            outside(i, j)
# 내부에 있는거 색칠 해주기.
for i in range(h):
    for j in range(w):
        if visited[i][j] == 0 and home[i][j] == 0:
            home[i][j] = 1

visited = [[0 for _ in range(w)] for _ in range(h)]
result = 0
for i in range(h):
    for j in range(w):
        if home[i][j] and visited[i][j] == 0:
            calc(i,j)
print(result)