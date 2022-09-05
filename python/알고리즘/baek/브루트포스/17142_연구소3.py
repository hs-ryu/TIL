# 총 바이러스 -> m개 뽑아서 활성화 -> BFS 돌리면서 확인.
dr = [-1,1,0,0]
dc = [0,0,-1,1]

def BFS(q):
    visited = [[0] * n for _ in range(n)]
    for i in range(m):
        r,c,t = q[i]
        visited[r][c] = 1
    # 제일 멀리 퍼진 바이러스
    max_cnt = 0
    while q:
        cr,cc,ct = q.pop(0)
        for i in range(4):
            nr = cr + dr[i]
            nc = cc + dc[i]
            if 0<=nr<n and 0<=nc<n and visited[nr][nc] == 0 and lab[nr][nc] != 1:
                visited[nr][nc] = 1
                q.append([nr,nc,ct+1])
                max_cnt = max(max_cnt,ct+1)

    # 다 돌았는지 체크해야함.
    cnt = 0
    for i in range(n):
        for j in range(n):
            if visited[i][j] == 1:
                cnt += 1
    if cnt == total_cell_cnt:
        return [True, max_cnt]
    else:
        return [False, max_cnt]


def search(level, arr):
    if level == len(virus):
        if len(arr) == m:
            # 여기서 bfs 체크
            q = []
            for i in range(m):
                q.append(arr[i])
            flag, cnt = BFS(q)
            print(flag, cnt)

        return
    arr.append(virus[level])
    search(level+1, arr)
    arr.pop(-1)
    search(level+1, arr)
    




n,m =  map(int,input().split())

lab = []
for _ in range(n):
    lab.append(list(map(int,input().split())))

virus = []
# 총 퍼트려야하는 칸의 수
total_cell_cnt = n * n 
for i in range(n):
    for j in range(n):
        if lab[i][j] == 2:
            virus.append([i,j,0])
        if lab[i][j] == 1:
            total_cell_cnt -= 1
search(0,[])