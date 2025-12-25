
# 상, 우상, 우, 우하, 하, 좌하, 좌, 좌상
dr = [-1,-1,0,1,1,1,0,-1]
dc = [0,1,1,1,0,-1,-1,-1]

def move(cr, cc, info, new_map):
    mass, speed, direction = info
    new_r = (cr + speed * dr[direction]) % n
    new_c = (cc + speed * dc[direction]) % n
    if new_map[new_r][new_c] == 0:
        new_map[new_r][new_c] = [mass, speed, direction]
    else:
        new_map[new_r][new_c].append([mass, speed, direction])


n,m,k = list(map(int, input().split()))

arr = [[0] * n for i in range(n)]


for i in range(m):
    a,b,c,d,e = map(int, input().split())
    arr[a-1][b-1] = [c,d,e]

cnt = 0
while cnt < k:
    cnt += 1
    new_map = [[0] * n for i in range(n)]

    for i in range(n):
        for j in range(n):
            if arr[i][j] != 0:
                move(i, j, arr[i][j], new_map)

    arr = new_map[:]