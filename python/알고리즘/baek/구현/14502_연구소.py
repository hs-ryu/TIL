# 시간초과.. 그럴거 같긴함.
# 재귀가 너무 많이 돈다. 어떻게 줄일 수 있지?
from collections import deque

dr = [-1,1,0,0]
dc = [0,0,-1,1]
def DFS():
    temp_industry = [industry[i][:] for i in range(n)]
    q = deque(birus[:])
    visited = [[0] * m for _ in range(n)]
    while q:
        cr,cc = q.popleft()
        visited[cr][cc] = 1
        for i in range(4):
            nr = cr + dr[i]
            nc = cc + dc[i]
            if 0 <= nr < n and 0 <= nc < m and visited[nr][nc] == 0 and temp_industry[nr][nc] == 0:
                visited[nr][nc] = 1
                temp_industry[nr][nc] = 2
                q.append([nr,nc])
    
    total = 0
    for i in range(n):
        for j in range(m):
            if temp_industry[i][j] == 0:
                total += 1
    return total


def act(wallcnt):
    if wallcnt == 3:
        global total_possible_cnt
        total = DFS()
        total_possible_cnt = max(total,total_possible_cnt)
        return

    for i in range(n):
        for j in range(m):
            if industry[i][j] == 0:
                industry[i][j] = 1
                act(wallcnt + 1)
                industry[i][j] = 0
    


n,m = map(int,input().split())
industry = [list(map(int,input().split())) for _ in range(n)]

birus = []
for i in range(n):
    for j in range(m):
        if industry[i][j] == 2:
            birus.append([i,j])

total_possible_cnt = 0

act(0)

print(total_possible_cnt)



