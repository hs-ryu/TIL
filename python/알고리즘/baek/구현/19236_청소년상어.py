# 위, 왼위, 왼, 왼아, 아, 오아, 오, 오위
dr = [-1, -1,0,1,1,1,0,-1]
dc = [0, -1, -1, -1, 0, 1,1,1]

# 찾기
def play(r,c,new_fishs, new_dir,temp_result):
    temp_result += new_fishs[r][c]
    new_fishs[r][c] = "상"
    pass



inf = [list(map(int,input().split())) for _ in range(4)]

# 물고기들 정보
fishs = [[0] * 4 for _ in range(4)]
# 방향 정보
dir = [[0] * 4 for _ in range(4)]

# 물고기정보, 방향정보 셋팅
for i in range(4):
    for j in range(4):
        fishs[i][j] = inf[i][j*2]
        dir[i][j] = inf[i][j*2 + 1]
result = 0

# 상어의 위치 (r,c), 물고기 정보, 방향, 현재까지의 최댓값을 인자로 넣어줌.
play(0,0,fishs,dir,0)

print(result)