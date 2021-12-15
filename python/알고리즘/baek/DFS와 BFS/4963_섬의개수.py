# 상하좌우, 좌상, 우상, 우하, 좌하
dr = [-1,1,0,0,-1,-1,1,1]
dc = [0,0,-1,1,-1,1,1,-1]

def BFS(r,c):
    q = [[r,c]]
    visited[r][c] = 1
    while q:
        cr, cc = q.pop()
        for i in range(8):
            nr = cr + dr[i]
            nc = cc + dc[i]
            if 0 <= nr < h and 0 <= nc < w:
                if jido[nr][nc] and not visited[nr][nc]:
                    visited[nr][nc] = 1
                    q.append([nr,nc])


w,h = map(int,input().split())
while w != 0 and h != 0:
    jido = [list(map(int,input().split())) for _ in range(h)]
    visited = [[0 for _ in range(w)] for _ in range(h)]

    result = 0
    for i in range(h):
        for j in range(w):
            if jido[i][j] and not visited[i][j]:
                BFS(i,j)
                result += 1
    print(result)
    # print(visited)
    w,h = map(int,input().split())
    