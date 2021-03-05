import sys
sys.stdin = open('sample_input(6).txt')


def BFS(s):
    visited[s] = 1
    Q.append(s)

    while Q:
        k = Q.pop(0)
        for i in AL[k]:
            if not visited[i]:
                Q.append(i)
                visited[i] = visited[k] + 1

T = int(input())
for t in range(1, T+1):
    V, E = map(int, input().split())
    x = []
    for _ in range(E):
        x.append(list(map(int,input().split())))
    S, G = map(int, input().split())
    AL = [[] for i in range(V+1)]
    for i, j in x:
        AL[i].append(j)
        AL[j].append(i)
    visited = [0 for i in range(V+1)]
    Q = []
    BFS(S)
    result = visited[G]-1 if visited[G] else 0
    print('#%d %d' %(t, result))

