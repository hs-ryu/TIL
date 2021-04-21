import sys
sys.stdin = open('sample_input.txt')

def DFS(s, level):
    global max_cnt
    if max_cnt < level:
        max_cnt = level
    visited[s] = 1
    for x in AL[s]:
        if visited[x] == 0:
            DFS(x, level+1)
    visited[s] = 0

T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    AL = [[] for i in range(N+1)]
    for i in range(M):
        x, y = map(int, input().split())
        AL[x].append(y)
        AL[y].append(x)
    max_cnt = 0
    for i in range(1, N+1):
        visited = [0] * (N+1)
        DFS(i,1)
    
    print('#%d %d' %(t, max_cnt))

