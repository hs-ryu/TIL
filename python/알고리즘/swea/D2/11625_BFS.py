'''
def BFS(s):
    q = [s]
    visited[s] = 1
    while q:
        x = q.pop(0)
        result.append(x)
        for i in AL[x]:
            if visited[i] == 0:
                q.append(i)
                visited[i] = 1

T = int(input())
for t in range(1, T+1):
    V, E = map(int ,input().split())
    AL = [[] for _ in range(V+1)]
    for i in range(E):
        s, e = map(int, input().split())
        AL[s].append(e)
        AL[e].append(s)
    visited = [0] * (V+1)
    # print(AL)
    result = []
    BFS(1)
    print('#%d %s' %(t, ' '.join(map(str, result))))
    # print(result)
'''



# 재귀로 해보기
def BFS(s):
    result.append(s)
    visited[s] = 1
    for x in AL[s]:
        if visited[x] == 0 and (x not in q):
            q.append(x)
    if q:
        BFS(q.pop(0))

T = int(input())
for t in range(1, T+1):
    V, E = map(int ,input().split())
    AL = [[] for _ in range(V+1)]
    for i in range(E):
        s, e = map(int, input().split())
        AL[s].append(e)
        AL[e].append(s)
    visited = [0] * (V+1)
    result = []
    q = [1]
    visited = [0] * (V+1)
    BFS(q.pop(0))
    print('#%d %s' %(t, ' '.join(map(str, result))))