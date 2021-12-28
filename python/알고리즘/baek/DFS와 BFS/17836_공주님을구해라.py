# # 상하좌우
# dr = [-1,1,0,0]
# dc = [0,0,-1,1]

# def BFS(r,c,sword_flag):

#     q = [[r,c,sword_flag]]
#     visited[r][c] = 1
#     while q:
#         cr,cc,sword_flag = q.pop(0)
#         for i in range(4):
#             nr = cr + dr[i]
#             nc = cc + dc[i]
#             if 0 <= nr < n and 0 <= nc < m and visited[nr][nc] == 0:
#                 if castle[nr][nc] == 0:
#                     visited[nr][nc] = visited[cr][cc] + 1
#                     # print(nr,nc,sword_flag)             
#                     q.append([nr,nc,sword_flag])
#                 elif castle[nr][nc] == 2:
#                     sword_flag = 1
#                     visited[nr][nc] = visited[cr][cc] + 1
#                     # print(nr,nc,sword_flag)
#                     q.append([nr,nc,sword_flag])
#                 else:
#                     if sword_flag == 1:
#                         visited[nr][nc] = visited[cr][cc] + 1
#                         # print(nr,nc,sword_flag)
#                         q.append([nr,nc,sword_flag])


# n,m,t = map(int,input().split())

# castle = [list(map(int,input().split())) for _ in range(n)]

# flag = 0
# for i in range(n):
#     for j in range(m):
#         if castle[i][j] == 2:
#             sword = [i,j]
#             flag = 1
#             break
#     if flag:
#         break
# visited = [[0] * m for _ in range(n)]
# sword_flag = 0
# if sword[0] == 0 and sword[1] == 0:
#     sword_flag = 1
# BFS(0,0,sword_flag)

# if visited[n-1][m-1] == 0:
#     result = "Fail"
# else:
#     if visited[n-1][m-1] > 100:
#         result = "Fail"
#     else:
#         result = visited[n-1][m-1] - 1
# print(result)

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def BFS(r, c):
    global gongju
    q = [[r,c,0]]
    visited[r][c] = 1

    while q:
        cr, cc, time = q.pop(0)
        if cr == n-1 and cc == m-1:
            gongju = min(gongju, time)
            break
        if time+1 > t:
            break
        for i in range(4):
            nr = cr + dr[i]
            nc = cc + dc[i]
            if 0 <= nr < n and 0 <= nc < m and visited[nr][nc]==0:
                if castle[nr][nc] == 1:
                    continue
                elif castle[nr][nc] == 0:
                    visited[nr][nc] = 1
                    q.append([nr, nc, time+1])
                else:
                    visited[nr][nc] = 1
                    diff = time + 1 + abs(nr-(n-1)) + abs(nc-(m-1))
                    if diff <= t:
                        gongju = diff

n, m, t = map(int, input().split())
visited = [[0 for _ in range(m)] for _ in range(n)]
castle = [list(map(int, input().split())) for _ in range(n)]

gongju = 10001

BFS(0, 0)
if gongju > t:
    print('Fail')
else:
    print(gongju)