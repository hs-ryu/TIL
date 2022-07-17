def DFS():
    pass


def BFS(x):
    q = graphs[x][:]
    for i in range(len(q)):
        q[i].append(0)
    while q:
        print(q)
        temp, dist, plus = q.pop(0)
        if visited[temp] == 0:
            visited[temp] = dist + plus
            for i in range(len(graphs[temp])):
                if visited[graphs[temp][i][0]]:
                    q.append(graphs[temp][i] + [visited[temp]])


n = int(input())

graphs = [[] for _ in range(n+1)]

for i in range(n-1):
    n1,n2,c = map(int,input().split())
    graphs[n1].append([n2,c])
    graphs[n2].append([n1,c])
# print(graphs)

# 1. 1번부터 제일 멀리 있는놈 찾기.(루트노드 1번)
# 2. 그놈부터 제일 멀리있는놈 찾기.

# BFS ㄱ
visited = [0] * (n+1)
BFS(1)
print(visited)