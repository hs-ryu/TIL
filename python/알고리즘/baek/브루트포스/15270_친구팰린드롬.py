from sys import stdin
input = stdin.readline

# DFS
def DFS():
    pass


n, m = map(int, input().split())

freinds = [[] for _ in range(n+1)]

for i in range(m):
    u, v = map(int, input().split())
    freinds[u].append(v)
print(freinds)