# 위, 왼위, 왼, 왼아, 아, 오아, 오, 오위
dr = [-1, -1,0,1,1,1,0,-1]
dc = [0, -1, -1, -1, 0, 1,1,1]

# 찾기. DFS 구만.
def play(r,c,new_fishs, new_dir,new_info,temp_result):
    # 먼저. 낮은 애들부터 이동시킨다.
    for i in range(len(new_info)):
        move_one = new_info[i]
        nr = move_one[2] + dr[move_one[1]-1]
        nc = move_one[3] + dc[move_one[1]-1]
        # 범위 내에서만 이동 가능
        if 0 <= nr < 4 and 0 <= nc < 4 and new_fishs[nr][nc] != "상":
            # 자리 바까주기. 방향도
            new_fishs[move_one[2]][move_one[3]], new_fishs[nr][nc] = new_fishs[nr][nc], new_fishs[move_one[2]][move_one[3]]
            new_dir[move_one[2]][move_one[3]], new_dir[nr][nc] = new_dir[nr][nc], new_dir[move_one[2]][move_one[3]]
        else:
            pass

inf = [list(map(int,input().split())) for _ in range(4)]

# 물고기들 정보
fishs = [[0] * 4 for _ in range(4)]
# 방향 정보
dir = [[0] * 4 for _ in range(4)]

new_inf = []
# 물고기정보, 방향정보 셋팅
for i in range(4):
    for j in range(4):
        fishs[i][j] = inf[i][j*2]
        dir[i][j] = inf[i][j*2 + 1]
        # 순서 처리하기 쉽게, 하나의 리스트에 관리 ㄱ
        new_inf.append([fishs[i][j], dir[i][j],i,j])

result = 0
new_inf.sort(key=lambda x:x[0])
new_inf.pop(fishs[0][0]-1)
result += fishs[0][0]
fishs[0][0] = '상'

print(new_inf)
# 상어의 위치 (r,c), 물고기 정보, 방향, 현재까지의 최댓값을 인자로 넣어줌.
play(0,0,fishs,dir,new_inf,0)

print(result)