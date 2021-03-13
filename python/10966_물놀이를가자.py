'''
여름이 되어 물놀이를 가는 사람들이 많다. 
지도는 N×M크기의 격자로 표현이 가능하고, 위쪽에서 i번째 줄의 왼쪽에서 j번째 칸이 물이면 ‘W’, 땅이면 ‘L’로 표현된다. 
어떤 칸에 사람이 있으면, 그 칸의 상하좌우에 있는 칸으로 이동하는 것을 반복하여 다른 칸으로 이동할 수 있다.
 단, 격자 밖으로 나가는 이동은 불가능하다. 
 땅으로 표현된 모든 칸에 대해서, 어떤 물인 칸으로 이동하기 위한 최소 이동 횟수를 구하고 모든 이동 횟수의 합을 출력하는 프로그램을 작성하라.

 

[입력]

첫 번째 줄에 테스트 케이스의 수 가 주어진다.
 

각 테스트 케이스의 첫 번째 줄에는 두 정수 이 공백 하나로 구분되어 주어진다.

다음 개의 줄에는 길이 인 문자열이 주어진다. 문자열은 ‘W’또는 ‘L’로만 이루어져 있다. 
모든 줄의 문자열을 모두 합쳤을 때, 적어도 하나의 ‘W’는 주어지는 것이 보장된다.

 

[출력]
 

각 테스트 케이스마다 땅으로 표현된 모든 칸에 대해서, 물인 칸으로 이동하기 위한 최소 이동 횟수의 합을 출력한다.
'''

import sys
sys.stdin = open('10966.txt')

#상하좌우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]




#Runtime error

# 최소거리 : BFS
# def BFS():
#     Q = [i for i in water]
#     total = 0
#     while Q:
#         cr, cc = Q.pop(0)
#         for i in range(4):
#             r = cr + dr[i]
#             c = cc + dc[i]
#             if 0 <= r < N and 0 <= c < M and grid[r][c]== 'L' and visited[r][c] == 0:
#                 visited[r][c] = visited[cr][cc] + 1
#                 Q.append([r, c])
#                 total += visited[r][c]
#     return total

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    grid = [list(input()) for _ in range(N)]
    Q = []
    for i in range(N):
        for j in range(M):
            if grid[i][j] == 'W':
                Q.append([i, j])

    visited = [[0] * M for _ in range(N)]
    total = 0
    while Q:
        cr, cc = Q.pop(0)
        for i in range(4):
            r = cr + dr[i]
            c = cc + dc[i]
            if 0 <= r < N and 0 <= c < M and grid[r][c] == 'L' and visited[r][c] == 0:
                visited[r][c] = visited[cr][cc] + 1
                Q.append([r, c])
                total += visited[r][c]
    print('#%d %d' % (t, total))
    






















# 아이디어1. 모든 땅에서 가장 가까운 물을 찾는다.  -> ????
# 물에서 각 땅에 대한 최단 거리를 찾는 경우  -> 물에서 출발하는 BFS
# 물이 여러개면 여러개 시작점