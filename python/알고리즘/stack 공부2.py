V, E = 7, 8
edges = '1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7'
line = list(map(int, edges.split()))
edges = [(line[i], line[i + 1]) for i in range(0, len(line), 2)]

AM = [[0 for i in range(V+1)] for i in range(V+1)]
for s, e in edges:
    AM[s][e] = 1
    AM[e][s] = 1

AL = [[] for _ in range(V+1)]
for s, e in edges:
    AL[s].append(e)
    AL[e].append(s)
print(edges)
print(AL)
print(AM)


def DFS(V, AM, sv):
    visited = [0] * (V+1)
    stack = [sv]
    travel = []
    # 스택에 내용이 있는 동안
    while len(stack):
        # 스택에서 pop.
        node = stack.pop()
        # 방문 했는지 안했는지 확인해서, 방문을 안 했을때
        if not visited[node]:
            # 1. 방문 표시를 한다.
            visited[node] = 1
            travel.append(node)
            # 2. node와 연결되어 있으면서 아직 방문하지 않은 node를 스택에 push한다.
            for c in range(V + 1):
                if AM[node][c] == 1 and visited[c] == 0:
                    stack.append(c)
    print(stack)
    print(visited)
    print(travel)
DFS(V, AM, 1)
#################################
def DFS_AL(V, AL, sv):
    visited = [0] * (V+1)
    stack = [sv]
    travel = []
    # 스택에 내용이 있는 동안
    while len(stack):
        # 스택에서 pop.
        node = stack.pop()
        # 방문 했는지 안했는지 확인해서, 방문을 안 했을때
        if not visited[node]:
            # 1. 방문 표시를 한다.
            visited[node] = 1
            travel.append(node)
            # 2. node와 연결되어 있으면서 아직 방문하지 않은 node를 스택에 push한다.
            for i in AL[node]:
                if not visited[i]:
                    stack.append(i)
    print(stack)
    print(visited)
    print(travel)

DFS_AL(V, AL, 1)
###########################

# 재귀 사용
# v는 방문되지 않은 정점으로, 방문하러 들어옴.
# visited[v] = 1 -> 방문처리를 한다
# v와 연결된 것 중에 방문하지 않을 것을 찾아 DFS를 호출한다.
visited = [0] * (V+1)
travel = []
def DFS_re(AL, v, visited):
    visited[v] = 1
    travel.append(v)
    for w in AL[v]:
        if not visited[w]:
            DFS_re(AL, w, visited)
DFS_re(AL, 1, visited)
print(visited)