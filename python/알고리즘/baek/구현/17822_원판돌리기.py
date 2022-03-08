# 원판 규칙 : 주어진 배열에서 위,아래, 양 옆과 인접함. 단, 행이 처음이나 마지막일 경우 위나 아래는 없음.
# 1. 원판 돌리기
# 1-1. x의 배수인 원판을 d 방향으로 k칸 회전시킴. d가 0이면 시계방향, 1이면 반시계방향
# 2. 인접한 애들 조건에 맞춰주기
# 2-1. 인접하면서 수가 같은애들 찾아 없애기.
# 2-2. 없다면, 원판에 적힌 수의 평균을 구하고, 평균보다 큰 수에서 1을 빼고, 작은 수에는 1을 더하기.
# T번 반복하고, 끝났을때 남은 애들 합 구하기.

dd = [-1,1]

# 돌려돌려 돌림판. 굳 최고.
def rotation(p, dir, h):
    rotated_disk = [0 for _ in range(m)]
    for i in range(m):
        j = i + dd[dir] * h
        if j >= m:
            j -= m
        elif j < 0:
            j += m
        rotated_disk[i] = disk[p][j]
    disk[p] = rotated_disk

# BFS로?
# 인접한 숫자 지우기
dr = [-1,1,0,0]
dc = [0,0,-1,1]
def remove_nums(r,c):
    global flag
    q = [[r,c]]
    remove_list = [[r,c]]
    visited = [[0] * m for _ in range(n)]
    visited[r][c] = 1
    while q:
        cr,cc = q.pop(0)
        for i in range(4):
            nr = cr + dr[i]
            nc = cc + dc[i]
            # 제일 안쪽거랑 제일 바깥쪽꺼 처리.
            if 0 <= nr < n:
                # 양 옆 범위 넘어가는거 처리
                if nc < 0:
                    nc += m
                elif nc >= m:
                    nc -= m
                # 같은 애들 있으면 플래그 1로 바까주고, q
                if visited[nr][nc] == 0 and disk[cr][cc] == disk[nr][nc]:
                    flag = 1
                    visited[nr][nc] = 1
                    q.append([nr,nc])
                    remove_list.append([nr,nc])
    
    # 지워주기. 기존에 remove_list에 하나 넣어놨으니까, 1보다 커야지 같은 값이 있는거임.
    if len(remove_list) > 1:
        for i in range(len(remove_list)):
            r,c = remove_list[i]
            disk[r][c] = 0

# 제거한 수가 없으면 평균 구해서 계산해주기.
def average_change():
    total = 0
    cnt = 0
    for i in range(n):
        for j in range(m):
            if disk[i][j]:
                total += disk[i][j]
                cnt += 1
    # 다 0일때 0으로 나눠지는거 방지.
    if cnt != 0:
        mean = total / cnt
    
    # 평균보다 작거나 큰 애들 계산해주기.
    for i in range(n):
        for j in range(m):
            # 0이 아닌애들만 계산해주기.
            if disk[i][j]:
                if disk[i][j] < mean:
                    disk[i][j] += 1
                elif disk[i][j] > mean:
                    disk[i][j] -= 1

n,m,t = map(int,input().split())


disk = [list(map(int,input().split())) for _ in range(n)]

# print(disk)

for _ in range(t):
    x,d,k = map(int,input().split())
    
    # x의 배수 원판들 돌려돌려 돌림판
    target = n//x
    for i in range(1,target+1):
        rotation(x*i-1, d, k)
    # print("돌린 후",disk)

    # 인접한 수가 같은것을 지운게 있는지 체크하는 플래그. 없으면 2-2 실행하기 위함.
    flag = 0
    for i in range(n):
        for j in range(m):
            if not disk[i][j]:
                continue    
            remove_nums(i,j)
    # print("같은애들 제거후",disk)
    
    # 인접한 같은 애들이 없어 제거 작업이 안이루어지면 평균 구해서 계산해주는 작업하기.
    if flag == 0:
        average_change()
        # print("평균 더해준 후", disk)

# t번 작업 끝난 뒤 남은 애들 합 구하기.
result = 0
for i in range(n):
    for j in range(m):
        result += disk[i][j]
print(result)


