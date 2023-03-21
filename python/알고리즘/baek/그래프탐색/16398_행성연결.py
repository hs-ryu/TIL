# 크러스컬. pypy만 통과.

from sys import stdin
input = stdin.readline

def find(x):
    while parents[x] != x:
        x = parents[x]
    return x

def union(x,y):
    parents[find(x)] = find(y)

n = int(input())
graph = [list(map(int,input().split())) for _ in range(n)]

info = []
for i in range(n):
    for j in range(i+1,n):
        info.append([i,j,graph[i][j]])
info.sort(key=lambda x:x[2])
parents = [i for i in range(n+1)]

result = 0
for x,y,l in info:
    if find(x) != find(y):
        union(x,y)
        result += l
print(result)