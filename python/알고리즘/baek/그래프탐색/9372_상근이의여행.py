from sys import stdin
input = stdin.readline

t = int(input())
def DFS(x,cnt):
    visited[x] = 1
    for i in lst[x]:
        if visited[i] == 0:
            cnt = DFS(i, cnt+1)
    return cnt

for _ in range(t):
    n,m = map(int, input().split())
    lst = [[] for _ in range(n+1)]
    visited = [0] * (n+1)
    for i in range(m):    
        a,b = map(int,input().split())
        lst[a].append(b)
        lst[b].append(a)
    print(DFS(1,0))
