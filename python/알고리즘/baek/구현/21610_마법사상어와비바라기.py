from collections import deque

# 왼, 왼위, 위, 오위, 오, 오아, 아, 왼아
dr = [0, 0, -1, -1, -1, 0, 1, 1, 1]
dc = [0, -1, -1, 0, 1, 1, 1, 0, -1]

# 왼위, 오위, 오아, 왼아
drr = [-1,-1,1,1]
dcc = [-1,1,1,-1]

def action(d,s):
    # print(cloud)
    # 구름 이동
    next_cloud = deque()
    # check_cloud = deque()
    while cloud:
        cr,cc = cloud.popleft()
        nr = cr + dr[d] * s
        nc = cc + dc[d] * s
        if nr < 0:
            while nr < 0:
                nr += n
        elif nr >= n:
            while nr >= n:
                nr -= n
        if nc < 0:
            while nc < 0:
                nc += n
        elif nc >= n:
            while nc >= n:
                nc -= n
        # 구름 이동 후 비 1씩 내리기.
        # print("이동")
        # print(d,s)
        # print(cr,cc,nr,nc)
        basket[nr][nc] += 1
        visited[nr][nc] = 1
        next_cloud.append([nr,nc])
        # check_cloud.append([nr,nc])
    
    # 대각선 체크해서 물 더하기
    while next_cloud:
        cr,cc = next_cloud.popleft()
        cnt = 0
        for i in range(4):
            nr = cr + drr[i]
            nc = cc + dcc[i]
            if 0 <= nr < n and 0 <= nc < n:
                if basket[nr][nc]:
                    cnt += 1
        basket[cr][cc] += cnt
    
    # 구름 만들기
    for i in range(n):
        for j in range(n):
            if basket[i][j] >= 2 and not visited[i][j]:
                cloud.append([i,j])
                basket[i][j] -= 2
    


n,m = map(int,input().split())

# 하늘
basket = []
for _ in range(n):
    basket.append(list(map(int,input().split())))

# 구름 이동 명령
command = []
for _ in range(m):
    d,s = map(int,input().split())
    command.append([d,s])

# 실행 ㄱㄱ
water = 0
cloud = deque()
cloud.append([n-1,0])
cloud.append([n-1,1])
cloud.append([n-2,0])
cloud.append([n-2,1])
for i in range(m):
    visited = [[0 for _ in range(n)] for _ in range(n)]
    action(command[i][0], command[i][1])
    # print(basket)

for i in range(n):
    for j in range(n):
        if basket[i][j]:
            water += basket[i][j]
print(water)