import sys
sys.stdin = open('5250_input.txt')



# BFS로 풀기
#상하좌우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
def search():
    q = [[0,0]]
    cnt = [[987654321] * N for _ in range(N)]
    cnt[0][0] = 0
    while q:
        cr, cc = q.pop(0)
        for i in range(4):
            nr = cr + dr[i]
            nc = cc + dc[i]
            if 0 <= nr < N and 0 <= nc < N:
                height = (area[nr][nc] - area[cr][cc]) if area[nr][nc] > area[cr][cc] else 0
                if cnt[nr][nc] > cnt[cr][cc] + 1 + height:
                    cnt[nr][nc] = cnt[cr][cc] + 1 + height
                    q.append([nr,nc])
    return cnt[-1][-1]

T = int(input())
for t in range(1, T+1):
    N = int(input())
    area = [list(map(int, input().split())) for _ in range(N)]
    result = search()
    print('#%d %d' %(t, result))