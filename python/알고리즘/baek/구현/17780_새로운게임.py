# 우, 좌, 상, 하
dr = [0, 0, 0, -1, 1]
dc = [0, 1, -1, 0, 0]

def change_direction(d):
    if d == 1:
        return 2
    elif d == 2:
        return 1
    elif d == 3:
        return 4
    else:
        return 3

n,k = map(int,input().split())

# 0: 흰색, 1: 빨간색, 2: 파란색
# 이동하려는 칸이
# 흰색 -> 그냥 그 칸으로 이동. 그 칸에 이미 체스가 있다면 올라탄다
# 빨간색 -> 이동한 말의 순서가 반대로 바뀐다. 이미 그 자리에 체스가 있는 경우 순서가 바뀌고 난 후 올라탄다.
# 파란색 -> 이동방향 바꾸고 반대로 1칸 이동. 방향을 반대로 한 후에 이동하려는 칸이 파란색이라면 방향만 바꾼다.
# 벽 -> 이동방향 바꾸고 반대로 1칸 이동

# 턴 한번 : 1~k번의 모든 말이 순서대로 한번씩 이동. 위에 올려져 있는 말이 있다면 가장 아래에 있는 말이 이동한다. (이동 방향은 현재 이동하려는 말의 방향인듯)

# 말이 4개 이상 쌓이면 끝

chess_map = [list(map(int,input().split())) for _ in range(n)]

numbers_location = [[[] for _ in range(n)] for _ in range(n)]
numbers_direction = [0] * (k+1)

for i in range(1,k+1):
    r,c,direction = map(int,input().split())
    numbers_location[r-1][c-1].append(i)
    numbers_direction[i] = direction

now_round = 0
escape = False
while True:
    now_round += 1
    if now_round >= 1000:
        break
    
    # 찾기!
    for num in range(1,k+1):
        cr, cc = 0, 0
        find_flag = False
        for r in range(n):
            for c in range(n):
                for i in range(len(numbers_location[r][c])):
                    if numbers_location[r][c][i] == num:
                        cr, cc = r,c
                        find_flag = True
                        break
                if find_flag:
                    break
            if find_flag:
                break
    
        # 제일 아래꺼만 이동 가능하니까, 제일 아랫놈이 아니면 패스
        if numbers_location[cr][cc][0] != num:
            continue
        
        # 이동 가능하다면 -> 이동해야지
        nr = cr + dr[numbers_direction[num]]
        nc = cc + dc[numbers_direction[num]]

        # 체스판을 벗어나지 않는 경우. 하나씩 보자
        if 0 <= nr < n and 0 <= nc < n:
            # 가려는 칸이 흰색일때
            if chess_map[nr][nc] == 0:
                numbers_location[nr][nc].extend(numbers_location[cr][cc])
                numbers_location[cr][cc] = []
            # 가려는 칸이 빨간색일때
            elif chess_map[nr][nc] == 1:
                temp = list(reversed(numbers_location[cr][cc]))
                numbers_location[nr][nc].extend(temp)
                numbers_location[cr][cc] = []
            # 가려는 칸이 파란색일때
            else:
                # 자, 근데 여기서도 반대로 이동하는 곳이 빨간색인지, 파란색인지, 체스판을 벗어나는 경우를 확인해야한다.
                # 일단 방향 바꾸기
                numbers_direction[num] = change_direction(numbers_direction[num])
                nr = cr + dr[numbers_direction[num]]
                nc = cc + dc[numbers_direction[num]]

                if 0 <= nr < n and 0 <= nc < n:
                    # 가려는 칸이 흰색일때
                    if chess_map[nr][nc] == 0:
                        numbers_location[nr][nc].extend(numbers_location[cr][cc])
                        numbers_location[cr][cc] = []
                    # 가려는 칸이 빨간색일때
                    elif chess_map[nr][nc] == 1:
                        temp = list(reversed(numbers_location[cr][cc]))
                        numbers_location[nr][nc].extend(temp)
                        numbers_location[cr][cc] = []
                else:
                    nr = cr
                    nc = cc

        
        # 체스판을 벗어나는 경우. 파란색과 같은 로직
        # 방향 반대로 놓고, 한칸 이동. 빨간색인지, 파란색인지, 체스판을 벗어나는 경우 확인 필요
        else:
            numbers_direction[num] = change_direction(numbers_direction[num])
            nr = cr + dr[numbers_direction[num]]
            nc = cc + dc[numbers_direction[num]]
            if chess_map[nr][nc] == 0:
                numbers_location[nr][nc].extend(numbers_location[cr][cc])
                numbers_location[cr][cc] = []
            # 가려는 칸이 빨간색일때
            elif chess_map[nr][nc] == 1:
                temp = list(reversed(numbers_location[cr][cc]))
                numbers_location[nr][nc].extend(temp)
                numbers_location[cr][cc] = []
            
        if len(numbers_location[nr][nc]) >= 4:
            escape = True
        
    if escape:
        break

if now_round == 1000:
    print(-1)
else:
    print(now_round)