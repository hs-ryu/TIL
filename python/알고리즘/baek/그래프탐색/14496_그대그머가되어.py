def BFS(i):
    global result
    q = [[i,0]]
    while q:
        now,cnt = q.pop(0)
        if now == b:
            result = min(result, cnt)
        for j in range(len(relation[now])):
            if not visited[relation[now][j]]:
                visited[relation[now][j]] = 1
                q.append([relation[now][j], cnt+1])

a,b = map(int,input().split())
n,m = map(int,input().split())

relation = [[] for _ in range(n+1)]

for _ in range(m):
    one,two = map(int,input().split())
    relation[one].append(two)
    relation[two].append(one)
print(relation)
visited = [0] * (n+1)
visited[a] = 1
result = 1000000001
BFS(a)
if result == 1000000001:
    print(-1)
else:
    print(result)