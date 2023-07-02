import sys
from collections import deque


def input_data():
	readl = sys.stdin.readline
	N = int(readl())
	map_cost = [
		[0] + list(map(int, readl()[:-1])) + [0] if 1 <= r <= N else [0] * (N + 2)
		for r in range(N + 2)
	]
	return N, map_cost


sol = -2

# 입력받는 부분
N, map_cost = input_data()

# 여기서부터 작성
# 상,하,좌,우
dr = [-1,1,0,0]
dc = [0,0,-1,1]

# BFS로 푸는데, 방문 처리는 한번만 하는게 아니라, 값을 비교해서 더 작을 경우 방문한다.
def BFS(r,c):
	q = [[r,c]]
	# print(visited)
	while q:
		cr,cc = q.pop(0)
		for i in range(4):
			
			nr = cr + dr[i]
			nc = cc + dc[i]
			
			if 1<=nr<N+1 and 1<=nc<N+1:
				if visited[nr][nc] > visited[cr][cc] + map_cost[nr][nc]:
					q.append([nr,nc])
					visited[nr][nc] = visited[cr][cc] + map_cost[nr][nc]
					
visited = [[99999] * (N+2) for i in range(N+2)]
visited[1][1] = 0
BFS(1,1)
print(visited[N][N])