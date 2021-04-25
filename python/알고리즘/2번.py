dxy = [[0, 1], [1, 0], [0, -1], [-1, 0]]

def attack(nat): # nat : 공격턴인 나라
    # 상대방 지역의 병력보다 상하좌우로 인접한 자신의 나라의 병력의 합이 5 배를 초과할 경우, 각 지역에서 1/4 의 병력을 보내 공격한다
    res = []
    for x in range(N):
        for y in range(N):
            # 다른 나라 땅이면
            if nations[x][y] != nat and nations[x][y] != 0:
                total = 0
                # 인접 4방향 중에서 공격턴 나라의 병력 계산
                for dx, dy in dxy:
                    nx = x + dx
                    ny = y + dy
                    if 0 <= nx < N and 0 <= ny < N and nations[nx][ny] == nat:
                        total += army[nx][ny]
                if total > army[x][y] * 5:
                    # 전체 병력 - 방어병력 and 나라 변경
                    for dx, dy in dxy: # 1/4씩 감소
                        nx = x + dx
                        ny = y + dy
                        if 0 <= nx < N and 0 <= ny < N and nations[nx][ny] == nat:
                            army_tmp = int(army[nx][ny] * 1 / 4)
                            res.append((nx, ny, -army_tmp, nat))
                            res.append((x,y,-int(army[nx][ny] * 1 / 4), nat))

    for xx,yy,after_army,after_nat in res:
        army[xx][yy] += after_army
        nations[xx][yy] = after_nat
    
    for xx,yy,after_army,after_nat in res:
        if army[xx][yy] < 0:
            army[xx][yy] *= -1



def assistance(nat):
    tmp = []
    #   a. 인접한 지역 중 다른 나라의 지역이 없는 경우, 모든 인접한 지역으로 그 지역의 병력의 1/5을 각각 지원한다.    
    for x in range(N):
        for y in range(N):
            # 자기 나라 땅이면
            if nations[x][y] == nat:
                # 인접 4방향 중에서 다른 나라 있는지 검사
                check = True # 인접 4방향에 다른나라가 없으면 True
                for dx, dy in dxy:
                    nx = x + dx
                    ny = y + dy
                    if 0 <= nx < N and 0 <= ny < N:
                        if nations[nx][ny] == nat or nations[nx][ny] == 0:
                            continue
                        else:
                            check = False
                            break

                if check:
                    for dx, dy in dxy:
                        nx = x + dx
                        ny = y + dy
                        # 4방향 돌면서 1/5씩 보충
                        if 0 <= nx < N and 0 <= ny < N and nations[nx][ny] == nat:
                            tmp.append((nx, ny, int(army[x][y]/5)))
                            tmp.append((x, y, -int(army[x][y]/5)))
                else:
                    for dx, dy in dxy:
                        nx = x + dx
                        ny = y + dy
                        if 0 <= nx < N and 0 <= ny < N and nations[nx][ny] == nat and army[nx][ny] * 5 < army[x][y]:
                            tmp.append((nx, ny, int(army[x][y]//5)))
                            tmp.append((x, y, -int(army[x][y]//5)))
    #   b. 인접한 지역 중 다른 나라의 지역이 있을 경우, 그 지역의 병력이 인접한 아군 나라의 병력의 5 배를 초과할 경우에만, 
    # 그 지역의 병력의 1/5을 인접한 지역으로 지원한다.
    
    for xx,yy,after_as in tmp:
        army[xx][yy] += after_as




def supplement():
    for i in range(N):
        for j in range(N):
            army[i][j] += supple[i][j]



for tc in range(1,1+int(input())):
    N = int(input()) # 지도의 한 변의 길이 (3<=N<=10)
    nations = [list(map(int, input().split())) for _ in range(N)] # 지역의 소유 정보(0,1,2,3): 0:산간지역
    army = [list(map(int, input().split())) for _ in range(N)] # 병력 정보
    supple = [list(map(int, input().split())) for _ in range(N)] # 보충 정보

    three_nat = [1] * 4
    ending = True
    while ending:
        for i in range(1,4):
            if not three_nat[i]:
                continue
            attack(i) # 공격
            assistance(i) # 지원
            supplement() # 전체 보충

            three_nat = [0] * 4
            for x in nations:
                for y in range(4):
                    three_nat[y] += x.count(y)
            for z in range(1,4):
                if three_nat[0] + three_nat[z] == N**2:
                    ending = False
                    break
            if not ending:
                break

            

    result = 0

    for s in army:
        result += sum(s)
    print('#{} {}'.format(tc,result))












    -----------------------------------


    drc = [(0, 1), (1, 0), (0, -1), (-1, 0)]

# n번 나라의 공격
def fight(n):
    cnt = [[0]*N for _ in range(N)]
    boom = [[0]*N for _ in range(N)]
    for r in range(N):
        for c in range(N):
            # 산악이 아니고 n이 아닐 때(상대방 나라일 때)
            if statement[r][c] > 0 and statement[r][c] != n:
                # 누적 공격력
                tmp = 0
                tmp2 = 0
                drc_idx = []
                for dr, dc in drc:
                    nr, nc = r+dr, c+dc
                    if 0<=nr<N and 0<=nc<N:
                        if statement[nr][nc] == n:
                            tmp += army[nr][nc]
                            tmp2 += army[nr][nc]//4
                            drc_idx.append((nr, nc))
                # 공격 조건 해당한다면
                if tmp > army[r][c]*5:
                    boom[r][c] = tmp2
                    for i, j in drc_idx:
                        cnt[i][j] += 1
    # print('boom', boom)
    # print('cnt', cnt)
    # 공격 완료 후
    for r in range(N):
        for c in range(N):
            if boom[r][c]:
                army[r][c] = boom[r][c]-army[r][c]
                statement[r][c] = n
            if cnt[r][c]:
                army[r][c] -= (army[r][c]//4)*cnt[r][c]
    return

# 인접 지역에 다른 나라 없는지 체크하는 함수(있으면 Flag = 1 반환)
def check(r, c, n):
    tmp = []
    flag = 0
    for dr, dc in drc:
        nr, nc = r+dr, c+dc
        if 0<=nr<N and 0<=nc<N:
            if statement[nr][nc] > 0 and statement[nr][nc] != n:
                flag = 1
            if statement[nr][nc] == n:
                tmp.append((nr, nc))
    return flag, tmp

def cover(n):
    cnt = [[0]*N for _ in range(N)]
    covered = [[0]*N for _ in range(N)]
    for r in range(N):
        for c in range(N):
            # n일 때
            if statement[r][c] == n:
                # 인접 지역에 다른 나라 없으면
                ishere, tmp = check(r, c, n)
                if not ishere:
                    for i, j in tmp:
                        cnt[r][c] += army[r][c]//5
                        covered[i][j] += army[r][c]//5
                # 다른 나라 있으면
                else:
                    for i, j in tmp:
                        if army[r][c] > army[i][j]*5:
                            cnt[r][c] += army[r][c]//5
                            covered[i][j] += army[r][c]//5
    # print('covered', covered)
    # print('cnt', cnt)
    # 파악 종료 후
    for r in range(N):
        for c in range(N):
            if covered[r][c]:
                army[r][c] += covered[r][c]
            if cnt[r][c]:
                army[r][c] -= cnt[r][c]
    return

def refilled():
    for r in range(N):
        for c in range(N):
            army[r][c] += refill[r][c]
    return

def state_cnt(n):
    cnt = 0
    for r in range(N):
        for c in range(N):
            if statement[r][c] == n:
                cnt += 1
    return cnt

T = int(input())
for t in range(1, T+1):
    N = int(input())
    statement = [list(map(int, input().split())) for _ in range(N)]
    army = [list(map(int, input().split())) for _ in range(N)]
    refill = [list(map(int, input().split())) for _ in range(N)]
    flag = 0
    while True:
        if flag == 1:
            break
        for i in range(1, 4):
            cnt = state_cnt(i)
            if cnt > 0:
                # print('turn', i)
                # 공격
                fight(i)
                # print(army)
                # 지원
                cover(i)
                # print(army)
                # 보충
                refilled()
                # print(statement)
                # print(army)
            if state_cnt(i)+state_cnt(0) == N**2:
                flag = 1
                break

    print("#%d %d" % (t, sum(sum(army[i]) for i in range(N))))