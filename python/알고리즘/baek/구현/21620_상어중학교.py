# 상,하,좌,우
dr = [-1,1,0,0]
dc = [0,0,-1,1]
def make_block_group(r,c):
    zero_visited = [[0] * n for _ in range(n)]
    block_group = {"counts" : 1, "rainbow" : 0, "coordi" : [[r,c]], "nonzero_coordi":[[r,c]]}
    visited[r][c] = 1
    target_number = arr[r][c]
    q = [[r,c]]
    while q:
        cr,cc = q.pop(0)
        for i in range(4):
            nr = cr + dr[i]
            nc = cc + dc[i]
            if 0 <= nr < n and 0 <= nc < n and visited[nr][nc] == 0:
                if arr[nr][nc] == target_number:
                    visited[nr][nc] = 1
                    block_group["counts"] += 1
                    block_group["coordi"].append([nr,nc])
                    block_group["nonzero_coordi"].append([nr,nc])
                    q.append([nr,nc])
                elif arr[nr][nc] == 0 and zero_visited[nr][nc] == 0:
                    zero_visited[nr][nc] = 1
                    block_group["counts"] += 1
                    block_group["rainbow"] += 1
                    block_group["coordi"].append([nr,nc])
                    q.append([nr,nc])
    if block_group["counts"] != 1:
        block_group["nonzero_coordi"] = sorted(block_group["nonzero_coordi"], key= lambda x:(x[0], x[1]))
        block_groups.append(block_group)

def gravity():
    for c in range(n):
        area = 0
        for r in range(n-1,-1,-1):
            if arr[r][c] == -2:
                area += 1
            elif arr[r][c] == -1:
                area = 0
            else:
                if area != 0:
                    arr[r+area][c] = arr[r][c]
                    arr[r][c] = -2

def rotate_90():
    new_arr = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            new_arr[n-1-j][i] = arr[i][j]
    return new_arr

n,m = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(n)]
score = 0
# 가장 많은 블럭이 들어간 그룹 찾기 -> 여러개일 경우 무지개 블럭이 많은것 -> 기준 블럭 행이 가잔 큰 것 -> 기준 블럭 열이 가장 큰 것
# 기준 블럭 : 무지개 블럭이 아닌 그룹 중 행의 번호, 열의 번호가 가장 작은 블럭
while True:
    # 만들어진 블록 그룹들이 들어갈 배열
    block_groups = []
    visited = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if arr[i][j] != -1 and arr[i][j] != 0 and arr[i][j] != -2 and visited[i][j] == 0:
                make_block_group(i,j)
    # 만들어진 블록 그룹이 없다면 그만.
    if len(block_groups) == 0:
        break
    block_groups.sort(key=lambda x:(-x["counts"], -x["rainbow"], -x["nonzero_coordi"][0][0], -x["nonzero_coordi"][0][1]))
    target_block_group = block_groups[0]
    # 블록 그룹 제거, 점수 획득
    score += target_block_group["counts"] ** 2
    for r,c in target_block_group["coordi"]:
        arr[r][c] = -2
    # 중력 작용
    gravity()
    # 90도 반시계 회전
    arr = rotate_90()
    # 중력 작용
    gravity()
print(score)