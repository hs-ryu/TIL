# pypy만 통과! python3 60% 시간초과.
dr = [-1,1,0,0]
dc = [0,0,-1,1]

def check(r,c):
    q = [[r,c]]
    visited = [[0] * y for _ in range(x)]
    visited[r][c] = 1
    
    while q:
        cr,cc = q.pop(0)
        for i in range(4):
            nr = cr + dr[i]
            nc = cc + dc[i]
            if 0 <= nr < x and 0 <= nc < y and visited[nr][nc] == 0 and treasure_map[nr][nc] == "L":
                global max_length
                q.append([nr,nc])
                visited[nr][nc] = visited[cr][cc] + 1
                if visited[nr][nc] > max_length:
                    max_length = visited[nr][nc]

from sys import stdin
input = stdin.readline

# 쉽네 BFS 돌려버리자.
x,y = map(int,input().split())
treasure_map = []

for _ in range(x):
    treasure_map.append(list(input()))

max_length = 0
for i in range(x):
    for j in range(y):
        if treasure_map[i][j] == "L":
            check(i,j)

# 처음 실행되는 visited 에서 시작점을 1로 초기화해놨으니까 1 빼주면됨.
print(max_length - 1)