dr = [-1,1,0,0]
dc = [0,0,-1,1]

def BFS(r,c):
    q = [[r,c]]
    visited[r][c] = 1
    nowWolf, nowSheep = 0,0
    if madang[r][c] == 'v':
        nowWolf += 1
    elif madang[r][c] == 'o':
        nowSheep += 1

    while q:
        cr,cc = q.pop(0)
        for i in range(4):
            nr = cr + dr[i]
            nc = cc + dc[i]
            if 0 <= nr < R and 0 <= nc < C and visited[nr][nc] == 0:
                if madang[nr][nc] != '#':
                    visited[nr][nc] = 1
                    q.append([nr,nc])
                if madang[nr][nc] == "v":
                    nowWolf += 1
                elif madang[nr][nc] == "o":
                    nowSheep += 1
    if nowSheep > nowWolf:
        nowWolf = 0
    else:
        nowSheep = 0
    return [nowWolf,nowSheep]

R,C = map(int,input().split())

madang = [list(input()) for _ in range(R)]
visited = [[0] * C for _ in range(R)]

wolf = 0
sheep = 0
for i in range(R):
    for j in range(C):
        if madang[i][j] != '#' and visited[i][j] == 0:
            w,s = BFS(i,j)
            wolf += w
            sheep += s
print(sheep,wolf)