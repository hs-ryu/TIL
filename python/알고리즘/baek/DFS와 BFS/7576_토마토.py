'''
문제
철수의 토마토 농장에서는 토마토를 보관하는 큰 창고를 가지고 있다. 토마토는 아래의 그림과 같이 격자 모양 상자의 칸에 하나씩 넣어서 창고에 보관한다. 


창고에 보관되는 토마토들 중에는 잘 익은 것도 있지만, 아직 익지 않은 토마토들도 있을 수 있다. 
보관 후 하루가 지나면, 익은 토마토들의 인접한 곳에 있는 익지 않은 토마토들은 익은 토마토의 영향을 받아 익게 된다. 
하나의 토마토의 인접한 곳은 왼쪽, 오른쪽, 앞, 뒤 네 방향에 있는 토마토를 의미한다. 
대각선 방향에 있는 토마토들에게는 영향을 주지 못하며, 토마토가 혼자 저절로 익는 경우는 없다고 가정한다. 
철수는 창고에 보관된 토마토들이 며칠이 지나면 다 익게 되는지, 그 최소 일수를 알고 싶어 한다.

토마토를 창고에 보관하는 격자모양의 상자들의 크기와 익은 토마토들과 익지 않은 토마토들의 정보가 주어졌을 때, 
며칠이 지나면 토마토들이 모두 익는지, 그 최소 일수를 구하는 프로그램을 작성하라. 단, 상자의 일부 칸에는 토마토가 들어있지 않을 수도 있다.

입력
첫 줄에는 상자의 크기를 나타내는 두 정수 M,N이 주어진다. M은 상자의 가로 칸의 수, N은 상자의 세로 칸의 수를 나타낸다. 단, 2 ≤ M,N ≤ 1,000 이다.
둘째 줄부터는 하나의 상자에 저장된 토마토들의 정보가 주어진다. 즉, 둘째 줄부터 N개의 줄에는 상자에 담긴 토마토의 정보가 주어진다.
하나의 줄에는 상자 가로줄에 들어있는 토마토의 상태가 M개의 정수로 주어진다. 
정수 1은 익은 토마토, 정수 0은 익지 않은 토마토, 정수 -1은 토마토가 들어있지 않은 칸을 나타낸다.
토마토가 하나 이상 있는 경우만 입력으로 주어진다.

출력
여러분은 토마토가 모두 익을 때까지의 최소 날짜를 출력해야 한다. 
만약, 저장될 때부터 모든 토마토가 익어있는 상태이면 0을 출력해야 하고, 토마토가 모두 익지는 못하는 상황이면 -1을 출력해야 한다.
'''

# 답은 맞는데 시간초과... 시불
#최소일수 구하기 : BFS

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def BFS(k):
    Q = [start_point.pop() for _ in range(k)]
    while Q:
        cr, cc = Q.pop(0)
        for i in range(4):
            r = cr + dr[i]
            c = cc + dc[i]
            if 0 <= r < N and 0 <= c < M and visited[r][c] == 0:
                if tomato[r][c] == -1:
                    visited[r][c] = -1
                elif tomato[r][c] == 0:
                    Q.append([r,c])
                    tomato[r][c] = 1
                    visited[r][c] = visited[cr][cc] + 1

def dayday(visited):
    maxV = 0
    for i in range(N):
        for j in range(M):
            if visited[i][j] == -1:
                continue
            if visited[i][j] == 0:
                if tomato[i][j] == -1:
                    continue
                return -1
            elif visited[i][j] > maxV:
                maxV = visited[i][j]
    return maxV

M, N = map(int, input().split())

tomato = [list(map(int, input().split())) for _ in range(N)]
visited = [[0 for _ in range(M)] for _ in range(N)]
start_point = []

for i in range(N):
    for j in range(M):
        if tomato[i][j] == 1:
            start_point.append([i, j])
            visited[i][j] = 1
k = len(start_point)
BFS(k)
result = dayday(visited)
if result != -1:
    res = result-1
else:
    res = -1
print(res)