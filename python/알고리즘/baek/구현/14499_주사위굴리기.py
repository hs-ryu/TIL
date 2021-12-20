
# 주사위를 굴렸을때 각 면 바꾸기.
def move(now):
    # 동쪽 굴리기
    if now == 1:
        # 주사위 위
        z = dice[0]
        # 주사위 동
        x = dice[2]
        # 주사위 서
        c = dice[3]
        # 주사위 바닥
        v = dice[5]
        dice[0] = c
        dice[2] = z
        dice[3] = v
        dice[5] = x
    # 서쪽 굴리기
    elif now == 2:
        # 주사위 위
        z = dice[0]
        # 주사위 동
        x = dice[2]
        # 주사위 서
        c = dice[3]
        # 주사위 바닥
        v = dice[5]
        dice[0] = x
        dice[2] = v
        dice[3] = z
        dice[5] = c
    # 남쪽 굴리기
    elif now == 3:
        # 주사위 위
        z = dice[0]
        # 주사위 북
        x = dice[1]
        # 주사위 남
        c = dice[4]
        # 주사위 바닥
        v = dice[5]
        dice[0] = x
        dice[1] = v
        dice[4] = z
        dice[5] = c
    # 북쪽 굴리기
    elif now == 4:
        # 주사위 위
        z = dice[0]
        # 주사위 북
        x = dice[1]
        # 주사위 남
        c = dice[4]
        # 주사위 바닥
        v = dice[5]
        dice[0] = c
        dice[1] = z
        dice[4] = v
        dice[5] = x


n, m, x, y, k = map(int, input().split())

jido = [list(map(int, input().split())) for _ in range(n)]
command = list(map(int, input().split()))

# 주사위는 최초 모든면이 0
# 위,북,동,서,남,바닥
dice = [0, 0, 0, 0, 0, 0]

# 동,서,북,남
dr = [0,0,-1,1]
dc = [1,-1,0,0]
for i in range(len(command)):
    now = command[i]
    # 동쪽으로 이동
    if now == 1:
        a = dr[0]
        b = dc[0]
    # 서쪽으로 이동
    elif now == 2:
        a = dr[1]
        b = dc[1]
    # 북쪽으로 이동
    elif now == 3:
        a = dr[2]
        b = dc[2]
    # 남쪽으로 이동
    elif now == 4:
        a = dr[3]
        b = dc[3]
    # 범위 안에있을때만 실행
    if 0 <= x + a < n and 0 <= y + b < m:
        x += a
        y += b
        # print('x', x)
        move(now)
        # 이동한 칸에 쓰여 있는 수가 0이면 주사위의 바닥면에 쓰여 있는 수가 칸에 복사됨.
        if jido[x][y] == 0:
            jido[x][y] = dice[5]
        # 0이 아닌경우 칸에 쓰여 있는 수가 주사위의 바닥면으로 복사, 칸에 쓰여 있는 수는 0이 됨
        else:
            dice[5] = jido[x][y]
            jido[x][y] = 0
        # 상단 출력
        print(dice[0])
