# from pprint import pprint

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

def turn_left():
    global d
    d -= 1
    if d == -1:
        d = 3

n,m = map(int, input().split())

r,c,d = map(int, input().split())

# 0: 상, 1: 우, 2: 하, 3: 좌

place = [list(map(int, input().split())) for _ in range(n)]
visited = [[0] * m for _ in range(n)]
cnt = 0
is_possible = True
while True:
    if visited[r][c] == 0:
        visited[r][c] = 1
        cnt += 1
    # 주변 4칸 중 청소되지 않은 빈 칸이 없는 경우
    for i in range(4):
        turn_left()
        nr = r + dr[d]
        nc = c + dc[d]
        if place[nr][nc] == 0 and visited[nr][nc] == 0:
            r = nr
            c = nc
            break
    else:
        # 뒤쪽 방향이 벽이라 후진할 수 없는 경우
        if place[r-dr[d]][c-dc[d]] == 1:
            is_possible = False
            break
        else:
            r -= dr[d]
            c -= dc[d]
    if is_possible == False:
        break
# pprint(visited)
print(cnt)