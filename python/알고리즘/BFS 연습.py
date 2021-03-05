# def BFS(s):
#     # 어 이거 BFS로 풀어야 된다! -> 제일 먼저 방문표시, 큐에 집어넣기
#     visit = []
#     visited[s] = True
#     queue.append(s)
#     while queue:
#         target = queue.pop(0)
#         visit.append(target)
#         for x in AL[target]:
#             if not visited[x]:
#                 visited[x] = 1
#                 queue.append(x)
#     return visit
# N = 7
# visited = [0] * (N+1)
# queue = []
# AL = [] # 얘만 설정 해주면 됨.
#
# BFS(1)
# result = BFS(1)


#재귀로 풀기
def BFS(x):
    cnt = 0
    for n in to_go[x]:
        if n not in visited and n not in q:
            q.append(n)
            cnt += 1
    for _ in range(cnt):
        visited.append(q[0])
        BFS(q.pop(0))

t = int(input())
N, V = map(int, input().split())
to_go = [[] for _ in range(N+1)]
for i in range(V):
    s, e = map(int, input().split())
    to_go[s].append(e)

q = [1]
visited = [1]
BFS(q.pop(0))
print("#%d" %t, end=' ')
print(*visited)