def solution(maps):
    dr = [-1,1,0,0]
    dc = [0,0,-1,1]
    def BFS(r,c):
        q = [[r,c]]
        visited = [[0] * len(maps[0]) for _ in range(len(maps))]
        visited[r][c] = 1
        find = False
        pr, pc = 0, 0
        while q:
            cr,cc = q.pop(0)
            for i in range(4):
                nr = cr + dr[i]
                nc = cc + dc[i]
                if 0<= nr < len(maps) and 0<=nc<len(maps[0]):
                    if maps[nr][nc] != "X" and visited[nr][nc] == 0:
                        visited[nr][nc] = visited[cr][cc] + 1
                        q.append([nr,nc])
                        if maps[nr][nc] == "L":
                            find = True
                            pr = nr
                            pc = nc
                            break
            if find:
                break
        return [pr,pc,visited[pr][pc]-1]
    
    def BFS2(r,c,l):
        q = [[r,c]]
        visited = [[0] * len(maps[0]) for _ in range(len(maps))]
        visited[r][c] = l
        find = False
        pr, pc = 0, 0
        while q:
            cr,cc = q.pop(0)
            for i in range(4):
                nr = cr + dr[i]
                nc = cc + dc[i]
                if 0<= nr < len(maps) and 0<=nc<len(maps[0]):
                    if maps[nr][nc] != "X" and visited[nr][nc] == 0:
                        visited[nr][nc] = visited[cr][cc] + 1
                        q.append([nr,nc])
                        if maps[nr][nc] == "E":
                            find = True
                            pr = nr
                            pc = nc
                            break
            if find:
                break
        return [pr,pc,visited[pr][pc]] if find else [-1,-1,-1]
                    
    r = 0
    c = 0
    find = False
    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if maps[i][j] == "S":
                r,c = i,j
                find = True
                break
        if find:
            break
    lr, lc, p = BFS(r,c)
    if p == -1:
        return -1
    gr, gc, answer = BFS2(lr,lc,p)
    
    return answer