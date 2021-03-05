import sys
sys.stdin = open('input.txt')
from pprint import pprint


def search_point(miro, k):
    for i in range(N):
        for j in range(N):
            if miro[i][j] == k:
                sr = i
                sc = j
                return sr, sc


def miro_search(sr, sc):
    # 상,하,좌,우
    dc = [0, 0, -1, 1]
    dr = [-1, 1, 0, 0]
    # 시작점 visit 체크, 큐에 집어넣기
    visited[sr][sc] = 1
    Q.append([sr, sc])
    # 큐에서 빼면서 돌기 점 이동하면, visit(옮긴점) = visit(옮기기 전 점) + 1
    while Q:
        r, c = Q.pop(0)
        for i in range(4):
            cr = r + dr[i]
            cc = c + dc[i]
            if 0 <= cc < N and 0 <= cr < N and miro[cr][cc] != 1 and visited[cr][cc] == 0:
                visited[cr][cc] = visited[r][c] + 1
                # pprint(visited)
                if miro[cr][cc] == 3:
                    return 1
                else:
                    Q.append([cr, cc])
    return 0


T = int(input())
for t in range(1, T+1):
    N = int(input())
    miro = [list(map(int, input())) for i in range(N)]
    flag = 0
    sr, sc = search_point(miro, 2)
    er, ec = search_point(miro, 3)
    visited = [[0 for _ in range(N)] for _ in range(N)]
    Q = []
    x = miro_search(sr, sc)
    result = visited[er][ec] - 2 if x else 0
    print('#%d %d' % (t, result))
