# 위, 아래, 왼쪽, 오른쪽
dr = [0, -1, 1, 0, 0]
dc = [0, 0, 0, -1, 1]

def move(shark):
    cr, cc = shark_location[shark]
    none_area = []
    for i in range(1,5):
        nr = cr + dr[i]
        nc = cc + dc[i]
        if 0<=nr<n and 0<=nc<n:
            if arr[nr][nc] == 0 and [nr,nc] not in sharks_moved[shark]:
                none_area.append([nr,nc])
                
    pass


n,m,k = map(int,input().split())

arr = [list(map(int,input().split())) for _ in range(n)]
shark_location = dict()

for i in range(n):
    for j in range(n):
        if arr[i][j]:
            shark_location[arr[i][j]] = [i,j]

sharks_direction = list(map(int,input().split()))

sharks_direction_priority = []
for i in range(m):
    temp_shark = dict()
    for j in range(1,5):
        temp_shark[j] = list(map(int,input().split()))
    sharks_direction_priority.append(temp_shark)

sharks_moved = [[] * (m+1)]
for i in range(1,m+1):
    move(i)